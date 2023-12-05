import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()

frame = Frame()
frame.pack()
root.geometry("400x400")
root.configure(background="#94b1a5")

boy_label = Label(root, text="Boy (cm)", font="Denmark, 12", bg="#94b1a5")
boy_label.pack(pady=10)

boy_entry = Entry(root)
boy_entry.pack(pady=10)

def get_boy():
    try:
        boy_value = int(boy_entry.get())
        print("Boy Girildi:", boy_value)
    except ValueError:
        print("Please enter a valid integer for Boy.")

kilo_label = Label(root, text="Kilo (kg)", font="Denmark, 12", bg="#94b1a5")
kilo_label.pack(pady=10)

kilo_entry = Entry(root)
kilo_entry.pack(pady=10)

def get_kilo():
    try:
        kilo_value = float(kilo_entry.get())
        print("Kilo Girildi :", kilo_value)
    except ValueError:
        print("Lütfen Kilonuzu Rakam ile Giriniz")

def calculate_bmi():
    try:
        boy_value = int(boy_entry.get())
        kilo_value = float(kilo_entry.get())
        bmi = kilo_value / ((boy_value / 100) ** 2)
        print("BMI calculated:", bmi)

        # Classify the BMI
        if bmi <= 18.5:
            result = "İyi bir beslenmeye ihtiyacın var. Biraz zayıfsın"
        elif bmi <= 24.9:
            result = "HARİKASIN"
        elif bmi <= 29.9:
            result = "Biraz Kilo Probleminiz Var"
        else:
            result = "OBEZ!!"

        # Show the result in a pop-up window
        messagebox.showinfo("BMI Result", result)

    except ValueError:
        print("Error calculating BMI. Please enter valid values for Boy and Kilo.")

send_button = Button(root, text="SONUÇ", command=calculate_bmi)
send_button.pack(pady=10)

root.mainloop()
