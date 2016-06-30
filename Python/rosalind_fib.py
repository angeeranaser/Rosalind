# Rosalind: Rabbits and Recurrence Relations
#   Given: Positive integers n < 40 and k < 5.
#   Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair 
#           and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit
#           pairs (instead of only 1 pair).

def numberPairs(months, offspring):
    
    # in the first month, only one pair of rabbits is present
    if (months == 1):
        return 1
    # in the second month, only one batch of offspring is produced
    if (months == 2):
        return offspring

    firstGen = numberPairs(months - 1, offspring)
    secondGen = numberPairs(months - 2, offspring)

    if (months <= 4):
        return (firstGen + secondGen)

    return (firstGen + (secondGen * offspring))

def main():

    # open file, extract data
    dataFile = open('rosalind_fib.txt','r')
    rabbits = dataFile.readline().strip()
    rabbits = rabbits.split(' ')
    months = int(rabbits[0])
    offspring = int(rabbits[1])

    # calculate number of rabbit pairs
    result = numberPairs(months, offspring)
    print(result)

if __name__ == "__main__":
    main()
