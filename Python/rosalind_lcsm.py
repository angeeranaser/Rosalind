# Rosalind: Finding a Shared Motif
#   Given: A collection of k (where k < 100) DNA string of length at most 1 kbp each in FASTA format.
#   Return: A longest common substring of the collection.

# long_substr and is_substr functions found at http://stackoverflow.com/questions/2892931/

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


def main():

    # open file, extract data
    dataFile = open('rosalind_lcsm.txt','r')
    dataList = dataFile.read().replace('\n','').split('>')
    dataFile.close()

    # make sure the list has only DNA sequences in it
    dataList = dataList[1:]
    for x in range(len(dataList)):
        dataList[x] = dataList[x][13:]

    # find the longest substring
    longestSubstring = long_substr(dataList)

    # export results
    outputFile = open('output.txt','w')
    outputFile.writelines(longestSubstring)
    outputFile.close()

if __name__ == "__main__":
    main()