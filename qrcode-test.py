import qrcode

img = qrcode.make("http://www.google.com/")

img.save("qrcode-test.png")
