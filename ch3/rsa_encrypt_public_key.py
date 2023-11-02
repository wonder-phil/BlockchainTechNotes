#
# Encrypt with public key
#
#
# First run: python3 key_gen.py
#


import rsa


pub_file = open("public-key.pem","r")
#mystr = pub_file.read()
pub_key = rsa.PrivateKey.load_pkcs1(pub_file)

pub_file.close()


data = "Welcome Today is a great day!".encode("utf-8")
c = rsa.PublicKey.encrypt(data, pub_key)

enc_file_out = open("encrypted_data.bin", "wb")
enc_file_out.write(c)

enc_file_out.close()
