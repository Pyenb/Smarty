from imageai.Detection.Custom import DetectionModelTrainer
import glob, os

list_of_files = glob.glob('/content/drive/MyDrive/Programmieren/Python/Smarty/dataset/models/*.pt')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="/content/drive/MyDrive/Programmieren/Python/Smarty/dataset")
trainer.setTrainConfig(
    object_names_array=["Smart"],
    batch_size=4,
    num_experiments=200#,
    train_from_pretrained_model=latest_file
    )
trainer.trainModel()