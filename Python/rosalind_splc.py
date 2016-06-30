# Rosalind: RNA Splicing
#   Given: A DNA string s and a collection of substrings acting as introns.
#   Result: A protein string transcribed from the exons.

def removeIntron(dna, intron):
    dna = dna.replace(intron,'')
    return dna

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
    dataFile = open('rosalind_splc.txt','r')
    dnaList = dataFile.read().strip()
    dnaList = dnaList.replace('\n','').split('>')
    dataFile.close()

    # remove introns from dna
    dnaString = dnaList[1][13:]
    for x in range(2, len(dnaList)):
        dnaString = removeIntron(dnaString, dnaList[x][13:])

    # transcribe dna into rna
    rnaString = dnaString.replace('T','U')

    # break string into codons
    rnaString = [rnaString[i:i + 3] for i in range(0, len(rnaString), 3)]
    proteinString = ''
    for x in range(len(rnaString)):
        proteinLetter = refTable(rnaString[x])
        if proteinLetter != 'Stop':
            proteinString += proteinLetter
        else:
            proteinString += '\n'

    # output results
    outputFile = open('output.txt','w')
    outputFile.writelines(proteinString)
    outputFile.close()
    
if __name__ == "__main__":
    main()