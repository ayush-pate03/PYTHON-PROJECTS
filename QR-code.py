import qrcode

print("===== QR CODE GENERATOR =====")

data = input("Enter text or URL: ")
filename = input("Enter file name: ")

img = qrcode.make(data)

img.save(filename + ".png")

print("QR Code generated successfully!")
print("Saved as:", filename + ".png")