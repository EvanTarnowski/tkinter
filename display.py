import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font

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

window.mainloop()
