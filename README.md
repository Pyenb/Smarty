# Smarty

Smarty is a project that utilizes [ImageAI](https://github.com/OlafenwaMoses/ImageAI) to detect cars from the brand *Smart* on the road.\
This is done through a [dataset](https://app.roboflow.com/anon-vqjqq/smarty) I compiled and annotated, consiting of around 430 pictures (for now at least).\
The 

## Prerequisites

- Python 3+
- [ImageAI](https://github.com/OlafenwaMoses/ImageAI) 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages from the `requirements.txt`.

```bash
> pip install cython pillow>=7.0.0 numpy>=1.18.1 opencv-python>=4.1.2 torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cpu torchvision>=0.10.0 --extra-index-url https://download.pytorch.org/whl/cpu pytest==7.1.3 tqdm==4.64.1 scipy>=1.7.3 matplotlib>=3.4.3 mock==4.0.3

> pip install cython pillow>=7.0.0 numpy>=1.18.1 opencv-python>=4.1.2 torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cu102 torchvision>=0.10.0 --extra-index-url https://download.pytorch.org/whl/cu102 pytest==7.1.3 tqdm==4.64.1 scipy>=1.7.3 matplotlib>=3.4.3 mock==4.0.3

> pip install pycocotools@git+https://github.com/gautamchitnis/cocoapi.git@cocodataset-master#subdirectory=PythonAPI

> pip install imageai --upgrade
```

## Installation

Use `git clone` to download the repository to your local machine:

```bash
> git clone https://github.com/Pyenb/Smarty
```

## Usage

The project is made for Google Colab, so the paths would need to be adjusted.\
The main files are `train.py`, `demo.py` and `video.py`

The `train.py` uses the data, from the folder *dataset* to train the model, the latest version can be found in *dataset/models*.

`demo.py` simply applies the model to all available pictures in the *images* folder:

![undetected](images/1.jpg?raw=true "Title")
![detect](images/1.jpg_detected.jpg?raw=true "Title")

![undetected](images/2.jpg?raw=true "Title")
![detect](images/2.jpg_detected.jpg?raw=true "Title")

`video.py` is just apply the model on the video in the *videos* folder:

![](https://github.com/Pyenb/Smarty/blob/master/videos/smart_detected.gif)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Disclaimer
This repository is for research purposes only, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.
