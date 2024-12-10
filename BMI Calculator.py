from tkinter import *

# Pencere ayarları
window = Tk()
window.title("BMI Calculator")
window.geometry("400x400")

# Etiketler ve giriş alanları
my_label = Label(window, text="BMI Calculator")  # Başlık
my_label.pack()

kg_label = Label(window, text="Enter weight in KG")  # Kilo etiketi
kg_label.pack()
kg_entry = Entry(window)  # Kilo girişi
kg_entry.pack()

cm_label = Label(window, text="Enter your height (cm)")  # Boy etiketi
cm_label.pack()
cm_entry = Entry(window)  # Boy girişi
cm_entry.pack()

result_label = Label(window, text="")  # Sonuç etiketi (başlangıçta boş)
result_label.pack()


# Hesaplama fonksiyonu
def calculate():
    try:
        # Kullanıcı girdilerini al
        kg = float(kg_entry.get())
        cm = float(cm_entry.get())

        # BMI hesapla
        bmi = kg / (cm / 100) ** 2

        # BMI sonuçlarını kontrol et ve mesaj oluştur
        if bmi < 18.5:
            message = f"Your BMI is {bmi:.2f}. You are underweight."
        elif 18.5 <= bmi <= 24.9:
            message = f"Your BMI is {bmi:.2f}. You have a normal weight."
        elif 25 <= bmi <= 29.9:
            message = f"Your BMI is {bmi:.2f}. You are overweight."
        else:
            message = f"Your BMI is {bmi:.2f}. You are obese."

        # Sonucu kullanıcıya göster
        result_label.config(text=message)

    except ValueError:
        # Geçersiz giriş durumunda hata mesajı göster
        result_label.config(text="Please enter valid numbers!")


# Hesaplama butonu
button = Button(window, text="CALCULATE", command=calculate)
button.pack()

# Tkinter ana döngüsü
window.mainloop()
