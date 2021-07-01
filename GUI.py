import numpy as np
import pandas as pd
import os
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
from PIL import Image, ImageTk
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
from PIL import Image, ImageTk

windown = Tk()
windown.title("Test Dog")
windown.geometry("450x500")

def showimage():
    global text_image
    global text_diachi
    filename = filedialog.askopenfilename(initialdir="D:\HK6\machine_learning\đồ án\dog\Alaskan Malamute dog",
                                                  title="Select Image File",
                                                  filetypes=(
                                                  ("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
    text_image = ""
    text_image = filename
    img = Image.open(text_image)
    img.thumbnail((350, 350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    lable_rootfile.destroy()
def sendmodel():
    global lable_rootfile
    directory = 'C:/Users/DELL/Downloads/class dog'

    mapping = {'Bocker dog': 0, 'Belgian Tervuren dog': 1, 'Corgi dog': 2, 'Borzoi_dog': 3, 'Boxer dog': 4,
           'Beagle dog': 5, 'Bulldog dog': 6, 'Phu Quoc dog': 7, 'Bugg dog': 8, 'Bichon Frise dog': 9,
           'Afgan Hound dog': 10, 'Akita dog': 11, 'Alaskan Malamute dog': 12}
    reverse_mapping = {0: 'Bocker dog', 1: 'Belgian Tervuren dog', 2: 'Corgi dog', 3: 'Borzoi_dog', 4: 'Boxer dog',
                   5: 'Beagle dog', 6: 'Bulldog dog', 7: 'Phu Quoc dog', 8: 'Bugg dog', 9: 'Bichon Frise dog',
                   10: 'Afgan Hound dog', 11: 'Akita dog', 12: 'Alaskan Malamute dog'}

    print(mapping)
    print(reverse_mapping)

    def mapper(value):
        return reverse_mapping[value]

    model = load_model('DenseNet201_TestDog90.h5')

    image = load_img(text_image, target_size=(180, 180))

    image = img_to_array(image)
    image = image / 255.0
    prediction_image = np.array(image)
    prediction_image = np.expand_dims(image, axis=0)
    prediction = model.predict(prediction_image)
    value = np.argmax(prediction)
    move_name = mapper(value)
    # print("Prediction is {}.".format(move_name))
    lable_rootfile = Label(windown, text="Giống chó này là:{}".format(move_name))
    lable_rootfile.pack(side=BOTTOM, fill="both")
frm = Frame(windown)
frm.pack(side=BOTTOM, padx=15, pady=15)
lbl = Label(windown)
lbl.pack( padx=15, pady=15)
btn = Button(frm, text="Browse Image",command=showimage)
btn.pack(side=tk.LEFT)
btn2 = Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)
btn3 = Button(frm, text="Test", command=sendmodel)
btn3.pack(side=tk.LEFT, padx=10)
windown.mainloop()