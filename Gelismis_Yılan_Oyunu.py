import tkinter
import turtle
import time
import random

class YilanOyunu:
    def __init__(self):
        # Ekranı Ayarla
        self.pencere = turtle.Screen()
        self.pencere.title("Gelişmiş Yılan Oyunu")
        self.pencere.bgcolor("powderblue")
        self.pencere.setup(width=600, height=600)
        self.pencere.tracer(0)

        # Puan ve Zaman
        self.puan = 0
        self.sure = 60

        # Puan ve Zaman Yazısı
        self.skor_yazisi = turtle.Turtle()
        self.skor_yazisi.speed(0)
        self.skor_yazisi.color("black")
        self.skor_yazisi.penup()
        self.skor_yazisi.hideturtle()
        self.skor_yazisi.goto(0, 260)
        self.guncelle_skor()

        # Yılanın başı
        self.kafa = turtle.Turtle()
        self.kafa.speed(0)
        self.kafa.shape("square")
        self.kafa.color("green")
        self.kafa.penup()
        self.kafa.goto(0, 0)
        self.kafa.direction = "stop"

        # Yemek
        self.yemek = turtle.Turtle()
        self.yemek.speed(0)
        self.yemek.shape("circle")
        self.yemek.color("red")
        self.yemek.penup()
        self.yemek.goto(0, 100)

        # Gövde listesi
        self.govde = []

        # Klavye kontrolünü başlat
        self.pencere.listen()
        self.pencere.onkey(self.yukari, "Up")
        self.pencere.onkey(self.asagi, "Down")
        self.pencere.onkey(self.sola, "Left")
        self.pencere.onkey(self.saga, "Right")
        self.pencere.onkey(self.cikis, "q")

    def yukari(self):
        if self.kafa.direction != "down":
            self.kafa.direction = "up"

    def asagi(self):
        if self.kafa.direction != "up":
            self.kafa.direction = "down"

    def sola(self):
        if self.kafa.direction != "right":
            self.kafa.direction = "left"

    def saga(self):
        if self.kafa.direction != "left":
            self.kafa.direction = "right"

    def cikis(self):
        self.pencere.bye()

    def hareket(self):
        if self.kafa.direction == "up":
            self.kafa.sety(self.kafa.ycor() + 20)
        if self.kafa.direction == "down":
            self.kafa.sety(self.kafa.ycor() - 20)
        if self.kafa.direction == "left":
            self.kafa.setx(self.kafa.xcor() - 20)
        if self.kafa.direction == "right":
            self.kafa.setx(self.kafa.xcor() + 20)

    def kenar_gecis(self):
        if self.kafa.xcor() > 290:
            self.kafa.setx(-290)
        if self.kafa.xcor() < -290:
            self.kafa.setx(290)
        if self.kafa.ycor() > 290:
            self.kafa.sety(-290)
        if self.kafa.ycor() < -290:
            self.kafa.sety(290)

    def guncelle_skor(self):
        self.skor_yazisi.clear()
        self.skor_yazisi.write(f"Skor: {self.puan} | Süre: {self.sure} sn", align="center", font=("Arial", 16, "normal"))

    def havai_fisek(self, x, y):
        fisek = turtle.Turtle()
        fisek.speed(0)
        fisek.shape("circle")
        fisek.color("yellow")
        fisek.penup()
        fisek.goto(x, y)

        for _ in range(10):
            fisek.shapesize(random.uniform(0.5, 2))
            fisek.color(random.choice(["yellow", "orange", "red"]))
            self.pencere.update()
            time.sleep(0.05)

        fisek.hideturtle()

    def oyun_dongusu(self):
        baslangic_zamani = time.time()
        while True:
            self.pencere.update()
            self.kenar_gecis()

            # Zaman güncellemesi
            gecen_sure = int(time.time() - baslangic_zamani)
            self.sure = max(60 - gecen_sure, 0)
            self.guncelle_skor()

            # Süre bittiğinde oyunu sonlandır
            if self.sure <= 0:
                self.skor_yazisi.goto(0, 0)
                self.skor_yazisi.write("Oyun Bitti!", align="center", font=("Arial", 24, "bold"))
                time.sleep(3)
                self.pencere.bye()
                break

            # Yılan yemeğe çarptı mı?
            if self.kafa.distance(self.yemek) < 20:
                # Puan artır ve güncelle
                self.puan += 1
                self.guncelle_skor()

                # Havai fişek efekti
                self.havai_fisek(self.yemek.xcor(), self.yemek.ycor())

                # Yemek yeni konuma gider
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                self.yemek.goto(x, y)

                # Gövdeye yeni parça eklenir
                yeni_parca = turtle.Turtle()
                yeni_parca.speed(0)
                yeni_parca.shape("square")
                yeni_parca.color("grey")
                yeni_parca.penup()
                self.govde.append(yeni_parca)

            # Gövdeyi takip ettir
            for index in range(len(self.govde) - 1, 0, -1):
                x = self.govde[index - 1].xcor()
                y = self.govde[index - 1].ycor()
                self.govde[index].goto(x, y)

            # Gövdeyi kafaya bağla
            if len(self.govde) > 0:
                x = self.kafa.xcor()
                y = self.kafa.ycor()
                self.govde[0].goto(x, y)

            self.hareket()

            # Kendine çarpma durumu
            for parca in self.govde:
                if parca.distance(self.kafa) < 20:
                    time.sleep(1)
                    self.kafa.goto(0, 0)
                    self.kafa.direction = "stop"

                    # Gövdeyi sıfırla
                    for parca in self.govde:
                        parca.goto(1000, 1000)
                    self.govde.clear()

            time.sleep(0.1)

# Tkinter Penceresi
def baslat_oyun():
    w.destroy()  # Tkinter penceresini kapat
    oyun = YilanOyunu()
    oyun.oyun_dongusu()

w = tkinter.Tk()
w.title("Last Of Snake")
w.geometry("300x200")
w.configure(bg="powderblue")

label = tkinter.Label(w, text="Yılan Oyununa Hoş Geldiniz!", bg="powderblue", fg="black", font=("Arial", 16))
label.pack()

info_label = tkinter.Label(w, text="Çıkmak için 'Q' tuşuna basabilirsiniz.", bg="powderblue", fg="red", font=("Arial", 12))
info_label.pack()

exit_button = tkinter.Button(w, text="Çıkış", command=w.destroy)
exit_button.pack()

game_button = tkinter.Button(w, text="Oyunu Başlat", command=baslat_oyun)
game_button.pack()

w.mainloop()
