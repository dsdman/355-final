import sys
import fileinput
import operator

def part(self, pattern):
    """ Calculate partial match table: String -> [Int]"""
    ret = [0]
        
    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret
        
def search(self, T, P):
    """ 
    KMP search main algorithm: String -> String -> [Int] 
    Return all the matching position of pattern string P in S
    """
    partial, ret, j = part(self,P), [], 0
        
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = partial[j - 1]
        if T[i] == P[j]: j += 1
        if j == len(P): 
            ret.append(i - (j - 1))
            j = 0
            
    return ret

def getString(loc):
    temp = open(loc, 'r')
    f1 = temp.readlines()
    string = f1[0].strip()
    temp.close()
    return string


def main():
    numberStates = 0
    accepting_states = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #transition_function = dict()
    filename = sys.argv[1]
    s = getString(filename)
    #print(s)
    numberStates = len(s)+1
    #print(numberStates)
    accepting_states = numberStates-1
    prevCol  = 0
    subS = ""

    mything = search("zz", "cacao","cac")
    print(mything)
    #print(s.find("cacc"))
    for state in range(0, accepting_states):
        column = alphabet.find(s[state])
        #print(alphebet[0].find(s[i]))
        if state > 0:
            prevCol = alphabet.find(s[state-1])
            subS = s[0:state]
            print(subS)
            '''print(i-1)
            print(s[i-1])
            print(prevCol)'''
        #if s[state] in subS:
            #print(subS)
            #print(s.find(subS))
        #else:
        #   pass
        for i in range(state, 0, -1):
            num = s.find(s[i:state])
            #print("niqq" + str(i) + "niqq")
            if num == 0:
                pass
                #print(i)
                #print(s[i])
                #print(s[i:state])
        for j in range(0, len(alphabet)):
            #print(subS + alphabet[j])   
            myNum = max(search("zz", s, subS + alphabet[j]))
            if myNum == []:
                print(0, end=" ")
            else:
                for item in myNum:

                print(myNum, end=" ")
            #if j == column:
                #transition_function[i] = column
                #print(state+1, end=" ")
            #elif (j == prevCol):
                #print(state, end=" ")
            #else:
                #transition_function[i] = 0
                #print(0, end=" ")
        print("\n")
        #print("cacao")
    for j in range(0, len(alphabet)):
        print(accepting_states, end=" ")
    #print(len(alphabet))
    #print(transition_function)

if __name__ == "__main__":
    main()

  
