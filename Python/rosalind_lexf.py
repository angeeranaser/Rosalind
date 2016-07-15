# Rosalind: Enumerating k-mers Lexicographically
#   Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n < 10).
#   Return:  All strings of length n that can be formed from the alphabet, ordered lexicographically.

from itertools import product

def main():
    
    # open file, read data
    dataFile = open('rosalind_lexf.txt','r')
    dataList, n = dataFile.readlines()
    dataList = dataList.strip().replace(' ','')
    dataFile.close()
    n = int(n)
    
    # open output file
    outputFile = open('output.txt','w')

    # strings formed with product function
    result = list(product(dataList,repeat=n))
    for x in range(len(result)):
        result[x] = ''.join(result[x])
        print(result[x]) # output results
        outputFile.writelines(result[x] + '\n')
    
    outputFile.close()

if __name__ == '__main__':
    main()
