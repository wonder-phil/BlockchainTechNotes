# BlockchainTechNotes - Gotchas Chapter 7

# From: "The Chains that bind us" by Phillip G Bradford
#  https://github.com/wonder-phil/BlockchainTechNotes
#      by P. G. Bradford
#

## Some common gotchas

0. Ensure you have network access to the RPis
   Ubuntu> ping <Rpi IP address>

1. If remote mining on an RPi does not work using the RPI_1_Mine() function.
   Check that your paramiko Python code can reach your RPi. 
   This can be done using a simple function with paramiko that creates a "hello-world.txt" file on the RPi.
   This file should be created in /home/rpi and it can be verified by SSH-ing into this RPi.
   
   If paramiko reaches your RPi, then ensure Block.py and testMine.py are both in 
   the directory /home/rpi
   
    
2. 
3. 

