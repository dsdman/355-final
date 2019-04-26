#Written by Dylan Desai for csce355
import sys

#Reads dfa from file
def readDFA(loc):
    #variables for dfa
    accepting = list()
    alphabet = list()
    transitions = list()

    f = open(loc, "r")
    lines = list()

    read = f.readlines()
    for line in read:
        l = line.strip().split("\n")
        lines.append(l)
    accepting = lines[1]
    alphabet = lines[2]
    accepting = accepting[0].split(" ")
    alphabet = alphabet[0].split(": ")

    for j in range(3, len(lines)):
        for i in range(0, len(lines[j])):
            transition = lines[j][i].split(" ")
            transitions.append(transition)
    f.close()
    return accepting, alphabet, transitions

#Returns pairs of states
def getPairs(states):
    ret = list()
    for i in range(0, len(states)):
        for j in range(0, len(states)):
            stateOne = states[i]
            stateTwo = states[j]
            #print(stateOne, end=' ')
            #print(stateTwo)
            if i != j:
                statePair = (stateOne, stateTwo)
                #print(statePair)
                ret.append(statePair)
    return ret

def inFinal(state, final):
    if str(state) in final:
        return True
    else:
        return False

#get states that are blank
def isBlank(matrix, statePair):
    if matrix[statePair[0]][statePair[1]] == '':
        return True
    else:
        return False

#Runs transition function to determine where it goes reading a character
def transitionsTo(alphabet, transition_func, state, char):
    ret = 0

    #Gets corresponding row and column in transition function
    row = state
    column  = alphabet.find(char)

    #Look it up in the function and return it
    ret = transition_func[row][column]
    return ret

#Gets whether or not pair transitions to 'X'
def GoesToX(alphabet, pair, matrix, transition_func):
    p = pair[0]
    q = pair[1]

    for trans in transition_func:
        pass
        #print(trans)
    #print(pair)

    for row in matrix:
        pass
        #print(row)
    for char in alphabet:
        p_trans = transitionsTo(alphabet, transition_func, p, char)
        q_trans = transitionsTo(alphabet, transition_func, q, char)

        #print(char)
        #print(p_trans, end = ' ')
        #print(q_trans)
        
        if matrix[int(p_trans)][int(q_trans)] == 'X':
            return True
        else:
            return False

#minimizes a given dfa
def minimize(states, alphabet, transitions, initial, final):
    T = list()
    pairs = list()

    #initialize a blank 2d array T with size cardinality of states
    for i in range(0, len(states)):
        temp = list()
        for j in range(0, len(states)):
            temp.append('')
        T.append(temp)
    for row in T:
        print(row)

    #get pairs of distinct states
    pairs = getPairs(states)
    print("\n")

    #Mark states distinguished by epsilon
    for pair in pairs:
        p = pair[0]
        q = pair[1]
        if  ( (inFinal(p, final) and (not inFinal(q, final))) or (not inFinal(p, final) and inFinal(q, final))):
            T[p][q] = 'X'
            T[q][p] = 'X'
    print("AFTER EPSILON DISTINCTION")
    for row in T:
        print(row)

    #Mark all other distinguishable states
    while(True):
        temp_T = T

        for pair in pairs:
            #Determine if pair of states are blank
            blank = isBlank(T, pair)
            #Determines if there is a transition from pair to 'X'
            isX = GoesToX(alphabet, pair, T, transitions)
            if blank and isX:
                T[pair[0]][pair[1]] = 'X'
                T[pair[1]][pair[0]] = 'X'

        if(temp_T == T):
            break

    print("AFTER OTHER DISTINCTION")
    for row in T:
        print(row)
def main():
    #Variables for dfa
    accepting = list()
    alphabet = list()
    transitions = list()
    states = list()

    #grab the dfa from description
    accepting, alphabet, transitions = readDFA(sys.argv[1])
    for i in range(0, len(transitions)):
        state = i
        states.append(i)
    
    #minimize it
    minimize(states, alphabet[1], transitions, states[0], accepting)

if __name__ == "__main__":
    main()
