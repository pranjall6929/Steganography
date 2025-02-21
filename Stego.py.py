import cv2
import os

# Default image path (Modify this path as needed)
default_image_path = ("D:\Steganography\mypic.jpg.jpg")

# Load the image
img = cv2.imread(default_image_path)
if img is None:
    print("Error: Unable to load the image.")
    exit()

# Take user input for the secret message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create dictionaries for ASCII encoding/decoding
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Encrypt message into image
n, m, z = 0, 0, 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

# Save encrypted image
encrypted_image_path = os.path.join(os.path.dirname(default_image_path), "encryptedImage.jpg")
cv2.imwrite(encrypted_image_path, img)
print(f"Encrypted image saved as: {encrypted_image_path}")

# Open the encrypted image (Windows only)
os.system(f'start "" "{encrypted_image_path}"')

# Decryption process
message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("ERROR: Incorrect passcode!")
