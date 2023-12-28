import random

def generatePoblation(maxPoblation, varNums=10):
    poblation= []
    for i in range(0, maxPoblation):
        gen= []
        for j in range(0, varNums):
            boolean= 1
            if random.random()< 0.5:
                boolean= 0
            gen.append(boolean)
        poblation.append(gen)
    return poblation

def geneticSearch(solution, poblation):
    if(solution== poblation[0]):
        return poblation

if __name__== "__main__":
    solution= generatePoblation(4, 10)