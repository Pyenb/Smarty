import sys, os, cv2, json
sys.path.insert(1, '/content/drive/MyDrive/Programmieren/Python/Smarty')

from pytube import YouTube
from pytube.cli import on_progress
from old.video import detection

settings_file = open('/content/drive/MyDrive/Programmieren/Python/Smarty/data-collection/settings.json', 'r')
settings = json.loads(settings_file.read())
settings_file.close()
output_file = settings["Files"]["output_file_path"]

def download_youtube_video(video_url, output_directory):
    global video
    yt = YouTube(video_url, on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    video_path = video.download(output_path=output_directory)
    
    print(f'Video {video.title} loaded.')
    return video_path

def capture_frames(video_path, frame_list, output_directory):
    # Frames erstellen
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    for frame_number in frame_list:
        # Frame-Position in Sekunden berechnen
        frame_time = frame_number / fps
        
        # Zum entsprechenden Frame springen
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_time * fps))
        
        # Frame abrufen
        ret, frame = cap.read()
        if ret:
            # Dateiname für den Screenshot erstellen
            output_pictures = os.path.join(output_directory, f"{video.title}_{frame_number}.png")
            
            # Screenshot speichern
            cv2.imwrite(output_pictures, frame)
            
            print(f"{video.title}_{frame_number}.png erstellt.")
    
    # Aufräumen
    cap.release()
    cv2.destroyAllWindows()

def capture_youtube_screenshots(video_url, frame_list, output_directory):
    video_path = download_youtube_video(video_url, output_directory)
    detected = video_path.replace(".mp4", "_detected")
    detection(video_path, detected, settings["Detection"]["output_FPS"], settings["Detection"]["minimum_probability"], bool(settings["Detection"]["save_detected_video"]))
    capture_frames(video_path, frame_list, output_directory)
    
    if input("Delete files? (Y/n): ").lower() or "y" == "y":
        os.remove(video_path)
        os.remove(detected)
        os.remove(output_file)

def get_frames(snip_at=0, all_frames=False):
    frames = []
    if not os.path.exists(output_file): open(output_file, 'w+').close()
    frame_file = open(output_file, 'r')
    for i in frame_file.readlines():
        if all_frames:
            frame = json.loads(i)
            if frame['output_count'] != {}:
                frames.append(frame['frame_number'])
        else:
            counter = 0
            if counter == snip_at:
                frame = json.loads(i)
                if frame['output_count'] != {}:
                    frames.append(frame['frame_number'])
                counter = 0
            counter += 1
    frame_file.close()
    return frames

video_url = input("Video-URL: ")
if video_url == "":
    video_url = "https://www.youtube.com/watch?v=V2rxegdBpD0"

all_frames = input("Take all detected frames? (Y/n): ").lower() or "y"
if all_frames == "y": all_frames = True
else: all_frames = False

output_dir = settings["Files"]["screenshot_output_path"]

capture_youtube_screenshots(video_url, get_frames(settings["Screenshots"]["every_N_frames"], all_frames), output_dir)