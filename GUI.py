from tkinter import *
from tkinter import ttk

title = "GUI"
width = 400
height = 300

root = Tk()
root.title(title)
root.geometry(f"{width}x{height}")

F = ttk.Frame(root, height=height, width=width)
F.grid(row=10, column=10)

button1 = ttk.Button(F, text="Button 1")
button1.grid(row=0, column=0)

button2 = ttk.Button(F, text="Button 2")
button2.grid(row=0, column=1)

button3 = ttk.Button(F, text="Button 3")
button3.grid(row=1, column=0)

button4 = ttk.Button(F, text="Button 4")
button4.grid(row=1, column=1)

button5 = ttk.Button(F, text="Button 5")
button5.grid(row=2, column=0)

button6 = ttk.Button(F, text="Button 6")
button6.grid(row=2, column=1)

button7 = ttk.Button(F, text="Button 7")
button7.grid(row=3, column=0)

button8 = ttk.Button(F, text="Button 8")
button8.grid(row=3, column=1)

button9 = ttk.Button(F, text="Button 9")
button9.grid(row=4, column=0)

button10 = ttk.Button(F, text="Button +")
button10.grid(row=4, column=1)

button11 = ttk.Button(F, text="Button =")
button11.grid(row=5, column=1)

textfield = ttk.Entry(F)
textfield.grid(row=6, column=0, columnspan=2)

button1.event_add("<<Button1Click>>", "<Button-1>")
button1.bind("<<Button1Click>>", lambda e: buttonHandler(e, "1"))
button2.event_add("<<Button2Click>>", "<Button-1>")
button2.bind("<<Button2Click>>", lambda e: buttonHandler(e, "2"))
button3.event_add("<<Button3Click>>", "<Button-1>")
button3.bind("<<Button3Click>>", lambda e: buttonHandler(e, "3"))
button4.event_add("<<Button4Click>>", "<Button-1>")
button4.bind("<<Button4Click>>", lambda e: buttonHandler(e, "4"))
button5.event_add("<<Button5Click>>", "<Button-1>")
button5.bind("<<Button5Click>>", lambda e: buttonHandler(e, "5"))
button6.event_add("<<Button6Click>>", "<Button-1>")
button6.bind("<<Button6Click>>", lambda e: buttonHandler(e, "6"))
button7.event_add("<<Button7Click>>", "<Button-1>")
button7.bind("<<Button7Click>>", lambda e: buttonHandler(e, "7"))
button8.event_add("<<Button8Click>>", "<Button-1>")
button8.bind("<<Button8Click>>", lambda e: buttonHandler(e, "8"))
button9.event_add("<<Button9Click>>", "<Button-1>")
button9.bind("<<Button9Click>>", lambda e: buttonHandler(e, "9"))
button10.event_add("<<Button10Click>>", "<Button-1>")
button10.bind("<<Button10Click>>", lambda e: buttonHandler(e, "+"))
button11.event_add("<<Button11Click>>", "<Button-1>")
button11.bind("<<Button11Click>>", lambda e: equalsHandler(textfield.get()))

def buttonHandler(event, value):
    textfield.insert(END, value)

def equalsHandler(event):
    expression = textfield.get()
    try:
        result = eval(expression)
    except:
        result = "Error"
    print(result)
    textfield.delete(0, END)
    textfield.insert(END, result)

F.mainloop()