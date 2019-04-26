#Written by Dylan Desai for csce 355

import sys
import fileinput
import operator

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

    accepting = lines[1][0].split(" ")
    alphabet = lines[2][0].split(": ")

    for j in range(3, len(lines)):
        for i in range(0, len(lines[j])):
            transition = lines[j][i].split(" ")
            transitions.append(transition)
    f.close()
    return accepting, alphabet, transitions

def finalState(alphebet, transition_function, string):
    row = 0
    column = 0
    if string == '':
        finalState = 0
        return finalState
    for letter in string:
        column = alphebet[1].find(letter)
        newrow = transition_function[row][column]
        row = int(newrow)
    return row

def readStrings(loc, accepting, alphabet, transitions):
    f = open(loc, "r")
    temp = open(loc, 'r')
    f1 = temp.readlines()
    Strings = list()

    for l in f1:
        Strings.append(l.strip())

    for string in Strings:
        laststate = finalState(alphabet, transitions, string)
        if ( str(laststate) in accepting):
            print("accept")
        else:
            print("reject")

def main():
    #dfa variables
    accepting = list()
    alphabet = list()
    transitions = list()

    #grab arguments
    dfa_file = sys.argv[1]
    strings_file = sys.argv[2]

    #read the dfa
    accepting, alphabet, transitions = readDFA(dfa_file)

    #read the strings and print to stdout
    readStrings(strings_file, accepting, alphabet, transitions)

if __name__ == "__main__":
    main()
