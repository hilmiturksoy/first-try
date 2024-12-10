from tkinter import ttk, messagebox
from cryptography.fernet import Fernet
from tkinter import *
from PIL import Image, ImageTk  # Pillow kütüphanesinden gerekli sınıflar

# Anahtar oluştur ve global hale getir
key = Fernet.generate_key()
f = Fernet(key)
cmessage = None  # Şifrelenmiş mesaj için global değişken


def encrypt():
    global cmessage  # Global değişkeni kullan
    message = text_entry.get("1.0", "end-1c")
    token = f.encrypt(message.encode())  # Mesajı şifrele
    cmessage = token  # Şifrelenmiş mesajı kaydet
    text_entry.delete("1.0", "end")  # Giriş alanını temizle

    # Şifrelenmiş mesajı ekranda göster
    output_text.delete("1.0", "end")  # Eski çıktıyı temizle
    output_text.insert("1.0", token.decode())  # Şifrelenmiş mesajı ekle
    print("Şifrelenmiş mesaj:", token)


def decrypt():
    global cmessage  # Global değişkeni kullan
    if cmessage is None:
        messagebox.showerror("Error", "No encrypted message found!")  # Eğer şifrelenmiş mesaj yoksa hata göster
        return
    token2 = f.decrypt(cmessage)  # Şifre çöz
    text_entry.delete("1.0", "end")  # Giriş alanını temizle

    # Şifre çözülmüş mesajı ekranda göster
    output_text.delete("1.0", "end")  # Eski çıktıyı temizle
    output_text.insert("1.0", token2.decode())  # Şifre çözülmüş mesajı ekle
    print("Şifre çözülmüş mesaj:", token2.decode())


# GUI Kurulumu
w = Tk()
w.title("Cryptography")
w.geometry("400x550")  # Daha geniş bir pencere

# Logo eklemek için bir Image widget
try:
    logo_image = Image.open("logo.png")  # Logo dosyasını yükleyin (örn. "logo.png")
    logo_image = logo_image.resize((200, 100))  # Logoyu yeniden boyutlandır
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = Label(w, image=logo)  # Logo için bir Label oluştur
    logo_label.pack(pady=10)  # Logoyu pencerenin üst kısmına yerleştir
except Exception as e:
    print("Logo yüklenemedi:", e)

# Başlık
myLabel = Label(w, text="Cryptography", font=("Arial", 16))
myLabel.pack(pady=10)

# Mesaj giriş alanı
text_entry = Text(w, width=40, height=5)
text_entry.pack(pady=10)

# Şifreleme ve çözme butonları
click_one = Button(w, text="Encrypt", command=encrypt)
click_one.pack(pady=5)

click_two = Button(w, text="Decrypt", command=decrypt)
click_two.pack(pady=5)

# Çıkış butonu
quit_button = Button(w, text="Quit", command=w.destroy)
quit_button.pack(pady=5)

# Çıktı gösterme alanı (kopyalanabilir metin kutusu)
output_label = Label(w, text="Output (Copy-Paste Area):", font=("Arial", 12))
output_label.pack(pady=5)

output_text = Text(w, width=40, height=5, state="normal")  # Kullanıcı kopyalayabilir
output_text.pack(pady=10)

mainloop()
