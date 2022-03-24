stack = []
sequence = []
pieces_Present = [False, False, False, False, False, False, False, False]
isValid = [False]

def Input():
    sequence = int(input())
    while(sequence > 0):
        stack.append(sequence % 10)
        sequence = sequence // 10

def checktPiecesPresent(sequence):
    for j in range(len(sequence)):
        for i  in range(8):
            if(i+1 == sequence[j]):
                pieces_Present[i] = True

def multipleOccurenceOf1stand2ndPiece(sequence):
    length = len(sequence) - 1
    for i in range(len(sequence)):
        if(i != 0 and i != length):
            if(sequence[i] == 1 or sequence[i] == 2):
                return True
    return False

def multipleOccurenceof8thPiece(sequence, index):
    for i in range(len(sequence)):
        if(i != index and sequence[i] == 8):
            return i
    return 0

def check1standLastPiece(sequence):
    if(sequence[0] == 1 and sequence[len(sequence) -1] == 2 and not multipleOccurenceOf1stand2ndPiece(sequence)):
        isValid[0] = True;
    else:
        isValid[0] = False
    


def check3rdPiece(sequence):
    index = sequence.index(3)
    if(sequence[index+1] == 4):
        isValid[0] = True
    else: 
        isValid[0] = False

def check4thPiece(sequence):
    index = sequence.index(4)
    if(sequence[index-1] == 1):
        isValid[0] = True
    else:
        isValid[0] = False

def check5thPiece(sequence):
    index = sequence.index(5)
    if(sequence[index-1] == 1 and pieces_Present[5]):
        isValid[0] = True
    else:
        isValid[0] = False

def check6thPiece(sequence):
    index = sequence.index(6)
    if(sequence[index + 1] == 2 and pieces_Present[4]):
        isValid[0] = True
    else:
        isValid[0] = False

def check7thPiece(sequence):
    index = sequence.index(7)
    if(sequence[index+1] ==  8 and sequence[index-1] == 8):
        isValid[0] = True
    else:
        isValid[0] = True
    
def check8thPiece(sequence):
    index1 = sequence.index(8)
    index2 = multipleOccurenceof8thPiece(sequence, index1)
    if(index2):
        if(sequence[index1-1] == 5 and sequence[index1+1] == 7 and sequence[index2-1] == 7 and sequence[index2+1] == 6):
            isValid[0] = True
        else:
            isValid[0] = False
    else:
        if(sequence[index1-1] == 5 and sequence[index1+1] == 6):
              isValid[0] = True
        else:
            isValid[0] = False

Input()
i = 0
while(len(stack)):
    sequence.insert(i, stack.pop())
    i += 1

checktPiecesPresent(sequence)
check1standLastPiece(sequence)

#check 3rd piece is in right position 
if(pieces_Present[2] and isValid[0]):
    check3rdPiece(sequence)

# check 4th piece is in right position
if(pieces_Present[3] and isValid[0]):
    check4thPiece(sequence)

# check 5th piece is in right position
if(pieces_Present[4] and isValid[0]):
    check5thPiece(sequence)

# check 6th piece is in right position
if(pieces_Present[5] and isValid[0]):
    check6thPiece(sequence)

# check 7th piece is in right position
if(pieces_Present[6] and isValid[0]):
    check7thPiece(sequence)

# check 8th piece is in righ position
if(pieces_Present[7] and isValid[0]):
    check8thPiece(sequence)

if(isValid[0]):
    print("VALID")
else:
    print("NOT")