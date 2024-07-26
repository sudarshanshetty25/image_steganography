import cv2
import string

# Define a Caesar cipher function for encryption
def caesar_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char in string.printable:
            char_index = string.printable.index(char)
            encrypted_index = (char_index + key) % len(string.printable)
            encrypted_text += string.printable[encrypted_index]
        else:
            encrypted_text += char  # Leave non-printable characters unchanged
    return encrypted_text

# Define a Caesar cipher function for decryption
def caesar_cipher_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char in string.printable:
            char_index = string.printable.index(char)
            decrypted_index = (char_index - key) % len(string.printable)
            decrypted_text += string.printable[decrypted_index]
        else:
            decrypted_text += char  # Leave non-printable characters unchanged
    return decrypted_text

# Read the input image
x = cv2.imread("C:/Users/shrey/OneDrive/Desktop/open_cv/efootball-2024-game-vj-1920x1080.jpg")
i, j, _ = x.shape
print("Image dimensions:", i, j)

# Input the text to hide
text = input("Enter text to hide: ")

# Encrypt the text using Caesar cipher
key = int(input("Enter the key code for encryption: "))
encrypted_text = caesar_cipher_encrypt(text, key)

# Hide the encrypted text within the image
n, m, z = 0, 0, 0
for char in encrypted_text:
    x[n, m, z] = ord(char)
    m = (m + 1) % j
    if m == 0:
        n = (n + 1) % i
    if n == 0 and m == 0:
        z = (z + 1) % 3

# Save the modified image with the encrypted text
cv2.imwrite("encrypted_img.jpg", x)

# Display a success message
print("Text was successfully hidden in the image and saved as 'encrypted_img.jpg'.")

# Read the modified image
x = cv2.imread("encrypted_img.jpg")

# Initialize variables for decryption
n, m, z = 0, 0, 0
retrieved_text = ""

# Retrieve the hidden text from the image
for _ in range(len(encrypted_text)):
    retrieved_text += chr(x[n, m, z])
    m = (m + 1) % j
    if m == 0:
        n = (n + 1) % i
    if n == 0 and m == 0:
        z = (z + 1) % 3

# Prompt the user to enter the verification key
verification_key = int(input("Enter the verification key code: "))

# Check if the verification key is correct
if verification_key != key:
    print("Verification key is incorrect. Decryption is not allowed.")
else:
    # Decrypt the text using Caesar cipher
    decrypted_text = caesar_cipher_decrypt(retrieved_text, key)
    # Print the decrypted text
    print("Decrypted Text:", decrypted_text)
