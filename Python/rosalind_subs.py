# Rosalind: Finding a Motif in DNA
#   Given: Two DNA strings s and t.
#   Return: All locations of t as a substring of s.

def main():
    
    # open file, extract data
    dataFile = open("rosalind_subs.txt","r")
    text = dataFile.readline().strip()
    findString = dataFile.readline().strip()
    dataFile.close()

    # find motif within string, output results
    index = 0
    outputFile = open("output.txt", "w")
    while index < len(text):
        result = text.find(findString, index)
        if result == -1:
            break
        index = index + 1
        nextResult = text.find(findString, index)
        if nextResult != result:
            print(result + 1)
            outputFile.write(str(result + 1) + " ")
    outputFile.close()

if __name__ == "__main__":
    main()