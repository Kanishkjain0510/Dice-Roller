import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x500")
window.title("Dice Roller")
window.config(bg="white")

jklu = "jklu.png"
jklu_image = ImageTk.PhotoImage(Image.open(jklu))
jklu_label = tk.Label(window, image=jklu_image)
jklu_label.image = jklu_image
jklu_label.place(x=150, y=0)

dice = ["one.png", "two.png", "three.png", "four.png", "five.png", "six.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window, image=image1)
label1.image = image1
label1.place(x=0, y=250)

label2 = tk.Label(window, image=image2)
label2.image = image2
label2.place(x=300, y=250)

def roll_dice():
    global image1, image2
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2

button = tk.Button(window, text="Roll the Dice", command=roll_dice)
button.place(x=202, y=300)

window.mainloop()
