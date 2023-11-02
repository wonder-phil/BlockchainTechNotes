#
# Encrypt with public key
#
#
# First run: python3 key_gen.py
#


import rsa
(pub,sec) = rsa.newkeys(1024)

pub_file = open("public-key.pem","w")
sec_file = open("secret-key.pem","w")

write(pub_file, pub.export_key('PEM'))
write(sec_file, sec.export_key('PEM'))
close(pub_file)
close(sec_file)

data = "Welcome Today is a great day!".encode("utf-8")
file_out = open("encrypted_data.bin", "wb")

pub_file_handle = open('public-key.pem', 'rb')
pub_key = rsa.PublicKey.load_pkcs1(pub_file_handle.read())
pub_file_handle.close()

cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(data)

# Encrypt the data with RSA
file_out.write(enc_session_key)
file_out.close()
