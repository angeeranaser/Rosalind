# Rosalind: Complementing a Strand of DNA
#   Given: A DNA string s of length at most 1000 bp.
#   Return: The reverse complement s(c) of s.

def findComplement(letter):
    if letter == 'A':
        complement = 'T'
    if letter == 'T':
        complement = 'A'
    if letter == 'C':
        complement = 'G'
    if letter == 'G':
        complement = 'C'

    return complement

def main():

    # open file, extract data
    dataFile = open('rosalind_revc.txt','r')
    dnaString = dataFile.readline().strip()

    # reverse string
    reversedString = dnaString[::-1]

    # generate complement
    reverseComplement = ''
    for x in range(len(reversedString)):
        comp = findComplement(reversedString[x])
        reverseComplement += comp

    # print result
    print(reverseComplement)

if __name__ == "__main__":
    main()