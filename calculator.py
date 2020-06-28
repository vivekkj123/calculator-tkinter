from tkinter import *

window = Tk()
window.geometry('360x640')
window.resizable(False, False)
window.title("Calculator By Vivek K J")
screen = Entry(window, textvariable=window, font=("Verdana", 35,), bd=12,
               insertwidth=4, width=11, justify=RIGHT, bg='#fff', state='disabled')
screen.grid(columnspan=3)

button7 = Button(window, text='7', height=4, width=8)
button8 = Button(window, text='8', height=4, width=8)
button9 = Button(window, text='9', height=4, width=8)
button4 = Button(window, text='4', height=4, width=8)
button5 = Button(window, text='5', height=4, width=8)
button6 = Button(window, text='6', height=4, width=8)
button1 = Button(window, text='1', height=4, width=8)
button2 = Button(window, text='2', height=4, width=8)
button3 = Button(window, text='3', height=4, width=8)

button7.grid(row=1, column=0, pady=30)
button8.grid(row=1, column=1, pady=30)
button9.grid(row=1, column=2, pady=30)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button1.grid(row=3, column=0, pady=30)
button2.grid(row=3, column=1, pady=30)
button3.grid(row=3, column=2, pady=30)


mainloop()
