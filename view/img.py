import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from src import config as cfg
import tkinter as tk
from PIL import Image, ImageTk

def setImgFrame(root):
    # Create a frame to contain the image
    image_frame = tk.Frame(root)
    # Add the frame to the root window
    image_frame.pack()
    
    return image_frame

def get_image_from_frame(image_frame):
    # Iterate through the children of image_frame
    for child in image_frame.winfo_children():
        # Check if the child is a Label object
        if isinstance(child, tk.Label):
            # Check if the Label has the 'img_tk' attribute
            if hasattr(child, 'img_tk'):
                # If yes, return the img_tk object (which is the image)
                return child.img_tk
    # If no image was found, you can return None or take appropriate action.
    return None

def setImages(self, pathImg, frameWidth, frameHeight, frameImg):
    try:
        # Destroy all widgets (e.g., labels) inside the frameImg
        for widget in frameImg.winfo_children():
            widget.destroy()
    except:
        pass
    # Open the image using Pillow
    img = Image.open(pathImg)

    # Resize the image to fit the frame size
    img = img.resize((frameWidth, frameHeight), Image.ANTIALIAS)

    # Convert the Pillow image to a format supported by Tkinter
    img = ImageTk.PhotoImage(img)

    # Create a label and place the image in it
    label = tk.Label(frameImg, image=img)
    label.image = img  # Keep a reference to the image to prevent garbage collection
    label.pack(fill=tk.BOTH, expand=True)

def trySetPathToimg(mode, name, default):
    # Determine the path to the resources directory based on the 'mode' value
    resources_path = f'{cfg.RESOURCES}/{mode}/'
    name=name.replace(' ', '_')
    # Create the full path to the image file
    image_path = os.path.join(resources_path, f'{name}.png')
    
    # Check if the file exists
    if os.path.isfile(image_path):
        return image_path  # If it exists, return the path to the image file
    else:
        return default  # If it doesn't exist, return the default value