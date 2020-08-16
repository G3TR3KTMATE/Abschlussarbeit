import hashlib
import json
import time

"""Quelle: https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/
Quelle 2: https://developer.ibm.com/technologies/blockchain/tutorials/develop-a-blockchain-application-from-scratch-in-python/
Quelle 3: https://github.com/mohandesosama/tiny_block_chain_python/blob/master/block_chain.py
"""

class Block:

    # Von allen Variablen wird ein Hash berechnet
    # Minimale Veränderung führt zu einer starken Veränderung
    # Sha 256 ist ein typischer Hash-Algorithmus

    def calculateHash(self):
        block_string = json.dumps(
            {"Block": self.block, "Nonce": self.nonce, "Time": self.time, "Geldbetrag": self.geldbetrag,
             "Prevhash": self.prevhash, "Schuldner": self.schuldner, "Gläubiger": self.glaeubiger},
            sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def printHashes(self):
        print("Prevhash", self.prevhash)
        print("Hash", self.hash)

    # Alle Variablen, welche wir in einem Block haben, werden hier bestimmt.

    def __init__(self, block, nonce, time, geldbetrag, schuldner, glaeubiger, prevhash=""):
        self.block = block
        self.nonce = nonce
        self.time = time
        self.geldbetrag = geldbetrag
        self.schuldner = schuldner
        self.glaeubiger = glaeubiger
        self.prevhash = prevhash
        self.hash = self.calculateHash()

    # Hier wird der Output der Variablen im programm erstellt.

    def __str__(self):
        string = "Block: " + str(self.block) + "\n"
        string += "Nonce: " + str(self.nonce) + "\n"
        string += "Zeit: " + str(self.time) + "\n"
        string += "Geldbetrag: " + str(self.geldbetrag) + "\n"
        string += "Schuldner: " + str(self.schuldner) + "\n"
        string += "Gläubiger: " + str(self.glaeubiger) + "\n"
        string += "Prevhash: " + str(self.prevhash) + "\n"
        string += "Hash:       " + str(self.hash) + "\n"

        return string

    # Der errechte Hash wird mit dem Anfang "0000" verglichen.
    # Man kann die Rechenleistung erhöhen durch eine längere Reihenfolge
    # Somit ist es eine Filterung nach dem Hash "0000"
    # Durch erhöhung von Nonce wird der Hash immer anders"
    # Durch Nonce kann man auch direkt sehen, wie viele Veruche der Rechner gebraucht hat.

    def ProofofWork(self):
        checker = None
        while str(checker) != "True":
            self.nonce += 1
            self.hash = self.calculateHash()
            checker = self.hash.startswith("0000")


class BlockChain:

    def LastBlock(self):
        return self.chain[-1]

    # Der Block wird nur erstellt, wenn unserer Proof of Work Algorithmus den richtigen Hash gefunden hat.

    def addBlock(self, newBlock):
        newBlock.prevhash = self.LastBlock().hash
        newBlock.ProofofWork()
        self.chain.append(newBlock)

    def validate_Chain(self):
        for i in range(1, len(self.chain)):
            lastblock = self.chain[i - 1]
            newblock = self.chain[i]

            # Bei einer Veränderung stimmt der Hash im Block nicht mehr mit dem berechneten Hash überein.
            # Es folgt ein Fehler

            if newblock.hash != newblock.calculateHash():
                #                label_for_Blockchain.insert(tk.INSERT, "Invalid Block" + "\n")
                return False

            # Es wird überprüft, ob der Hash mit dem letzten Hash des zukünftigen Blockes übereinstimmt
            # Falls dies nicht der Fall ist, erkennt das Programm ein Fehler in der Blockchain selbst.

            if newblock.prevhash != lastblock.hash:
                #                label_for_Blockchain.insert(tk.INSERT, "Invalid Chain" + "\n")
                return None

            # Falls kein Fehler auftritt, ist die Blockchain valid.
            # False, None und True wird als Output gebraucht
            # Auf der anderen Seite wird anhand dieses Outputs, der Text bestimmt, welcher im Programm vorzufinden ist.

        return True

    def generateGenesisBlock(self):
        return Block(0, 0, "09/07/2020", "Genesis Block", "Genesis Block", "Genesis Block")

    def __init__(self):
        self.chain = [self.generateGenesisBlock(), ]



