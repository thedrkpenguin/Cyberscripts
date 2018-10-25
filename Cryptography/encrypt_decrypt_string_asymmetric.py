import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5


key_length = 1024  #setup up the key length, typically this would be a larger number

random_gen_number = Random.new().read  #create a random number to be used with the
     				       #public/private key pairs

#Generate RSA public/private key pairs for communicating parties
keypair_alice = RSA.generate(key_length, random_gen_number)
keypair_bob = RSA.generate(key_length, random_gen_number)

#Export public keys for exchange between communicating parties
pubkey_alice = keypair_alice.publickey()
pubkey_bob = keypair_bob.publickey()

#Plain text messages to send for conversation
message_to_alice = "Hello Alice"
message_to_bob = "Hello Bob"

#Generate digital signatures using the private keys
hash_of_alice_message  = MD5.new(message_to_alice).digest()
hash_of_bob_message = MD5.new(message_to_bob).digest()

signature_of_alice = keypair_alice.sign(hash_of_bob_message, '')
signature_of_bob = keypair_bob.sign(hash_of_alice_message, '')

#encrypt messages using the recipients public key
encrypted_for_alice = pubkey_alice.encrypt(message_to_alice, 32)
encrypted_for_bob = pubkey_bob.encrypt(message_to_bob, 32)

#decrypt messages using their own private key
decrypted_for_alice = keypair_alice.decrypt(encrypted_for_alice)
decrypted_for_bob = keypair_bob.decrypt(encrypted_for_bob)

#validate signatures and output message to the console
hash_decrypted_for_alice = MD5.new(decrypted_for_alice).digest()
hash_decrypted_for_bob = MD5.new(decrypted_for_bob).digest()

if pubkey_alice.verify(hash_decrypted_for_bob, signature_of_alice):
	print "Alice recieved from Bob: " , decrypted_for_alice
	print ""
if pubkey_bob.verify(hash_decrypted_for_alice, signature_of_bob):
	print "Bob recieved from Alice: ", decrypted_for_bob
	print ""


