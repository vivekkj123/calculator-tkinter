from tkinter import *

window = Tk()
window.geometry('360x640')
window.resizable(False, False)
window.title("Calculator By Vivek K J")
screen = Entry(window, textvariable=window, font=("Verdana", 35,), bd=12,
               insertwidth=4, width=11, justify=RIGHT, bg='#fff', state='disabled')
screen.grid(columnspan=4)



mainloop()
