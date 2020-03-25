import sys
# lets build up our simulator some more
# now we will add the concept of registers
# and an add opcode

# let's make a simple data driven machine!!!
HALT = 1
PRINT_TOM = 2
PRINT_NUM = 3
SAVE = 4
PRINT_REG = 5
ADD = 6
PUSH = 7
POP = 8
CALL = 9 # New for day 4
RET = 10 # New for day 4

# think of some operations that we might want to perform such as print something, load  or store something etc
# maybe some way to stop execution and some arithmetic operations

# TODO: demo the idea of a branch table 
## branch table
# bt = {
#     HALT: op_halt,
#     PRINT_TOM: op_print_tom,
#     PRINT_NUM: op_print_num,
#     SAVE: op_save,
#     PRINT_REG: op_print_reg,
#     ADD: op_add,
#     PUSH: op_push,
#     POP: op_pop,
#     CALL: op_call,
#     RET: op_ret
# }

# lets load a program in to memory
def load_memory(filename):
    try:
        address = 0
        with open(filename) as f:
            for line in f:
                # split line before and after comment symbol
                comment_split = line.split("#")

                # extract our number
                num = comment_split[0].strip() # trim whitespace

                if num == '':
                    continue # ignore blank lines

                # convert our binary string to a number
                val = int(num, 2)

                # store val at address in memory
                memory[address] = val

                address += 1

    except FileNotFoundError:
        print(f"{sys.argv[0]}: {filename} not found")
        sys.exit(2)


# lets make a model of memory to hold our program
memory = [0] * 128

register = [0] * 8

sp = 7


# think about keeping track where we are currently in mem to fetch the next instruction
pc = 0
# are we actually running
running = True
inc_size = 0
# TODO op_pc boolean to use for pc condition (add to each instruction case)

# Main entrypoint
if len(sys.argv) != 2:
    print("usage: simple.py filename", file=sys.stderr)
    sys.exit(1)

load_memory(sys.argv[1])
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
    
    elif cmd == PRINT_TOM:
        # EXECUTE
        print("Tom")
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

    elif cmd == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        inc_size = 3

    elif cmd == PUSH:
        # setup
        reg = memory[pc + 1]
        val = register[reg]

        #PUSH
        register[sp] -= 1
        memory[register[sp]] = val
        
        inc_size = 2

    elif cmd == POP:
        # setup
        reg = memory[pc + 1]
        val = memory[register[sp]]

        # pop
        register[reg] = val
        register[sp] += 1

        inc_size = 2
    
    # TODO add CALL instruction
    elif cmd == CALL:
        pass
    # TODO: add RET instruction
    elif cmd == RET:
        pass

    else:
        print(f"Invalid Instruction: {cmd}")
        running = False

    # how will we move forward in memory to grab the next command?
    # TODO: add a condition for the opcode that interacts directly with the pc
    pc += inc_size


# TODO: demo for Branch Table

# while running:
#     ir = memory[pc]

#     if ir in bt:
#         bt[ir]()
#     else:
#         raise Exception(f"Invalid instruction {hex(ir)} at address {hex(pc)}")

# def op_halt():
#     print("Halted!")
#     sys.exit(-1)

# def op_print_tom():
#     print("tom")
#     pc += 1

# def op_print_num():
#     print("PRINT_NUM")
#     pc +=2

# def op_save():
#     print("SAVE")
#     pc += 2

# def op_print_reg():
#     print("PRINT_REG")
#     pc += 2

# def op_add():
#     print("ADD")
#     pc += 3

# def op_push():
#     print("PUSH")
#     pc += 2

# def op_pop():
#     print("POP")
#     pc += 2

# def op_call():
#     print("CALL")
#     pc += 3

# def op_ret():
#     print("RET")
#     pc -= 3