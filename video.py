from imageai.Detection.Custom import CustomVideoObjectDetection
import glob

himAP = 0
list_of_files = glob.glob('/content/drive/MyDrive/Programmieren/Python/Smarty/dataset/models/*.pt')
for file in list_of_files:
    if 'last' in file:
        list_of_files.remove(file)
for file in list_of_files:
    mAP = float(file.split('mAP-')[1].split('_')[0])
    if mAP > himAP:
        himAP = mAP
        latest_file = file.replace("\\", "/")
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