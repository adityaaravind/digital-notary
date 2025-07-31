import hashlib
import json
import datetime
import os

BLOCKCHAIN_FILE = "blockchain.json"

class Block:
    def __init__(self, index, timestamp, document_hash, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.document_hash = document_hash
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.document_hash}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "document_hash": self.document_hash,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            index=data["index"],
            timestamp=data["timestamp"],
            document_hash=data["document_hash"],
            previous_hash=data["previous_hash"]
        )

class Blockchain:
    def __init__(self):
        self.chain = self.load_chain()

    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "GENESIS", "0")

    def load_chain(self):
        if not os.path.exists(BLOCKCHAIN_FILE):
            genesis = self.create_genesis_block()
            self.save_chain([genesis.to_dict()])
            return [genesis]
        else:
            with open(BLOCKCHAIN_FILE, "r") as f:
                data = json.load(f)
                return [Block.from_dict(block) for block in data]

    def save_chain(self, chain_dicts):
        with open(BLOCKCHAIN_FILE, "w") as f:
            json.dump(chain_dicts, f, indent=4)

    def add_block(self, document_hash):
        last_block = self.chain[-1]
        new_block = Block(
            index=last_block.index + 1,
            timestamp=str(datetime.datetime.now()),
            document_hash=document_hash,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)
        self.save_chain([block.to_dict() for block in self.chain])
        return new_block

    def verify_document(self, document_hash):
        return any(block.document_hash == document_hash for block in self.chain)

    def get_all_blocks(self):
        return [block.to_dict() for block in self.chain]