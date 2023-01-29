import tkinter as tk
import os,glob
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

# Other = 0
# Smart = 1

counter = 0
for folder in ['train', 'valid']:
    path = os.path.join(path, folder, 'labels')
    all = glob.glob(os.path.join(path, '*.txt'))
    for filename in all:
        with open(filename, 'r+') as f:
            text = f.read()
            type = text.split(' ')
            new = text.replace(type[0], '0')
            f.write(new)
            counter += 1
            print(f'{counter}/{len(all)}')