import tkinter as tk
from tkinter import *
from AI_Gui import thread_mutiii
from PIL import Image,ImageTk
from functools import partial

Gui = tk.Tk()
Gui.title("Trợ lý ảo")
Gui.geometry("500x500")
Gui.resizable(False, False)
Gui.configure(bg='white')

img_pil = Image.open("Image\\bot.jpg")
img_main = ImageTk.PhotoImage(img_pil.resize((300,200)))
img_label = tk.Label(image=img_main,border=0,bg="white")

record_open = Image.open(r"Image\\recording.png")
img_record= ImageTk.PhotoImage(record_open.resize((80,80)))
Record = tk.Button(Gui, image=img_record,border=0,bg='white')
Record.configure(command=partial(thread_mutiii, Gui,Record))
user_label = Label(Gui, text="User Talk:",border=0,bg='white',font=("Courier", 13 ,"bold"))
asssitant_label = Label(Gui,text="Assistant:",border=0,bg='white',font=("Courier", 13 ,"bold"))

user_label.place(x=40,y=200)
asssitant_label.place(x=40,y=250)
Record.place(x=50,y=390)
img_label.place(x=100,y=0)


Gui.mainloop()
