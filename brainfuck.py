##Information and TODO at the end

##30 000 cells (brainfuck array)
brainfuckArray = []
for i in range(30000):
    brainfuckArray.append(0)
    
##brainfuck pointer
currentPtr = 0

##Handle the current char of the input
def HandleInput(charInput):
    ##Increment current cell
    if charInput == '+':
        brainfuckArray[currentPtr] += 1
    
    ##Decrement current cell
    elif charInput == '-':
        brainfuckArray[currentPtr] -= 1
    
    ##Move Data pointer to next cell
    elif charInput == '>':
        currentPtr += 1
        if currentPtr > 30000:
            currentPtr = 30000
    
    ##Move Data pointer to previous cell
    elif charInput == '<':
        currentPtr -= 1
        if currentPtr < 0:
            currentPtr = 0
    
    ##Print
    elif charInput == '.':
        str(unichr(brainfuckArray[currentPtr])) ##should work by not tested
        
    elif charInput == ',':
        
        
    elif charInput == '[':
        
        
    elif charInput == ']':
        
        
##Read every character of the input file
##Use HandleInput with every character

## TODO
## Read all character from file
## Handle Character:     , [ ]
## Make/Find a brainfuck file to test the program

##brainfuck doc: learnxinyminutes.com/docs/brainfuck/