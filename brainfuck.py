import sys

# The brainfuck program string
program = ""

# 30 000 cells (brainfuck array)
brainfuckArray = []

# Cursor in the brainfuck program (program)
programCursor = 0

# Cursor in the brainfuck memory array (brainfuckArray)
memCursor = 0

result = ""

def main():
    global program, brainfuckArray, programCursor, result

    file = open(sys.argv[1])
    
    # The input program string
    program = file.read()

    for i in range(30000):
        brainfuckArray.append(0)

    while programCursor < len(program):
        HandleInput()
        programCursor += 1

    print(result)
    file.close()
        
# Handle the current char of the input
def HandleInput():
    global brainfuckArray, memCursor, programCursor, result

    charInput = program[programCursor]

    # Increment current cell
    if (charInput == '+'):
        brainfuckArray[memCursor] += 1
    
    # Decrement current cell
    elif (charInput == '-'):
        brainfuckArray[memCursor] -= 1
    
    # Move Data pointer to next cell
    elif (charInput == '>'):
        memCursor += 1
        if memCursor > 30000:
            memCursor = 30000
    
    # Move Data pointer to previous cell
    elif (charInput == '<'):
        memCursor -= 1
        if memCursor < 0:
            memCursor = 0

    # Print
    elif (charInput == '.'):
        result += chr(brainfuckArray[memCursor])
        
    elif (charInput == ','):
        brainfuckArray[memCursor] = ord(sys.stdin.read(1))
        
    elif (charInput == '['):
        if (brainfuckArray[memCursor] == 0):
            while (program[programCursor] != ']'):
                programCursor += 1
        
    elif (charInput == ']'):
        if (brainfuckArray[memCursor] != 0):
            while (program[programCursor] != '['):
                programCursor -= 1

# Do not disturb this sacred piece of code
if __name__ == "__main__":
    main()
