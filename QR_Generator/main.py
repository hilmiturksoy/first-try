import qrcode

url=input("enter your URL: ")

img = qrcode.make(url)
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
