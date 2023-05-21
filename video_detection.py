from imageai.Detection.Custom import CustomVideoObjectDetection
from select_model import select
from tqdm.auto import tqdm
import json, cv2

latest_file = select()
print(latest_file)

SETTINGS_FILE_PATH = '/content/drive/MyDrive/Programmieren/Python/Smarty/data-collection/settings.json'

def load_settings():
    global SETTINGS
    with open(SETTINGS_FILE_PATH, 'r') as settings_file:
        SETTINGS = json.load(settings_file)

load_settings()

def set_total(input_file):
    global total_frames
    cap = cv2.VideoCapture(input_file)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

def for_frame(frame_number, output_array, output_count):
    progress_bar.set_description(f"Processing {frame_number}/{total_frames}")
    progress_bar.update(1)
    with open(SETTINGS["Files"]["output_file_path"], 'a+') as output:
        output.write(json.dumps({"frame_number": frame_number, "output_array": output_array, "output_count": output_count}) + "\n")

def detection(input_file_path, output_file_path, frames_per_second, minimum_percentage_probability, save_video=False):
    global progress_bar
    set_total(input_file_path)
    
    progress_bar = tqdm(total=total_frames, desc="Processing")
    
    video_detector = CustomVideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    video_detector.setModelPath(latest_file)
    video_detector.setJsonPath(SETTINGS["Files"]["json_file_path"])
    video_detector.loadModel()

    video_detector.detectObjectsFromVideo(input_file_path=input_file_path,
                                          output_file_path=output_file_path,
                                          frames_per_second=frames_per_second,
                                          per_frame_function=for_frame,
                                          minimum_percentage_probability=minimum_percentage_probability,
                                          save_detected_video=save_video)
    progress_bar.close()