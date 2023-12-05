import tkinter as tk
import pyautogui
import time
import sys

def mesaj():
    pyautogui.write(entry.get())
    pyautogui.press("enter")

def activate_function():
    while True:
        mesaj()
        time.sleep(0)

def exit_application():
    confirm_exit = tk.messagebox.askyesno("Çıkış", "Uygulamadan çıkmak istediğinizden emin misiniz?")
    if confirm_exit:
        root.destroy()
        sys.exit()

# Ana pencere oluşturuluyor
root = tk.Tk()
root.title("Whatsapp Milyar Mesaj")
root.geometry("500x500")
root.configure(bg="#FAD7A0")

# Başlık ekleniyor
label = tk.Label(root, text="Metin Girin", font=("Helvetica", 16))
label.pack(pady=10)

# Text box oluşturuluyor
entry = tk.Entry(root, width=40)
entry.pack(pady=20)

# Açıklama alanı oluşturuluyor ve sabit açıklama ekleniyor
description_text = tk.Text(root, height=5, width=40)
description_text.insert(tk.END, "Uygulamayı kullanmak için whatsapp web'i açın. "
                                "Sonra mesaj atmak istediğiniz"
                                " kişiye açın ve uygulamayı çalıştırın ")
description_text.config(state="disabled")  # Kullanıcı tarafından düzenlenemez
description_text.pack(pady=10)

# Button oluşturuluyor
button = tk.Button(root, text="Sinir Et!!!", command=activate_function)
button.pack()

# Exit butonu oluşturuluyor
exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.pack(pady=5)

# Pencereyi başlat
root.mainloop()
