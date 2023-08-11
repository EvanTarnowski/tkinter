import tkinter as tk
import os
from PIL import ImageTk, Image
from tkinter import font

os.environ['DISPLAY']=":0"

window = tk.Tk()
window.attributes('-fullscreen', True)

img = ImageTk.PhotoImage(Image.open("couple.jpg"))
image = tk.Label(
    window,
    image=img
)
image.place(relx=0.5, rely=0.5, anchor='center')

font = ("Comic Sans MS", 20, 'bold')
text = tk.Label(
    window,
    text='Hello World',
    font=font,
    foreground='blue'
    )
text.place(relx=0.5, rely=0.8, anchor='center')

button = tk.Button(
    window,
    text='close',
    command=window.quit
)
button.place(relx=0.5, rely=0.8, anchor='center')

window.mainloop()
