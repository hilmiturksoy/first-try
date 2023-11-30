from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=30, borderwidth=5)
e.grid(padx=0, pady=0, columnspan=3)
e.get()

f_num = None
l_num = None
math_operation = None





# e.insert(0...)
def button_click(number):
    #e.delete(0,END)
    e.insert(END,number)

#Clear funk
def clear_button ():
    e.delete(0,END)

def toplama_islemi ():
    global f_num, l_num, math_operation
    f_num = float(e.get())
    math_operation = "toplama"
    e.delete(0, END)

def cıkarma_islemi():
    global f_num, l_num, math_operation
    f_num = float(e.get())
    math_operation = "cikarma"
    e.delete(0, END)

def carma_islemi():
    global f_num, l_num, math_operation
    f_num = float(e.get())
    math_operation = "carpma"
    e.delete(0, END)

def bolme_islemi():
    global f_num, l_num, math_operation
    f_num = float(e.get())
    math_operation = "bolme"
    e.delete(0, END)

def esittir():
    global f_num, l_num, math_operation
    l_num = float(e.get())
    e.delete(0, END)

    if math_operation =="toplama":
        e.insert(0, f_num+l_num)
    elif math_operation=="cikarma":
        e.insert(0,f_num - l_num)
    elif math_operation =="carpma":
        e.insert(0, f_num * l_num)
    elif math_operation == "bolme":
        e.insert(0, f_num/l_num)
        try:
            e.insert(0, f_num/l_num)
        except ZeroDivisionError:
            e.insert(0, "Hata")






# define buttons

button1 = Button(root, text="1", padx=30, pady=20, command=lambda :button_click(1))
button2 = Button(root, text="2", padx=30, pady=20, command=lambda :button_click(2))
button3 = Button(root, text="3", padx=30, pady=20, command=lambda :button_click(3))
button4 = Button(root, text="4", padx=30, pady=20, command=lambda :button_click(4))
button5 = Button(root, text="5", padx=30, pady=20, command=lambda :button_click(5))
button6 = Button(root, text="6", padx=30, pady=20, command=lambda :button_click(6))
button7 = Button(root, text="7", padx=30, pady=20, command=lambda :button_click(7))
button8 = Button(root, text="8", padx=30, pady=20, command=lambda :button_click(8))
button9 = Button(root, text="9", padx=30, pady=20, command=lambda :button_click(9))
button0 = Button(root, text="0", padx=30, pady=20, command=lambda :button_click(0))

button_nokta = Button(root, text=".", padx=30, pady=20, command=lambda :button_click("."))
button_topla = Button(root, text="+", padx=30, pady=20, command=toplama_islemi)
button_cıkar= Button(root, text="--", padx=30, pady=20, command=cıkarma_islemi)
button_bol= Button(root, text="bol", padx=30, pady=20, command=bolme_islemi)
button_carp= Button(root, text="x", padx=30, pady=20, command=carma_islemi)
button_clear= Button(root, text="Clear", padx=40, pady=20, command=clear_button)
button_esittir = Button(root, text="=", padx=30, pady=20, command=esittir)


# put the buttons on screen
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4, column=1)


button_nokta.grid(row=4, column=0)
button_topla.grid(row=4,column=2)
button_cıkar.grid(row=5,column=0)
button_carp.grid(row=5, column=1)
button_bol.grid(row=6, column=2, columnspan=3)
button_clear.grid(row=6, column=0, columnspan=2)
button_esittir.grid(row=5, column=2, columnspan=3)

# myButton = Button(root, text="enter num", command=click)

root.mainloop()
