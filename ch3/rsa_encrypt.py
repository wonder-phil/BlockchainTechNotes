#
# From https://pycryptodome.readthedocs.io/en/latest/src/examples.html
#
# First run: python3 key_gen.py
#
import crypto
import sys
sys.modules['Crypto'] = crypto

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

data = "Welcome Today is a great day!".encode("utf-8")
file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.importKey(open("public.pem").read())

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(data)

# Encrypt the data with RSA
file_out.write(enc_session_key)
file_out.close()
