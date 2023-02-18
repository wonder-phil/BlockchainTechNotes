#
# From https://pycryptodome.readthedocs.io/en/latest/src/examples.html
#
# 
# pip3 install pycryptodome
#
# First Run python3 key_gen.py   
#
import crypto
import sys
sys.modules['Crypto'] = crypto
from Crypto.PublicKey import RSA 

key = RSA.generate(2048)
private_key = key.exportKey()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().exportKey()
file_out = open("public.pem", "wb")
file_out.write(public_key)
file_out.close()
