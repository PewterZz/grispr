import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

directory = "./Trees"

def load_pngs(directory):
    """ Load all PNG files from a directory. """
    return [file for file in os.listdir(directory) if file.endswith('.png')]

def show_selected_image(event):
    """ Display the selected image. """
    file_name = dropdown_var.get()
    image_path = os.path.join(directory, file_name)
    image = Image.open(image_path)
    image = image.resize((250, 250)) 
    photo = ImageTk.PhotoImage(image)

    # Update the image label
    image_label.config(image=photo)
    image_label.image = photo

root = tk.Tk()
root.title("GRISPR")

root.geometry("500x500+100+100")

dropdown_var = tk.StringVar()
png_files = load_pngs(directory)
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=png_files)
dropdown.bind('<<ComboboxSelected>>', show_selected_image)
dropdown.pack(side='top', anchor='nw') 

image_label = tk.Label(root)
image_label.pack()

root.mainloop()
