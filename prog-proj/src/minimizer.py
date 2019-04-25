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
def getBlankPairs(matrix, states):
    ret = list()

    for i in range(0, len(states)):
        for j in range(0, len(states)):
            if i != j:
                stateOne = states[i]
                stateTwo = states[j]
                if matrix[stateOne][stateTwo] == '':
                    for row in matrix:
                        pass
                        #print(row)
                    pair = (stateOne, stateTwo)
                    ret.append(pair)
                    #print(pair)
    return ret

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
    for row in T:
        print(row)

    #Get all pairs that are blank
    blankPairs = getBlankPairs(T, states)

    #Mark all other distinguishable states
    while(True):
        temp_T = T
        if(temp_T == T):
            break
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
    minimize(states, alphabet, transitions, states[0], accepting)

if __name__ == "__main__":
    main()
