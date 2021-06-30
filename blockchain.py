import hashlib
import os
import json
from time import sleep, time

#Blockchain main class
class BlockChain(object): 
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="HASH", proof = 100)

    #for creating a new block , previous hash is none for genesis block
    def new_block(self,proof,previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) # previous hash or the last calculated hash
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    @property #property() , for last block of this blockchain
    def last_block(self):

        return self.chain[-1]

    #new Transaction
    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1
    
    #hash function
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

#getting Transaction details from the user
def user_intraction():
    sender = input("Sender Username > ")
    receiver = input("Receiver Username > ")
    value = input("Amount (ACOIN) > ") 
    return sender,receiver,value
    

blockchain = BlockChain()

#mining part 
def mining():
    sender, receiver, value = user_intraction()
    t1 = blockchain.new_transaction(sender,receiver,value)

    hash_object = json.dumps(str(sender+receiver+value))
    raw_hash = hash_object.encode()

    proof_of_work = hashlib.sha256(raw_hash)
    hex_hash = proof_of_work.hexdigest()
    blockchain.new_block(hex_hash)
    user_inp = input("Next Tranaction? yes / no > ")
    if user_inp == "yes":
        mining()
    else:
        return 0
#CLI part
print("\tWelcome to Abhi's Crypto Macthine")
sleep(2)
os.system("clear")
mining()



#printing a Block
print("BlockChain:",blockchain.chain)

