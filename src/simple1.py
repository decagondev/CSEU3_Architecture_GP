# let's make a simple data driven machine!!!
class ALU:
    def __init__(self):
        self.operation = None
        self.operandA = None
        self.operandB = None
        self.retval = [0, 0]

    def execute(self, cmd, opa, opb):
        self.operation = cmd
        self.operandA = opa
        self.operandB = opb

        if cmd == "ADD":
            self.add(opa, opb)

        if cmd == "ADD_A":
            self.add(opa, opb)

        if cmd == "ADD_B":
            self.add(opa, opb)

        elif cmd == "SUB":
            self.sub(opa, opb)

        elif cmd == "MUL":
            self.mul(opa, opb)

        elif cmd == "DIV":
            self.div(opa, opb)

        elif cmd == "MOD":
            self.mod(opa, opb)

        return self.retval
    
    def add(self, opa, opb):
        self.retval[0] =  opa + opb
        self.retval[1] = 3

    def sub(self, opa, opb):
        self.retval[0] =  opa - opb
        self.retval[1] = 3


    def mul(self, opa, opb):
        self.retval[0] =  opa * opb
        self.retval[1] = 3

    def div(self, opa, opb):
        self.retval[0] =  opa / opb
        self.retval[1] = 3
    
    def mod(self, opa, opb):
        self.retval[0] =  opa % opb
        self.retval[1] = 3




class CPU:
    def __init__(self):
        self.alu = ALU()
        self.pc = 0
        self.sp = -1
        self.registers = [0] * 8
        self.flags = []
        self.cache = []
        self.running = False

    def fetch(self, opcode, opa = None, opb = None):
        self.__decode__(opcode, opa, opb)

    def __decode__(self, opcode, opa = None, opb = None):
        # print(f"Running Instruction: {opcode}")
        op_size = 0
        if opcode == 0:
            self.halt()

        elif opcode == 1:
            res = self.__execute__("PRINT_TOM")
            op_size = 1

        elif opcode == 2:
            res = self.__execute__("ADD", opa, opb)
            op_size = res[1]
        
        elif opcode == 3:
            res = self.__execute__("ADD_A", self.registers[opa], opb)
            # print(res)
            self.registers[opa] = res[0]
            op_size = res[1]

        elif opcode == 4:
            op_size = self.__execute__("STORE", opa, opb)
        
        elif opcode == 5:
            op_size = self.__execute__("PRINT_REG", opa, opb)

        self.pc += op_size
        

        

    def __execute__(self, command, operandA = None, operandB = None):
        if command == "PRINT_TOM":
            print("TOM")
            return 1
        elif command == "ADD":
            results = self.alu.execute(command, operandA, operandB)
            # print(f"Results = {results}")
            # print(f"{operandA} + {operandB} = {results[0]}")
            return results

        elif command == "ADD_A":
            results = self.alu.execute(command, operandA, operandB)
            # print(f"Results = {results}")
            # print(f"{operandA} + {operandB} = {results[0]}")
            return results

        elif command == "STORE":
            self.registers[operandA] = operandB
            print(f"STORE: {operandB} => REG[{operandA}]")
            return 3

        elif command == "PRINT_REG":
            print(f"REG[{operandA}] => {self.registers[operandA]}")
            return 2



    def run(self):
        print("CPU: is running...")
        self.running = True
    
    def halt(self):
        print("CPU: Halted...")
        self.running = False



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
    def __init__(self):
        self.ram = Memory(256)
        self.cpu = CPU()

    
    def start(self):
        self.cpu.run()
        self.__run__()


    def stop(self):
        self.cpu.halt()

    def __run__(self):
        while self.cpu.running:

            # fetch -> decode -> execute cycle
            pc = self.cpu.pc
            opcode = self.ram.read(pc)
            opa = self.ram.read(pc + 1)
            opb = self.ram.read(pc + 2)
            # print(opa)

            # print(opb)
            self.cpu.fetch(opcode, opa, opb)

if __name__ == '__main__':
    print("running from terminal...")

    # make some instructions
    HALT = 0
    PRINT_TOM = 1
    ADD = 2
    ADD_A = 3
    STORE = 4
    PRINT_REG = 5

    # create a machine object called computer
    computer = Machine()

    # load the ram with some program code
    computer.ram.write(0, PRINT_TOM)
    computer.ram.write(1, STORE)
    computer.ram.write(2, 0)
    computer.ram.write(3, 100)
    computer.ram.write(4, ADD_A)
    computer.ram.write(5, 0)
    computer.ram.write(6, 20)
    computer.ram.write(7, PRINT_REG)
    computer.ram.write(8, 0)
    computer.ram.write(9, 0)
    computer.ram.write(10, 0)
    computer.ram.write(11, 0)
    computer.ram.write(12, 0)
    computer.ram.write(13, 0)
    computer.ram.write(14, 0)



    # start the computer up
    computer.start()