import pyqrcode
import png


image = pyqrcode.create(input("Enter the link: "))
image.png("QR-Code.png", scale = 16)
print("QR-Code generated successfully!")

