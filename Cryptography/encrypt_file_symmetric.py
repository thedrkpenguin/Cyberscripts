#bringing in libraries neccessary for program
import os
import random
import struct
from Crypto.Cipher import AES

#create a function to encrypt a text file
def encrypt_file(key, plaintextFile,filesize,chunk_size = 64 * 1024):

	#create a random initialization vector for encryption process
	#it will pick a random number betwwen 0 and 256 and repeat this process
	#16 times
	init_vector = ''.join(chr(random.randint(0, 256)) for i in range(16))

	#this will set the AES encryption mode using the key entered by
	#the user, CBC mode, and the initialization vector created above
	encrypt_mode = AES.new(key, AES.MODE_CBC, init_vector)

	#we are going to write data to teh ciphpertxt file
	#using the pack method the Q means unsigned long long and the
	#< means write using little-endian
	#the initialization vector will also be written to the file
	ciphertextFile.write(struct.pack('<Q', filesize))
	ciphertextFile.write(init_vector)

	#here we create a while loop to write the encrypted data
	#to the ciphertext file
	while True:
		#first we need to write pieces of the file at a
		#time. Larger chunks could be faster, but they must
		#be divisible by 16, hence using the % (modulus) function
		#if the length of the chunk is not divisible by 16
		#padding of spaces will be added
		chunk = plaintextFile.read(chunk_size)
		if len(chunk) == 0:
			break
		elif len(chunk) % 16 != 0:
			chunk += " " * (16 - len(chunk) % 16)
		ciphertextFile.write(encrypt_mode.encrypt(chunk))

#create a function to decrypt a text file
def decrypt_file(key, ciphertext, chunk_size = 24 * 1024):
	#need to get the original size of the encrypted file.
	original_size_of_file = struct.unpack('<Q', ciphertext.read(struct.calcsize\
		('Q')))[0]

	#we know that we added a 16-byte initialization vector to the file
	#here we are going to strip off that information.
	init_vector = ciphertext.read(16)

	#here we are creating our decryption mode utilizing the same key and
	#initialization vector as was used during the encryption.  Then reading each
	#chunk of the file to get the original data
	decryption_mode = AES.new(key, AES.MODE_CBC, init_vector)
	while True:
		chunk = ciphertext.read(chunk_size)
		if len(chunk) == 0:
			break
		original_file.write(decryption_mode.decrypt(chunk))

	#this will make sure the file gets back to the original size before
	#the encryption process
	original_file.truncate(original_size_of_file)

#this will prompt the user to enter the secret key and filename
#for use in this program
secret_key = raw_input("Enter a 16-byte secret key: ")
file_2_encrypt = raw_input("Enter the name of the file to encrypt: ")

#this is used to get the size of the file.  this is needed to ensure
#the proper chunks can be calculated
filesize = os.path.getsize(file_2_encrypt)

#open the files for binary reading and writing
plaintextFile = open(file_2_encrypt, 'rb')
ciphertextFile = open('ciphertext.enc','wb')

#call the encrypt file function and pass the key,file to be encrypted, and
#size of the file
encrypt_file(secret_key, plaintextFile,filesize)

#close the files after finished writing to them
plaintextFile.close()
ciphertextFile.close()


## need an original file to write to
original_file = open('plaintext.txt','wb')

## need to open ciphertext file as well
ciphertextFile = open('ciphertext.enc', 'rb')

#call the decrypt function and pass the key and file to be decrypted.
decrypt_file(secret_key, ciphertextFile)

