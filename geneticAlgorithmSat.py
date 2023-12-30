import random
#Generar la población inicial
#Generate the inital population
def generatepopulation(maxPopulation= 50, varNums=10):
    population= []
    for i in range(0, maxPopulation):
        gen= []
        for j in range(0, varNums):
            boolean= 1
            if random.random()< 0.5:
                boolean= 0
            gen.append(boolean)
        population.append(gen)
    return population

def punteateGen(gen):
    score= 0
    for i in range(0, len(gen)):
        if gen[i]== solution[i]:
            score+=1
    return score

def evaluatePopulation(population):
    score= 0
    #En base a cada individuo, si su puntación es mayor a 4, incrementa la puntación de la población en 1,
    #si es meon a 4, la puntación de la población es menor a 4

    #For each individual, if it score is greathen than 4, the population´s score by 1, else if is less than 4,
    #the population´s score is decreased by 1
    for gen in population:
        genValue= punteateGen(gen)
        if genValue> 4:
            score+= 1
        elif genValue< 4:
            score-= 1
    return score

def selectGen(population):
    total= 0
    for gen in population: 
        total+= punteateGen(gen)
    randomGen= random.randint(0, 100)
    for gen in population:
        total-= punteateGen(gen)
        if randomGen>= total:
            return gen

def combineGen(gen1, gen2):
    index= random.randint(0, len(gen1)-1)
    newGen1= gen1[0: index]
    newGen1.extend(gen2[index:])
    newGen2= gen2[0: index]
    newGen2.extend(gen1[index:])
    return newGen1, newGen2

#Crear funcion de mutación
#Create function for mutation
def mutate(gen, prob= 0.1):
    if (random.random()<= prob):
        index= random.randint(0, len(gen)-1)
        if gen[index]== 0:
            gen[index]= 1
        else:
            gen[index]= 0
    return gen

def evolvePopulation(population, solution, maxPopulation= 50, iterations= 100):
    for i in range(0, iterations):
        #Seleccionar los 2 mejores genes y cruzarlos, no pueden ser el mismo gen
        #Select the 2 best genes and combine it, they can´t be the same gen
        gen1, gen2= selectGen(population), selectGen(population)
        new1, new2= combineGen(gen1, gen2)
        new1= mutate(new2)
        new2= mutate(new2)
        population.append(new1)
        population.append(new2)
        population= sorted(population, key= punteateGen, reverse= True)
        if (len(population)> maxPopulation):
            population.pop(len(population)-1)
            population.pop(len(population)-1)
    return population[0]
if __name__== "__main__":
    #Esta varieble es requerida para la ejecución de varias funciones
    #This var is neccesary for the execution of many functions
    solution= generatepopulation(1)[0]
    population= generatepopulation(10)
    bestGen= evolvePopulation(population, solution)
    print(bestGen)
    print(punteateGen(bestGen))