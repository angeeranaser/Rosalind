# Rosalind: Counting Point Mutations
#   Given: Two DNA string s and t of equal length.
#   Result: The Hamming distance d(h)(s,t).

def main():

    # open file, extract data
    dataFile = open('rosalind_hamm.txt','r')
    dna1 = dataFile.readline().strip()
    dna2 = dataFile.readline().strip()
    dataFile.close()

    # compare the two strings, find hamming distance
    hammCount = 0
    for x in range(len(dna1)):
        if (dna1[x] != dna2[x]):
            hammCount += 1

    # output result
    print(hammCount)



if __name__ == "__main__":
    main()