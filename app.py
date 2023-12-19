import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import threading
import time

base_directory = "./Trees"  # Change this to your base directory

def list_folders(directory):
    """ List all folders in a directory. """
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

def load_pngs(directory):
    """ Load all PNG files from a directory. """
    return [file for file in os.listdir(directory) if file.endswith('.png')]

def update_image_list(event):
    """ Update the list of images based on the selected folder. """
    folder = folder_var.get()
    global image_list
    image_list = load_pngs(os.path.join(base_directory, folder))
    global current_image_index
    current_image_index = 0
    show_image()

def resize_image(event):
    """ Resize the image based on the window size. """
    if not image_label.image:
        return
    new_width = event.width
    new_height = event.height
    image = Image.open(image_label.image_path)
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

def show_image():
    """ Display the selected image. """
    folder = folder_var.get()
    file_name = image_list[current_image_index]
    image_path = os.path.join(base_directory, folder, file_name)
    image = Image.open(image_path)

    # Dynamically resize the image based on the label size
    image = image.resize((image_label.winfo_width(), image_label.winfo_height()), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)

    # Update the image label
    image_label.config(image=photo)
    image_label.image = photo
    image_label.image_path = image_path

def next_image():
    """ Show next image. """
    global current_image_index
    if current_image_index < len(image_list) - 1:
        current_image_index += 1
        show_image()

def previous_image():
    """ Show previous image. """
    global current_image_index
    if current_image_index > 0:
        current_image_index -= 1
        show_image()

def toggle_autoplay():
    """ Toggle autoplay on/off. """
    global autoplay
    autoplay = not autoplay
    if autoplay:
        autoplay_button.config(text="Stop Autoplay")
        start_autoplay()
    else:
        autoplay_button.config(text="Start Autoplay")

def start_autoplay():
    """ Start autoplaying images. """
    def autoplay_loop():
        while autoplay and current_image_index < len(image_list) - 1:
            time.sleep(0.5)  # Change delay as needed
            next_image()

    if autoplay:
        threading.Thread(target=autoplay_loop).start()

root = tk.Tk()
root.title("GRISPR")
root.geometry("600x600+100+100")

folder_var = tk.StringVar()
folders = list_folders(base_directory)
folder_dropdown = ttk.Combobox(root, textvariable=folder_var, values=folders)
folder_dropdown.bind('<<ComboboxSelected>>', update_image_list)
folder_dropdown.pack(side='top', anchor='nw')

image_list = []
current_image_index = 0
autoplay = False

prev_button = tk.Button(root, text="<< Previous", command=previous_image)
prev_button.pack(side='left', anchor='sw')

next_button = tk.Button(root, text="Next >>", command=next_image)
next_button.pack(side='right', anchor='se')

autoplay_button = tk.Button(root, text="Start Autoplay", command=toggle_autoplay)
autoplay_button.pack(side='bottom', anchor='s')

image_label = tk.Label(root)
image_label.pack()

root.bind("<Configure>", resize_image)

root.mainloop()
