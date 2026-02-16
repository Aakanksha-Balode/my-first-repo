# pip install Pillow
#import PIL
#print(PIL.__version__)


from itertools import cycle
from PIL import Image, ImageTK
import time
import tkinter as tk

root = tk.TK()
root.title("Image Slideshow Viewer")

# list of Image Path
image_paths = [
    r"C:\Users\nachiket\Pictures\photos\image.jpg"
    r"C:\Users\nachiket\Pictures\photos\image1.jpg"
    ]

# Resize the images to 1080x1080
image_size = (1080,1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image = photo_image)
        label.update()
        time.sleep(3)


slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        upade_image()


play_button = tk.Button(root, text = 'Play Slideshow', command = start_slideshow)
play_button.pack()

root.mainloop()

