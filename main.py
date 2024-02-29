# Importing classes from shapes.py
# create window Tkinter
from tkinter import *
import tkinter as tk
import webbrowser

Window = Tk()
def main_button():
 hello["text"] = "Button Clicked"

def callback():
 webbrowser.open("http://www.google.com")

Window.title('hello world')
Window.geometry ("1920x1080")
hello = tk.Label(text="Click The Button")
hello.pack()
button = tk.Button(text="Click Me", command=main_button)
button.pack()

label2 = tk.Label(text="Click to open google")
label2.pack()

button2 = tk.Button(text="Google", command=callback)
button2.pack()

tk.mainloop()
