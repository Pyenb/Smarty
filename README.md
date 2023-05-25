
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
Smarty
</h1>
<h3 align="center">📍 Never lose a game of Smart again!</h3>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#%EF%B8%8F-project-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
- [🤖 Using Smarty](#-using-smarty)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [📃 License](#-license)
- [📚Disclaimer](#-disclaimer)

---

## 📍Overview

Smarty is a project that utilizes [ImageAI](https://github.com/OlafenwaMoses/ImageAI) to detect cars from the brand *Smart* on the road.
This is done through a [dataset](https://app.roboflow.com/anon-vqjqq/smarty) I compiled and annotated, consisting of around 430 pictures (for now at least).

---

## 🔮 Features

### Distinctive Features

1. **Architecture:** The project is built with ImageAI and YOLOv3, and provides a comprehensive set of scripts that enable users to quickly and easily start tracking Smarts.

2. **Progress Tracking:** The project also includes a progress bar to track the detection process, when using the youtube video analysis feature, as well as a function to save the output frames and counts to a JSON file.

3. **Latest Model Selection:** The project uses the glob and os modules to search for the `.pt` file with the highest mAP value, and stores the filepath of the latest version in the variable `latest_file`.

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
Smarty
├── data-collection
│   ├── bing_images.py
│   ├── dataconvert.py
│   ├── settings.json
│   └── youtube_analysis.py
├── dataset
│   ├── json
│   │   └── dataset_yolov3_detection_config.json
│   ├── models
│   │   └── yolov3_dataset_mAP-0.96238_epoch-11.pt
│   ├── train
│   │   ├── annotations
│   │   │   └── ...
│   │   └── images
│   │       └── ...
│   └── validation
│       ├── annotations
│       │   ├── classes.txt
│       │   └── ...
│       └── images
│           └── ...
├── demo.py
├── images
│   ├── 1.jpg
│   └── 1.jpg_detected.jpg
├── LICENSE.md
├── README.md
├── requirements.txt
├── select_model.py
├── train.py
├── video_detection.py
└── videos
    ├── smart_detected.gif
    ├── smart_detected.mp4
    └── smart.mp4

12 directories, many files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

| File               | Summary                                                                                                                                                                                                                                                                                       |
|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| demo.py            | This script uses ImageAI to detect objects from a given set of images and prints the name, percentage probability, and box points of the detected objects. The CustomObjectDetection module is used to set the model type and model path, while a JSON file is used to configure the dataset. |
| video_detection.py | This code script provides a function to detect objects in a Youtube video using the pretrained YOLOv3 model, to use in the dataset after annotating it. It also sets up a progress bar to track the detection process, as well as a function to save the output frames and counts to a JSON file.                                                           |
| train.py           | This code script sets up a custom model trainer using YOLOv3 and trains it from a pre-trained model on a given dataset. It also determines the latest file in the dataset and prints it out.                                                                                                  |
| select_model.py    | This code script uses the glob and os modules to search for the `.pt` file in the dataset/models directory with the highest mAP value and stores the filepath of the latest version in the variable `latest_file`.                                                                           |
| bing_images.py     | This script utilizes the `bing_images` module to download a specified number of images related to a given search query, such as "cars from brand 'smart'". The `download_images` function is used with parameters like the search query, number of images, pool size, and an option to force replace existing images.                                                                                                   |
| dataconvert.py     | This script allows the user to select a directory using a file dialog and then converts the labels in the text files present in the specified directory. It replaces the type value (0 or 1) in the text files with "0" for all files.                                                                                                                                                                               |
| youtube_analysis.py| This script performs various operations related to YouTube video analysis. It includes functionalities to download a YouTube video, capture frames from the video, perform object detection on the frames, and save screenshots. The script uses the `pytube` library to download YouTube videos and OpenCV for frame extraction and image saving. The `video_detection` module is imported for object detection using the YOLOv3 model. The script also loads settings from a JSON file and provides an interactive command-line interface for capturing screenshots from a YouTube video. |

## 🚀 Getting Started

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Pyenb/Smarty/blob/master/Smarty_training.ipynb)


### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `Python 3+`

### 💻 Installation

1. Clone the Smarty repository:
```sh
git clone https://github.com/Pyenb/Smarty
```

2. Change to the project directory:
```sh
cd Smarty
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

---

### 🤖 Using Smarty

The project is designed to be used with Google Colab, so some adjustments may be required for different environments.

- `train.py`
This script is used to train the model using the data from the dataset folder. It automatically finds the latest version of the model in the dataset/models directory.

- `demo.py`
This script applies the trained model to all available pictures in the images folder. It detects objects in the images and provides information such as the name, percentage probability, and box points of the detected objects.

![undetected](images/1.jpg?raw=true "Title")
![detect](images/1.jpg_detected.jpg?raw=true "Title")

- `video_detection.py`
This script provides a function to detect objects in YouTube videos using the pre-trained YOLOv3 model. It includes a progress bar to track the detection process and can save the output frames and object counts to a JSON file.

![](https://github.com/Pyenb/Smarty/blob/master/videos/smart_detected.gif)

- `select_model.py`
This script searches for the latest version of the model (.pt file) in the dataset/models directory based on the mean Average Precision (mAP) value. It stores the filepath of the latest version in the latest_file variable for further use.

- `bing_images.py`
The bing_images.py script allows you to download a specified number of images related to a search query using the bing_images module. It is useful for gathering image data for training or testing purposes.

- `dataconvert.py`
This script facilitates the conversion of label data by replacing type values in text files. It prompts the user to select a directory and then modifies the labels in the text files accordingly.

- `youtube_analysis.py`
The youtube_analysis.py script offers functionalities for YouTube video analysis. It can download a YouTube video, capture frames from the video, perform object detection on the frames, and save screenshots. The script relies on the pytube library for video downloading and uses OpenCV for frame extraction and image saving. The video_detection module is imported for object detection using the YOLOv3 model.

---

## 🛠 Future Development
- [X] [📌  Adding Youtube video analysis]
- [ ] [📌  Expanding Dataset]
- [ ] [📌  Label Studio ML backend for ML annotation]

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

### 📃 License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

---

## 📚 Disclaimer
This repository is for research purposes only, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.

---
