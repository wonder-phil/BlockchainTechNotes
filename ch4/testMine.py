import sys
from Block import *

b=Block("empty","genesis block")

difficulty = int(sys.argv[1])
newBlock=b.mine(difficulty)
print("start:"+newBlock.bHash+":end")
