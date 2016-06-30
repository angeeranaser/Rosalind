# Rosalind: Enumerating Gene Orders
#   Given: A positive integer n < 7.
#   Result: The total number of permutations of length n, followed by a list of all such permutations (in any order).

import itertools

def converter(input):
    result = " ".join(input)
    return result

def main():

    # open file, extract data
    dataFile = open('rosalind_perm.txt','r')
    n = dataFile.readline().strip()
    n = int(n)
    dataFile.close()

    # find permutations of length n, output results
    index = ''
    for x in range (1,n+1):
        index += str(x)
    listPerm = list(itertools.permutations(index))

    outputFile = open("output.txt", "w")
    outputFile.write(str(len(listPerm)) + "\n") # number of permutations of length n
    for x in range(len(listPerm)):
        result = converter(listPerm[x])
        outputFile.write(result + "\n")
        print(result)
    outputFile.close()

if __name__ == "__main__":
    main()
