import json
from config import MEMORY_PATH

class MemoryAgent:
    def save(self, data):
        try:
            mem = json.load(open(MEMORY_PATH))
        except:
            mem = []

        mem.append(data)
        json.dump(mem, open(MEMORY_PATH, "w"), indent=2)
