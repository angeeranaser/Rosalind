from itertools import product

def main():
    dataFile = open('rosalind_lexf.txt','r')
    dataList, n = dataFile.readlines()
    dataList = dataList.strip().replace(' ','')
    dataFile.close()
    n = int(n)

    outputFile = open('output.txt','w')

    result = list(product(dataList,repeat=n))
    for x in range(len(result)):
        result[x] = ''.join(result[x])
        print(result[x])
        outputFile.writelines(result[x] + '\n')
    
    outputFile.close()

if __name__ == '__main__':
    main()