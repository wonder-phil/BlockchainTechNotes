# BlockchainTechNotes - Gotchas Chapter 8

# From: "The Chains that bind us" by Phillip G Bradford
#  https://github.com/wonder-phil/BlockchainTechNotes
#      by P. G. Bradford
#

## Some common gotchas

0. Ensure you have network access to the RPis
   Ubuntu> ping <Rpi IP address>

1. Can't pub/sub on the same RPi?
     Ensure you did the following recently
	 Rpi> sudo apt update 
	 
2. Can't install paho.mqtt on a virtual RPi?  
    Check if there is enough memory on the virtual RPi
	 Rpi>  df -h
	This should be at least 10 GB
	If not, then ensure the IMG or qcow2 file was enlarged by at least 10GB using
	  Ubuntu> qemu-img resize ...
	  and the RPi OS is aware of the larger IMG or qcow2 file using
	  RPi> sudo raspi-config

3. Can't connet to the broker machine
     Check that the broker machine has the /etc/mosquitto/mosquitto.conf updated with 
	 allow_anonymous  true   # this is dangerous
     listener 1883 0.0.0.0   # you can whitelist machines
	  
4. All publish/subscribe clients must use the same broker.  Each machine has a single paho.mqtt broker.

