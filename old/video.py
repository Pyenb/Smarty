from imageai.Detection.Custom import CustomVideoObjectDetection
from select_model import select
import json, cv2

latest_file = select()
print(latest_file)

settings_file = open('/content/drive/MyDrive/Programmieren/Python/Smarty/data-collection/settings.json', 'r')
settings = json.loads(settings_file.read())
settings_file.close()

def set_total(input_file):
    global total_frames
    cap = cv2.VideoCapture(input_file)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames: {total_frames}")

def forFrame(frame_number, output_array, output_count):
    print(f"{frame_number} / {total_frames}")
    output = open(settings["Files"]["output_file_path"], 'a+')
    output.write(json.dumps({"frame_number": frame_number, "output_array": output_array, "output_count": output_count}) + "\n")
    output.close()

def detection(input_file_path, output_file_path, frames_per_second, minimum_percentage_probability, save_video=True):
    set_total(input_file_path)
    video_detector = CustomVideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    video_detector.setModelPath(latest_file)
    video_detector.setJsonPath(settings["Files"]["json_file_path"])
    video_detector.loadModel()

    video_detector.detectObjectsFromVideo(input_file_path=input_file_path,
                                            output_file_path=output_file_path,
                                            frames_per_second=frames_per_second,
                                            per_frame_function=forFrame,
                                            minimum_percentage_probability=minimum_percentage_probability,
                                            save_detected_video=save_video)