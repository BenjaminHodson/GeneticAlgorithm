import random
import math

#def makeGenes():
 #   genes = "".join([random.choice(["0","1"]) for i in range(32)])
  #  return genes

def makeRandSeq(n=32):
    return "".join([random.choice(['0','1']) for i in range(n)])

def toFloat(genes):
    gn = genes
    num = int(gn, 2) /2**30
    return num

def fitness(genes):
    hab = toFloat(genes)
    return -abs(2-hab*hab)              #Negative absolute to find maximum of the parabola


def breed_pair(seq1, seq2):
    gen = "".join([random.choice(p) for p in zip(seq1, seq2)])
    return gen


seq1 = makeRandSeq()
seq2 = makeRandSeq()





pop = [makeRandSeq() for i in range(100)]
top50 = sorted(pop, key=fitness, reverse = True)[:50]
popCreation = [breed_pair(random.choice(top50), random.choice(top50)) for i in range(100)]

def breedPop(pop, frac = 0.5):
    n = len(pop)
    fitList=sorted(pop,key= fitness, reverse = True)[math.floor(frac*n)]
    return [breed_pair(random.choice(fitList), random.choice(fitList)) for i in range(n)]


print (makeRandSeq())
print(toFloat(makeRandSeq()))
print(fitness(makeRandSeq()))
print(top50)
print(fitness(breed_pair(seq1, seq2)))
