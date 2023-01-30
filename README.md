# Smarty

Smarty is a project that utilizes [ImageAI](https://github.com/OlafenwaMoses/ImageAI) to detect cars from the brand *Smart* on the road.\
This is done through a [dataset](https://app.roboflow.com/anon-vqjqq/smarty) I compiled and annotated, consisting of around 430 pictures (for now at least).\
The 

## Prerequisites

- Python 3+

## Dependencies
 
To install ImageAI, run the python installation instruction below in the command line:

- [Download and Install](https://www.python.org/downloads/) **Python 3.7**, **Python 3.8**, **Python 3.9** or **Python 3.10**
- Install dependencies
  - Download `requirements.txt` file and install via the command
    
    ```bash
    > pip install -r requirements.txt
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
