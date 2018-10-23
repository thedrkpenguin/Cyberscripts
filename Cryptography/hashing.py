import hashlib

print("The message is 'MyMessage'")
a=hashlib.md5()
a.update(b"MyMessage")
a.digest()
print("MD5 Hash")
print(a.hexdigest())

b=hashlib.sha224()
b.update(b"MyMessage")
b.digest
print("SHA224 Hash")
print(b.hexdigest())
