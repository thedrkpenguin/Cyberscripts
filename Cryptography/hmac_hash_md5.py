#bring in the library for message authentication code
import hmac

#create a key for the md5 algorithm 'salt'
hmac_md5 = hmac.new('mySecretKey')

#open the text file in read only binary mode (rb)
plain_text = open('encrypt_text.txt','rb')

try:
	while True:
		#read each block of the file in 1024 bytes
		block_of_text = plain_text.read(1024)
		if not block_of_text:
			break
		hmac_md5.update(block_of_text)
finally:
	#close the text file
	plain_text.close()

#create the md5 digest using the secret key above
md5_digest = hmac_md5.hexdigest()

#print the  digest or hash
print md5_digest
