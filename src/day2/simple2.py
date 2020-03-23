# lets build up our simulator some more
# now we will add the concept of registers
# and an add opcode

# let's make a simple data driven machine!!!
HALT = 1
PRINT_BOB = 2 # TODO: refactor to print name as in for me PRINT_TOM
PRINT_NUM = 3
SAVE = 4
PRINT_REG = 5
ADD = 6

# think of some operations that we might want to perform such as print something, load  or store something etc
# maybe some way to stop execution and some arithmetic operations

# TODO: lets load a program in to memory
def load_memory(filename):
    pass

# lets make a model of memory to hold our program
# TODO: refactor to load in memory from file eg `memory = [0] * 128`
memory = [
    SAVE,
    65,
    2,
    PRINT_REG,
    2,
    HALT,
    PRINT_BOB
]

register = [0] * 8

# think about keeping track where we are currently in mem to fetch the next instruction
pc = 0
# are we actually running
running = True
inc_size = 0

# Main entrypoint
# TODO: grap any args

# TODO: load the memory

# REPL

# lets make a running loop...
while running:
    # extract a command maybe?
    # FETCH
    cmd = memory[pc]

    # lets check what command has been fetched
    # DECODE
    if cmd == HALT:
        # EXECUTE
        running = False
    
    elif cmd == PRINT_BOB:
        # EXECUTE
        print("Bob")
        inc_size = 1

    elif cmd == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        inc_size = 2

    elif cmd == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        inc_size = 3

    elif cmd == PRINT_REG:
        reg = memory[pc + 1]
        print(register[reg])
        inc_size = 2

    # TODO: handle ADD opcode
    
    else:
        print("Invalid Instruction")
        running = False

    # how will we move forward in memory to grab the next command?
    pc += inc_size