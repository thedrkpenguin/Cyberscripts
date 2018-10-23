import base64

cipher_text = base64.b64encode(b"Secret Message")

print("Encoded text using base64 is: ")
print(cipher_text)


plain_text = base64.b64decode(cipher_text)
print(plain_text)
