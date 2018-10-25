from Crypto.Cipher import AES

#this will creat the encryption options.  The first entry is the secret key
#the secret key must be 16, 24, or 32 bytes long for AES
#the second option is the AES Mode. Here we are using Cipher Block Chaining
#the third option is the initialization vector.  It must be 16 bytes
#for AES
encrypt_AES = AES.new('mySecretKey12345',AES.MODE_CBC, 'my 16-byte-IV456')

#string to encrypt must be in multiples of 16 bytes
message_to_encrypt = 'Encrypt me1234!!'

ciphertext = encrypt_AES.encrypt(message_to_encrypt)

print "Here is the encrypted text: ", ciphertext


decrypt_AES = AES.new('mySecretKey12345',AES.MODE_CBC, 'my 16-byte-IV456')
message_decrypted = decrypt_AES.decrypt(ciphertext)
print "Here is the decrypted message: ", message_decrypted
