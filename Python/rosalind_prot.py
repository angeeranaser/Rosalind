# Rosalind: Translating RNA into Protein
#   Given: An RNA string s corresponding to a strand of mRNA.
#   Result: The protein string encoded by s.

def refTable(first):
    codonList = [('UUU','F'),('CUU','L'),('AUU','I'),('GUU','V'),
    ('UUC','F'),('CUC','L'),('AUC','I'),('GUC','V'),
    ('UUA','L'),('CUA','L'),('AUA','I'),('GUA','V'),
    ('UUG','L'),('CUG','L'),('AUG','M'),('GUG','V'),
    ('UCU','S'),('CCU','P'),('ACU','T'),('GCU','A'),
    ('UCC','S'),('CCC','P'),('ACC','T'),('GCC','A'),
    ('UCA','S'),('CCA','P'),('ACA','T'),('GCA','A'),
    ('UCG','S'),('CCG','P'),('ACG','T'),('GCG','A'),
    ('UAU','Y'),('CAU','H'),('AAU','N'),('GAU','D'),
    ('UAC','Y'),('CAC','H'),('AAC','N'),('GAC','D'),
    ('UAA','Stop'),('CAA','Q'),('AAA','K'),('GAA','E'),
    ('UAG','Stop'),('CAG','Q'),('AAG','K'),('GAG','E'),
    ('UGU','C'),('CGU','R'),('AGU','S'),('GGU','G'),
    ('UGC','C'),('CGC','R'),('AGC','S'),('GGC','G'),
    ('UGA','Stop'),('CGA','R'),('AGA','R'),('GGA','G'),
    ('UGG','W'),('CGG','R'),('AGG','R'),('GGG','G')]

    codonList = dict(codonList)
    return codonList[first]

def main():

    # open file, extract data
    dataFile = open('rosalind_prot.txt','r')
    line = dataFile.read().strip()
    dataFile.close()

    # break RNA into codons
    index = 3
    result = [line[i:i + index] for i in range(0, len(line), index)]
    
    # convert codons into protein string
    proteinString = ''
    for x in range(0,len(result)):
        if refTable(result[x]) != 'Stop':
            proteinString += refTable(result[x])
        else:
            proteinString += "\n"
    print(proteinString)

    # output results
    outputFile = open('output.txt','w')
    outputFile.write(proteinString)
    outputFile.close()

if __name__ == "__main__":
    main()
