from tkinter import *

window = Tk()
window.geometry('390x640')
window.resizable(False, False)
window.title("Calculator By Vivek K J")
screen = Entry(window, textvariable=window, font=("Verdana", 35,), bd=12,
               insertwidth=4, width=12, justify=LEFT, bg='#fff')
screen.grid(columnspan=4)

button7 = Button(window, text='7', height=2, width=4, command=lambda:setInput("7"))
button8 = Button(window, text='8', height=2, width=4, command=lambda:setInput("8"))
button9 = Button(window, text='9', height=2, width=4, command=lambda:setInput("9"))
button4 = Button(window, text='4', height=2, width=4, command=lambda:setInput("4"))
button5 = Button(window, text='5', height=2, width=4, command=lambda:setInput("5"))
button6 = Button(window, text='6', height=2, width=4, command=lambda:setInput("6"))
button1 = Button(window, text='1', height=2, width=4, command=lambda:setInput("1"))
button2 = Button(window, text='2', height=2, width=4, command=lambda:setInput("2"))
button3 = Button(window, text='3', height=2, width=4, command=lambda:setInput("3"))
button0 = Button(window, text='0', height=2, width=4, command=lambda:setInput("0"))
buttonequal = Button(window, text='=', height=2, width=4, command=lambda:setInput("="))
buttonmultiple = Button(window, text='*', height=2, width=4, command=lambda:setInput("*"))
buttonaddition = Button(window, text='+', height=2, width=4, command=lambda:setInput("+"))
buttonminus = Button(window, text='-', height=2, width=4, command=lambda:setInput("-"))
buttondivision = Button(window, text='/', height=2, width=4, command=lambda:setInput("/"))
buttonclear = Button(window, text='AC', height=2, width=4, command=lambda:clearfun(""))
buttondot = Button(window, text='.', height=2, width=4, command=lambda:setInput("."))

buttonclear.grid(row=1, column=0, pady=30)
buttondivision.grid(row=2, column=3, pady=30)
buttonmultiple.grid(row=3, column=3, pady=30)
buttonminus.grid(row=4, column=3, pady=30)
buttonaddition.grid(row=5, column=3, pady=30)
buttonequal.grid(row=5, column=2, pady=30)
button0.grid(row=5, column=1, pady=30)
buttondot.grid(row=5, column=0, pady=30)
button7.grid(row=2, column=0, pady=30)
button8.grid(row=2, column=1, pady=30)
button9.grid(row=2, column=2, pady=30)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button1.grid(row=4, column=0, pady=30)
button2.grid(row=4, column=1, pady=30)
button3.grid(row=4, column=2, pady=30)


def setInput(text):
    screen.insert(30, text)

def clearfun(text):
    screen.delete(0, "end")

mainloop()
