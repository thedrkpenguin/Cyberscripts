#bring in the libraries needed.  hashlib is required for sha256
import hmac
import hashlib

#create secret key for the hash algorithm 'salt'
hmac_sha256 = hmac.new('mySecretKey','',hashlib.sha256)

#open the file in read only binary mode (rb)
plain_text = open('encrypt_text.txt','rb')

try:
	while True:
		#read the file in 1024 byte blocks
		block_of_text = plain_text.read(1024)
		if not block_of_text:
			break
		hmac_sha256.update(block_of_text)
finally:
	#close the file
	plain_text.close()

#create the sha256 digest
sha256_digest = hmac_sha256.hexdigest()

#print the digest or hash
print sha256_digest
