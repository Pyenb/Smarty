from imageai.Detection.Custom import DetectionModelTrainer
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
        latest_file = file
print(latest_file)

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="/content/drive/MyDrive/Programmieren/Python/Smarty/dataset")
trainer.setTrainConfig(
    object_names_array=["Smart"],
    batch_size=4,
    num_experiments=200,
    train_from_pretrained_model=latest_file
    )
trainer.trainModel()