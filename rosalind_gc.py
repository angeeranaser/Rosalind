# Rosalind: Computing GC Content
#   Given: At most 10 DNA strings in FASTA format.
#   Return: The ID of the string with the highest GC content, followed by the GC content of that string.

def gcContent(string):
    gcCount = 0
    for x in range(len(string)):
        if (string[x] == 'C' or string[x] == 'G'):
            gcCount += 1
    gcPercent = float(gcCount / len(string))
    return gcPercent

def main():

    # open file, extract data
    dataFile = open('rosalind_gc.txt','r')
    dataList = dataFile.read().strip()
    dataList = dataList.replace('\n','').split('>')

    # find GC contents of strings
    gcList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(1, len(dataList)):
        gcList[x - 1] = gcContent(dataList[x][13:])

    # find string with max GC content
    maxGC = max(gcList)
    maxIndex = int(gcList.index(maxGC))
    maxString = dataList[maxIndex][:13]
    results = [maxString, '\n', str(maxGC)]

    # output results
    outputFile = open('output.txt','w')
    outputFile.writelines(results)
    outputFile.close()

if __name__ == "__main__":
    main()