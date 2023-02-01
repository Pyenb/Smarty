from imageai.Detection.Custom import CustomObjectDetection
import glob

himAP = 0
list_of_files = glob.glob('dataset\models\*.pt')
for file in list_of_files:
    if 'last' in file:
        list_of_files.remove(file)
for file in list_of_files:
    mAP = float(file.split('mAP-')[1].split('_')[0])
    if mAP > himAP:
        himAP = mAP
        latest_file = file
print(latest_file)

images = glob.glob('images\*.jpg')
for image in images:
    if 'detected' in image:
        continue
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(latest_file)
    detector.setJsonPath("dataset\json\dataset_yolov3_detection_config.json")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=image, output_image_path=image + "_detected.jpg")
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])