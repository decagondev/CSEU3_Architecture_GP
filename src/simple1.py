# let's make a simple data driven machine!!!

class CPU:
    def __init__(self):
        self.pc = 0
        self.sp = -1
        self.registers = []
        self.flags = []
        self.cache = []



class Memory:
    def __init__(self, mem_size):
        self.storage = [0] * mem_size

    def read(self, addr):
        if addr < len(self.storage):
            return self.storage[addr]

    def write(self, addr, value):
        if addr < len(self.storage):
            self.storage[addr] = value

class Machine:
    pass