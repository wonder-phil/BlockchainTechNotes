#
# From https://pycryptodome.readthedocs.io/en/latest/src/examples.html
#
# First run:  python3 key_gen.py  
# Second run: python3 rsa_encrypt.py 
#  
# 

import crypto
import sys
sys.modules['Crypto'] = crypto


from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

file_in = open("encrypted_data.bin", "rb")

private_key = RSA.importKey(open("private.pem").read())
cipher_text = file_in.read()


cipher_rsa = PKCS1_OAEP.new(private_key)
plain_text = cipher_rsa.decrypt(cipher_text)

print(plain_text)


