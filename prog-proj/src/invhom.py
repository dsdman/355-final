#Written by Dylan Desai for CSCE 355

import sys
import fileinput
import operator

def readDFA(path):
    stateNum = list()
    numberState = 0;
    temp = open(path, 'r')
    f = temp.readlines()
    accepting = list()
    tmp = list()
    alphabet = list()
    for line in f:
        l = line.strip().split("\n")
        tmp.append(l)
    stateNum = tmp[0]
    accepting = tmp[1]
    alphabet = tmp[2]
    tranition_function = list()
    accepting = accepting[0].split(" ")
    alphabet = alphabet[0].split(": ")
    for trans in range(3, len(tmp)):
        for index in range(0, len(tmp[trans])):
            temp_split = tmp[trans][index].split(" ")
            tranition_function.append(temp_split)
    temp.close()
    stateNum = stateNum[0].split(" ")
    numberState = int(stateNum[len(stateNum)-1])
    return numberState, accepting, alphabet, tranition_function

def stringRead(path):
    temp = open(path, 'r')
    f = temp.readlines()
    lines = list()
    returnlines = list()
    tmpAlphabet = list()
    for line in f:
        lines.append(line.split("\n"))
    for i in range(2, len(lines)):
        returnlines.append(lines[i])
    tmpAlphabet.append(lines[0])
    alphabet = list()
    for line in tmpAlphabet:
        alphabet.append(line[0].split())
    return returnlines, alphabet

def endState(alphabet, transition_function, string,startstate):
    endstate = 0
    row = startstate
    column = 0
    for line in string:
        for letter in line:
            column = alphabet[1].find(letter)
            newrow = transition_function[row][column]
            row = int(newrow)
    endstate = row
    return endstate


def main():
    #Initialize the stuff
    numberOfStates = 0;
    accepting = list()
    alphabet = list()
    transition_function = list()
    strings = list()
    finalAlphabet = list()

    #Get dfa information
    strings, finalAlphabet = stringRead(sys.argv[2])
    numberOfStates, accepting, alphabet, transition_function = readDFA(sys.argv[1])


    #Build and print the info
    alphabetString = finalAlphabet[0][2]
    acceptStates = accepting[2:]
    acceptString= ''
    for state in acceptStates:
        acceptString += " "
        acceptString += state
    print("Number of states: " + str(numberOfStates))
    print("Accepting states:" + acceptString)
    print("Alphabet: " + str(alphabetString))
    for j in range(0, numberOfStates):
        for string in strings:
            endstate = endState(alphabet, transition_function, string,j)
            print(endstate, end = " ")
        print()    

if __name__ == "__main__":
    main()


