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
    
    def progress_callback(stream, chunk, bytes_remaining):
        bytes_downloaded = file_size - bytes_remaining
        progress_bar.update(bytes_downloaded - progress_bar.n)
    
    yt = YouTube(video_url, on_progress_callback=progress_callback)
    video = yt.streams.get_highest_resolution()
    
    file_size = video.filesize
    progress_bar = tqdm(total=file_size, unit='bytes', unit_scale=True, desc="Downloading")
    
    video_path = video.download(output_path=video_dir)
    
    progress_bar.close()
    
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

def capture_youtube_screenshots(video_url, detection_result_path, screenshot_dir, video_dir):
    video_path, video_ID = download_youtube_video(video_url, video_dir)
    if not bool_input("Skip detection? (y/N): ", False):
        detected = video_path.replace(".mp4", "_detected")
        detection(video_path, detected, SETTINGS["Detection"]["output_FPS"], SETTINGS["Detection"]["minimum_probability"], SETTINGS["Detection"]["save_detected_video"])
        try: os.remove(detected)
        except: pass
        print("Waiting 10 seconds for screenshots to load...")
        sleep(10)
    capture_frames(video_path, get_frames(detection_result_path), screenshot_dir, video_ID)
    
    if bool_input("Delete old files? (Y/n): ", True):
        os.remove(video_path)
        os.remove(detection_result_path)

def get_frames(detection_result_path):
    frames = []
    if not os.path.exists(detection_result_path):
        open(detection_result_path, 'w+').close()
    
    with open(detection_result_path, 'r') as frame_file:
        counter = 0
        
        frame_file_lines = frame_file.readlines()
        
        print("Removing frames without detected objects...")
        
        progress_bar = tqdm(total=len(frame_file_lines), desc="Removing", unit="frame")
        
        for line in frame_file_lines:
            frame = json.loads(line)
            if frame['output_count'] == {}:
                frame_file_lines.remove(line)
            progress_bar.update(1)
            
        progress_bar.close()
        
        print(f"Found {len(frame_file_lines)} potential frames.")
        all_frames = bool_input("Take all detected frames? (y/N): ", False)
        if not all_frames:
            N_frame = SETTINGS["Screenshots"]["every_N_frames"]
            snip_at = int(input(f"Make screenshot at every Nth frame | Default {N_frame}: ") or SETTINGS["Screenshots"]["every_N_frames"])
        
        for line in frame_file_lines:
            frame = json.loads(line)
            if all_frames or counter == snip_at:
                frames.append(frame['frame_number'])
                counter = 0
            counter += 1
    
    return frames

def main():
    video_url = input("Video URL: ") or "https://www.youtube.com/watch?v=V2rxegdBpD0"
    
    screenshot_dir = SETTINGS["Files"]["screenshot_output_path"]
    video_dir = SETTINGS["Files"]["video_output_path"]
    detection_result_path = SETTINGS["Files"]["output_file_path"]
    
    capture_youtube_screenshots(video_url, detection_result_path, screenshot_dir, video_dir)

if __name__ == "__main__":
    main()