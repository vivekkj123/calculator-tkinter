from tkinter import * #Importing All of TKinter

window = Tk()   #window Variable
window.configure(bg="#778899") #Window Background
window.geometry('380x660')  #Window Size
window.resizable(False, False)  #Disabled Window Resizing
window.title("Calculator By Vivek K J") #Window Title

icon = PhotoImage(file='logo.png')  #Window Favicon Variable
window.iconphoto(False, icon)   #Set window icon

screen = Entry(window, textvariable=window, font=("Courier", 35), bd=12, fg="#000000",
               insertwidth=4, width=12, justify=RIGHT, bg='#fff')   #Screen Of Calculator
screen.grid(columnspan=4, pady=10)
screen.focus()  #Set default focus to screen for better entry from keyboard
if __name__ == '__main__':
    button7 = Button(window, text='7', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("7"))
    button8 = Button(window, text='8', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("8"))
    button9 = Button(window, text='9', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("9"))
    button4 = Button(window, text='4', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("4"))
    button5 = Button(window, text='5', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("5"))
    button6 = Button(window, text='6', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("6"))
    button1 = Button(window, text='1', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("1"))
    button2 = Button(window, text='2', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("2"))
    button3 = Button(window, text='3', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("3"))
    button0 = Button(window, text='0', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                     activebackground="#ff6f61", command=lambda: setInput("0"))
    buttonequal = Button(window, text='=', height=2, width=4, borderwidth=4, relief="ridge", bg="#ffaa00",
                         activebackground="#ffaa00", command=lambda: equals(str(eval(screen.get()))))
    buttonmultiple = Button(window, text='*', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                            activebackground="#ff6f61", command=lambda: setInput("*"))
    buttonaddition = Button(window, text='+', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                            activebackground="#ff6f61", command=lambda: setInput("+"))
    buttonminus = Button(window, text='-', height=2, width=4, borderwidth=4, relief="ridge", bg="#424211",
                         activebackground="#ff6f61", command=lambda: setInput("-"))
    buttondivision = Button(window, text='÷', height=2, width=4, bg="#424211", activebackground="#ff6f61",
                            command=lambda: setInput("/"))
    buttonclear = Button(window, text='AC', height=2, width=4, bg="#ff0000", activebackground="#ff0000",
                         command=lambda: clearfun(""))
    buttondot = Button(window, text='.', height=2, width=4, bg="#424211", activebackground="#ff6f61",
                       command=lambda: setInput("."))

    buttonclear.grid(row=1, column=0, pady=30)      #Grid Setup of buttons
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

    window.bind('<Return>', lambda event: equals(str(eval(screen.get()))))  # Shortcut for result (Enter Key)
    window.bind('<KP_Enter>',
                lambda event: equals(str(eval(screen.get()))))  # Shortcut for result (Enter Key in numpad)


def setInput(text):     #Function For Button input
    screen.insert(30, text)


def clearfun(text):     #Function for Clear Button
    screen.delete(0, "end")


def equals(text):       #Function for finding result using eval function
    global evaluate
    evaluate = eval(text)
    screen.delete(0, "end")
    screen.insert(30, evaluate)


mainloop()      #Mainloop