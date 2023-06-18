from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window
root = Tk()
  
# Creating button. In this destroy method is passed
# as command, so as soon as button 1 is pressed root
# window will be destroyed
btn1 = Button(root, text ="Button 1", command = root.destroy)
btn1.pack(pady = 10)

btn3 = Button(root, text ="Button 3", command = btn1.destroy)
btn3.pack(pady = 10)  
# Creating button. In this destroy method is passed
# as command, so as soon as button 2 is pressed
# button 1 will be destroyed
def dt():
   root.destroy()
   mainloop()
   # btn1 = Button(root, text ="Button 1", command = root.destroy)
   # btn1.pack(pady = 10)
btn2 = Button(root, text ="Button 2", command = dt)
btn2.pack(pady = 10)
  
# infinite loop
mainloop()