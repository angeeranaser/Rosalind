# Rosalind: Finding a Spliced Motif
#   Given: Two DNA string in FASTA format.
#   Return: One collection of indices of s in which the symbols of t appear as a subsequence of s.

def main():
    
    # open file, extract data
    dataFile = open('rosalind_sseq.txt','r')
    dnaList = dataFile.read().replace('\n','').split('>')
    dataFile.close()

    dnaSequence = dnaList[1][13:]
    subSequence = dnaList[2][13:]

    # find subsequence within main dna string
    index = 0
    indexString = ''
    for x in range(len(subSequence)):
        result = dnaSequence.find(subSequence[x], index)
        if (result != -1):
            index = result + 1
            result += 1
            x += 1
            indexString += str(result)
            indexString += ' '

    # output results
    outputFile = open('output.txt','w')
    outputFile.writelines(indexString)
    outputFile.close()

if __name__ == "__main__":
    main()