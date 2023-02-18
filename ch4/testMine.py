import sys
from Block import *

b=Block("empty","genesis block")

difficulty = int(sys.argv[1])
newBlock=b.mineBlock(difficulty)
print("start:"+newBlock.bHash+":end")
