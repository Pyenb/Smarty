import sys, os, cv2, json
sys.path.insert(1, '/content/drive/MyDrive/Programmieren/Python/Smarty')

from pytube import YouTube
from pytube.cli import on_progress
from video import detection

def download_youtube_video(video_url, output_directory):
    # Video herunterladen
    yt = YouTube(video_url, on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    video_path = video.download(output_path=output_directory)
    
    print(video_path)
    return video_path

def capture_frames(video_path, frame_list, output_directory):
    # Frames erstellen
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    counter = 0
    for frame_number in frame_list:
        counter += 1
        # Frame-Position in Sekunden berechnen
        frame_time = frame_number / fps
        
        # Zum entsprechenden Frame springen
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_time * fps))
        
        # Frame abrufen
        ret, frame = cap.read()
        if ret:
            # Dateiname für den Screenshot erstellen
            ID = video_path.split('=')[1]
            output_file = os.path.join(output_directory, f"ID_{ID}_frame_{frame_number}.png")
            
            # Screenshot speichern
            cv2.imwrite(output_file, frame)
            
            print(f"{counter}: {output_file} erstellt.")
    
    # Aufräumen
    cap.release()
    cv2.destroyAllWindows()

def capture_youtube_screenshots(video_url, frame_list, output_directory):
    # Video herunterladen
    video_path = download_youtube_video(video_url, output_directory)
    
    detected = video_path.replace(".mp4", "_detected.mp4")
    detection(video_path, detected, 20, 40)
    
    # Frames erstellen
    capture_frames(video_path, frame_list, output_directory)
    
    # Video-Datei löschen
    os.remove(video_path)
    os.remove(detected)

def get_frames(snip_at):
    frames = []
    counter = 0
    output_file = open('/content/drive/MyDrive/Programmieren/Python/Smarty/data-collection/output.txt', 'r')
    for i in output_file.readlines():
        if counter == snip_at:
            frame = json.loads(i)
            if frame['output_count'] != {}:
                frames.append(frame['frame_number'])
            counter = 0
        counter += 1
    output_file.close()
    return frames

video_url = "https://www.youtube.com/watch?v=SgBzXAZy40s"
output_dir = "/content/drive/MyDrive/Programmieren/Python/Smarty/data-collection/screenshots"
capture_youtube_screenshots(video_url, get_frames(10), output_dir)