import time
import hashlib
class Block:
    def _init_(self, timestamp, data, prevblockhash, hash_value):
        self.timestamp = timestamp
        self.data = data
        self.prevblockhash = prevblockhash
        self.hash = hash_value
    
    def Sethash(self):
        self.timestamp=str(int(self.timestamp))
        payload = self.timestamp + self.data + self.prevblockhash
        s = hashlib.sha256()
        s.update(payload)
        self.hash = str(s.hexdigest())

def CreateBlock(data, prevblockhash):
	b = Block(time.time(), data, prevblockhash, '')
	b.SetHash()
	return b        

def AddBlock(data){
    prevblock =                                                                 
}