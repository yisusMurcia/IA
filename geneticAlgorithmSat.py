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
    for i in range(0, len(gen)-1):
        if gen[i]== solution[i]:
            score+=1
    return score

def evaluatepopulation(population):
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

def combineGen(gen1, gen2):
    index= random.randint(0, len(gen1)-1)
    newGen1= gen1[0: index]
    newGen1.extend(gen2[index:])
    newGen2= gen2[0: index]
    newGen2.extend(gen1[index:])
    return newGen1, newGen2

def evolvePoblation(poblation, solution):
    poblation= sorted(poblation, key= punteateGen, reverse= True)
    #Seleccionar los 2 mejores genes y cruzarlos
    #Select the 2 best genes and combine it
    gen1, gen2= poblation[0], poblation[2]
    new1, new2= combineGen(gen1, gen2)
    poblation.append(new1)
    poblation.append(new2)
    poblation= sorted(poblation, key= punteateGen, reverse= True)
    poblation.pop(len(poblation)-1)
    poblation.pop(len(poblation)-1)

if __name__== "__main__":
    #Esta varieble es requerida para la ejecución de varias funciones
    #This var is neccesary for the execution of many functions
    solution= generatepopulation(1)[0]
    poblation= generatepopulation(5)