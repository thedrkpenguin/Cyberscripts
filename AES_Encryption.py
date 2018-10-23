from Crypto.Cipher import AES

#IV must be 16 bytes
#AES Key 16,24, or 32 bytes
#Input string must be a multiple of 16 in length

encryption_suite = AES.new("This is a key123", AES.MODE_CBC, "This is an IV123")
cipher_text = encryption_suite.encrypt("secret message12")

print(cipher_text)
