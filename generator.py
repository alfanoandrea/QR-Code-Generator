import pyqrcode

print("Inserisci il link:")
link = input()
image = pyqrcode.create(link)
print("QR Code generato con successo!")
image.svg("qrcode.svg", scale=8)
