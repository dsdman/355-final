#Written by Dylan Desai for CSCE 355

import sys
import fileinput
import operator

def getString(loc):
    temp = open(loc, 'r')
    f1 = temp.readlines()
    string = f1[0].strip()
    temp.close()
    return string


def main():
    #Get all the info to initialize a dfa
    numberStates = 0
    accepting_states = 0
    alphebet = ['abcdefghijklmnopqrstuvwxyz']
    transition_function = list()


    filename = sys.argv[1]
    s = getString(filename)
    numberStates = len(s)+1
    accepting_states = len(s)

    print(s)
    print(numberStates)
    #initialize transition matrix with all zeros
    for i in range(0, numberStates):
        zeros = list()
        for j in range(0, len(alphebet[0])):
            zeros.append(0)
        transition_function.append(zeros)

    for transition in transition_function:
        print(transition)

    #Makes the transition function matrix
    for i in range(0, accepting_states):
        print("fuck me in the asshole")
    #print(transition_function)
    #for i in range(0, accepting_states):
    #    column = alphebet[0].find(s[i])
    #    print(alphebet[0].find(s[i]))
    #
    #    for j in range(0, len(alphebet)):
    #        if j == column:
    #            transition_function.append(i).append(column)
    #        else:
    #            transition_function.append(0)
    #print(transition_function)

if __name__ == "__main__":
    main()
