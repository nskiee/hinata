import tkinter
from tkinter import messagebox as mb
import hinata

window = tkinter.Tk()




def callHinata():
   #mb.showinfo( "Hello Python", "Hello World")
   ht = hinata.hinata()
   ht.startup(outputtextbox, window)


window.title("Aritifical Intelligent - Voice Assistant")
window.minsize(600,400)


hinatabutton = tkinter.Button(window, text ="Hinata!!!", command = callHinata)
hinatabutton.grid(column = 0 , row = 0)

label = tkinter.Label(window, text = "Output")
label.grid(column = 0, row = 1)

outputtextbox = tkinter.Text(window)
outputtextbox.grid(column = 0,row = 2)

window.mainloop()