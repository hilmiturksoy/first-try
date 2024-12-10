class Kitap:
    def __init__(self, ad, yazar, yayin):
        self.ad = ad
        self.yazar = yazar
        self.yayin = yayin

    def __str__(self):
        return f"{self.ad} - {self.yazar} - {self.yayin}"


class Kutuphane:
    def __init__(self):
        self.kitaplari = []

    def add_book(self, kitap):
        """Kütüphaneye kitap ekler."""
        self.kitaplari.append(kitap)
        print(f"Kitap eklendi: {kitap}")

    def erase_book(self, kitap_adi):
        """Kütüphaneden belirtilen kitabı siler."""
        if not kitap_adi.strip():  # Kitap adı boşsa uyarı ver
            print("Kitap adı boş bırakılamaz. Lütfen tekrar deneyin.")
            return

        for kitap in self.kitaplari:
            if kitap.ad == kitap_adi:  # Kitap adı eşleşiyor mu?
                self.kitaplari.remove(kitap)  # Kitabı sil
                print(f"Kitap silindi: {kitap}")
                return  # İşlem tamamlandı, metodu sonlandır

        print(f"Kitap bulunamadı: {kitap_adi}")  # Eşleşen kitap yoksa uyarı ver

    def listele(self):
        """Kütüphanedeki tüm kitapları listeler."""
        if not self.kitaplari:  # Liste boşsa uyarı ver
            print("Kütüphane boş!")
        else:
            print("Kütüphanedeki Kitaplar:")
            for kitap in self.kitaplari:
                print(kitap)


def ana_program():
    kutuphane = Kutuphane()  # Kütüphane nesnesi oluştur

    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Sil")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":  # Kitap ekleme işlemi
            ad = input("Kitap adı: ")
            yazar = input("Yazar adı: ")
            yayin = input("Yayın yılı: ")
            kitap = Kitap(ad, yazar, yayin)  # Kitap nesnesi oluştur
            kutuphane.add_book(kitap)

        elif secim == "2":  # Kitapları listeleme işlemi
            kutuphane.listele()

        elif secim == "3":  # Kitap silme işlemi
            kitap_adi = input("Silmek istediğiniz kitabın adı: ")
            kutuphane.erase_book(kitap_adi)

        elif secim == "4":  # Çıkış
            print("Programdan çıkılıyor.")
            break

        else:
            print("Geçersiz seçim! Lütfen 1, 2, 3 veya 4'ü seçin.")


# Programı başlat
ana_program()
