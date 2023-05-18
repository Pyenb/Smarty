from imageai.Detection.Custom import CustomVideoObjectDetection
from select_model import select
import json

latest_file = select()
print(latest_file)

open("/content/drive/MyDrive/Programmieren/Python/Smarty/data-collection/output.txt", 'w+').close()

def forFrame(frame_number, output_array, output_count):
    #print(f'Frame: {frame_number} | Output: {output_array} | Count: {output_count}')
    open("/content/drive/MyDrive/Programmieren/Python/Smarty/data-collection/output.txt", 'a+').write(json.dumps({"frame_number": frame_number, "output_array": output_array, "output_count": output_count}) + "\n").close()

def detection(input_file_path, output_file_path, frames_per_second, minimum_percentage_probability):
    video_detector = CustomVideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    video_detector.setModelPath(latest_file)
    video_detector.setJsonPath("/content/drive/MyDrive/Programmieren/Python/Smarty/dataset/json/dataset_yolov3_detection_config.json")
    video_detector.loadModel()

    video_detector.detectObjectsFromVideo(input_file_path=input_file_path,
                                            output_file_path=output_file_path,
                                            frames_per_second=frames_per_second,
                                            per_frame_function=forFrame,
                                            minimum_percentage_probability=minimum_percentage_probability,
                                            log_progress=True)