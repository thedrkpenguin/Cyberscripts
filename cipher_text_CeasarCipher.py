def main(plain_text, shift):
    cipher_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher_text += chr((ord(char) + shift - 97 ) % 26 + 97)
    return cipher_text

plain_text = "Secret MESSAGE!!!"
shift = 13

print("Plain Text Message is: ", plain_text)
print("Shift Pattern is: ", str(shift))
print("Cipher Text is: ", main(plain_text, shift))
