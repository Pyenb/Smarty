import sys, os, cv2, json
from pytube import YouTube
from tqdm.auto import tqdm
from time import sleep

SMARTY_PATH = '/content/drive/MyDrive/Programmieren/Python/Smarty'
SETTINGS_FILE_PATH = os.path.join(SMARTY_PATH, 'data-collection/settings.json')

sys.path.insert(1, SMARTY_PATH)
from video_detection import detection

def load_settings():
    global SETTINGS
    with open(SETTINGS_FILE_PATH, 'r') as settings_file:
        SETTINGS = json.load(settings_file)

load_settings()

def bool_input(question, default):
    answer = input(question).lower()
    if answer == "y": return True
    elif answer == "n": return False
    elif answer == "": return default
    else: return bool_input(question, default)

def download_youtube_video(video_url, video_dir):
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    video_path = video.download(output_path=video_dir)
    print(f'{video.title} - loaded.')
    return video_path, yt.video_id

def capture_frames(video_path, frame_list, screenshot_dir, video_ID):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    progress_bar = tqdm(frame_list, desc=f"Screenshotting", unit="frame")
    
    for frame_number in progress_bar:
        frame_time = frame_number / fps
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_time * fps))
        ret, frame = cap.read()
        
        if ret:
            output_pictures = os.path.join(screenshot_dir, f"{video_ID}_{frame_number}.png")
            cv2.imwrite(output_pictures, frame)
            progress_bar.set_postfix({"Frame": frame_number})
    
    progress_bar.close()
    cap.release()
    cv2.destroyAllWindows()

def capture_youtube_screenshots(video_url, frame_list, detection_result_path, screenshot_dir, video_dir):
    video_path, video_ID = download_youtube_video(video_url, video_dir)
    if not bool_input("Skip detection? (y/N): ", False):
        detected = video_path.replace(".mp4", "_detected")
        detection(video_path, detected, SETTINGS["Detection"]["output_FPS"], SETTINGS["Detection"]["minimum_probability"], SETTINGS["Detection"]["save_detected_video"])
        try: os.remove(detected)
        except: pass
    print("Waiting 10 seconds for screenshots to load...")
    sleep(10)
    capture_frames(video_path, frame_list, screenshot_dir, video_ID)
    
    if bool_input("Delete files? (Y/n): ", True):
        os.remove(video_path)
        os.remove(detection_result_path)

def get_frames(detection_result_path, snip_at=20, all_frames=False):
    frames = []
    if not os.path.exists(detection_result_path):
        open(detection_result_path, 'w+').close()
    
    with open(detection_result_path, 'r') as frame_file:
        counter = 0
        
        for line in frame_file.readlines():
            if all_frames or counter == snip_at:
                frame = json.loads(line)
                if frame['output_count'] != {}:
                    frames.append(frame['frame_number'])
                counter = 0
            counter += 1
    
    return frames

def main():
    video_url = input("Video URL: ") or "https://www.youtube.com/watch?v=V2rxegdBpD0"
    
    all_frames = bool_input("Take all detected frames? (Y/n): ", True)
    screenshot_dir = SETTINGS["Files"]["screenshot_output_path"]
    video_dir = SETTINGS["Files"]["video_output_path"]
    detection_result_path = SETTINGS["Files"]["output_file_path"]
    
    capture_youtube_screenshots(video_url, get_frames(detection_result_path, SETTINGS["Screenshots"]["every_N_frames"], all_frames), detection_result_path, screenshot_dir, video_dir)

if __name__ == "__main__":
    main()