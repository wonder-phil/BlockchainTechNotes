#
#
# 
# > pip3 install rsa
# > python3 key_gen.py 
#
# First generate these keys  
#

import rsa
(pub,sec) = rsa.newkeys(1024)

pub_file = open("public-key.pem","w")
sec_file = open("secret-key.pem","w")

pub_file.write(pub.save_pkcs1().decode('utf-8'))
sec_file.write(sec.save_pkcs1().decode('utf-8'))

pub_file.close()
sec_file.close()
