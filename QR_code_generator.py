import qrcode

# Taking a input from the User (Give the filename in jpg formate)
data = input ("Enter the Text or URL: ").strip()
filename = input("Enter the File nam: ").strip()

# using qrcode library
qr = qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)

# generating qr code image
image = qr.make_image(fill_color = 'black',back_color = 'white')
image.save(filename)

# printing a image
print(f'QR code saved as {filename}')