import qrcode

# the Url that opens when the QR Code is scanned
image = qrcode.make('https://127.0.0.1:8000')
image.save('qr.png')