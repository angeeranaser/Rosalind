# Rosalind: Transcribing DNA into RNA
#   Given: A DNA string t having length at most 1000 nt.
#   Return: The transcribed RNA string of t.

def main():

    # open file, extract data
    dataFile = open('rosalind_rna.txt','r')
    dnaString = dataFile.readline().strip()

    # convert DNA into RNA
    rnaString = dnaString.replace('T','U')

    # print result
    print(rnaString)


if __name__ == "__main__":
    main()
