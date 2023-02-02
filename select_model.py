import glob

def select(env='colab'):
    himAP = 0
    if env == 'colab':
        list_of_files = glob.glob('/content/drive/MyDrive/Programmieren/Python/Smarty/dataset/models/*.pt')
    elif env == 'local':
        list_of_files = glob.glob('dataset/models/*.pt')
    for file in list_of_files:
        if 'last' in file:
            list_of_files.remove(file)
    for file in list_of_files:
        mAP = float(file.split('mAP-')[1].split('_')[0])
        if mAP > himAP:
            himAP = mAP
            latest_file = file
    return latest_file