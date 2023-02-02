from imageai.Detection.Custom import DetectionModelTrainer
from select_model import select

latest_file = select()
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