'''
install tinkter in python
'''

import os
import tkinter as tk
from tkinter import filedialog


def read_write():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    script = "leafpad " + file_path
    os.system(script)


if __name__ == "__main__":
    read_write()
