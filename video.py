from imageai.Detection.Custom import CustomVideoObjectDetection
from select_model import select

latest_file = select().replace("\\", "/")
print(latest_file)

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(latest_file)
video_detector.setJsonPath("/content/drive/MyDrive/Programmieren/Python/Smarty/dataset/json/dataset_yolov3_detection_config.json")
video_detector.loadModel()

video_detector.detectObjectsFromVideo(input_file_path="/content/drive/MyDrive/Programmieren/Python/Smarty/videos/smart.mp4",
                                          output_file_path="/content/drive/MyDrive/Programmieren/Python/Smarty/videos/smart_detected",
                                          frames_per_second=20,
                                          minimum_percentage_probability=20,
                                          log_progress=True)