# BlockchainTechNotes - Gotchas Chapter 7

# From: "The Chains that bind us" by Phillip G Bradford
#  https://github.com/wonder-phil/BlockchainTechNotes
#      by P. G. Bradford
#

## Some common gotchas

1. If remote mining on an RPi does not work using the RPI_1_Mine() function.
   Check that your paramiko Python code can reach your RPi. 
   This can be done using a simple function with paramiko that creates a `hello-world.txt' file on the RPi.
   
   If paramiko reaches your RPi, then ensure Block.py and testMine.py are both in 
   the correct directory /home/rpi
   
    
2. 
3. 

