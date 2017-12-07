'''
Title: My Turing Language Interpreter
Author: Aditya S. Chanda
'''

class Tape(dict):
    '''
    This tape is comprised of a dictionary of missing keys and entries.
    Since the point of the machine is to have an infinitely long tape,
    this fills in the gaps moving to the right.
    '''
    def __missing__(self,key):
        return 0

def constitute_tape(arg):
    '''
    arg is type string and is supposed to be the entire data string.
    This function takes the data and assigns each value to an entry in
    the dict Tape
    '''
    global tape
    for i in range(len(arg)):
        tape[i] = arg[i]
    return None

def adjust_tape(position):
    '''
    if the position being requested is negative, then it moves
    the entire tape to the right.
    '''
    global tape
    indexer = list(reversed([i+1 for i in range(len(tape))]))
    if position >= 0:
        return None
    elif position < 0:
        for i in range(len(tape)):
            tape[indexer[i]] = tape[indexer[i-1]]
        tape[0] = '0'
    return None

def segmentize(arg):#argument is source
    '''
    The purpose of this function is to turn the source into segments of
    length 5 because each instruction in a Turing machine is of the following
    form:
    <current state, current symbol, next symbol, direction, next state>
    '''
    frame = []
    while True:
        frame = frame+[arg[:5]];arg = arg[5:]
        if arg == '':
            break
    return frame

def find_instruction(state,symbol):
    '''
    Given the current state and symbol (type string) at position,
    this function outputs the corresponding instruction.
    '''
    global command
    candidates,finer_candidate,error = [],None,False
    for i in command:
        if i[0] == state:
            candidates = candidates+[i]
    for i in candidates:
        if i[1] == symbol:
            if finer_candidate == None:
                finer_candidate = i
            else:
                error = True
                return 'Error, duplicated mapping state & symbol. '
    if error != True:
        return finer_candidate

#data_raw = input("Data >> ")
#position,data = int(data_raw[-1:]),list(data_raw[:-1])
#source = input("Source >> ");command = segmentize(source)
#source.sort(key=lambda x: int(x[0]))

'''
Initialize
'''
data_raw = '1231231231231323123'
source = '1 12 101010010100100100001011111010001000101101010101010010010010'
#the format of the source is initial_state initial_position code
split_source = source.split(' ')
state = split_source[0]
position = split_source[1]
instruction_set = split_source[2]
#represent halt with . (period)
command = segmentize(source)

tape = Tape()
constitute_tape(data_raw)

'''
data_raw is data that will be computed upon.
source is the actual program.
'''

while True:
    if state == '.':
        break
    #prepare state of computer further
    current_instruction = find_instruction(state,tape[position])
    next_symbol = current_instruction[2]
    direction = [-1,1][current_instruction[3] == 1]
    next_state = current_instruction[4]
    #update tape and computer state
    tape[position] = next_symbol
    if (position + direction)<0:
        adjust_tape()
        position = 0
    elif (position+direction)>0:
        position = position+direction
    state = next_state
