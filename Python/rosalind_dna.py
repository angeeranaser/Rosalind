# Rosalind: Counting DNA Nucleotides
#   Given: A DNA string s of length at most 1000 nt.
#   Return: Four integers (separated by spaces) counting the respective number of times 
#           that the symbols 'A', 'C', 'G', and 'T' occur in s.

def main():
    
    # open file, extract data
    dataFile = open('rosalind_dna.txt','r')
    dnaString = dataFile.readline().strip()

    # initialize variables
    countA = 0
    countC = 0
    countG = 0
    countT = 0

    # count instances of each letter
    for x in range(len(dnaString)):
        if dnaString[x] == 'A':
            countA += 1
        if dnaString[x] == 'C':
            countC += 1
        if dnaString[x] == 'G':
            countG += 1
        if dnaString[x] == 'T':
            countT += 1

    # print result
    print(countA, countC, countG, countT)
    

if __name__ == "__main__":
    main()
