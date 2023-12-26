import math
import random
def getDistance(coord1, coord2):
    lat1= coord1[0]
    lon1= coord1[1]
    lat2= coord2[0]
    lon2= coord2[1]
    return math.sqrt((lat1-lat2)**2+(lon1-lon2)**2)

def evaluateRute(rute):
    total= 0
    for i in range(0, len(rute)-2):
        city1= rute[i]
        city2= rute[i+1]
        total= total+ getDistance(coord[city1], coord[city2])
    total+= getDistance(coord[rute[0]], coord[rute[len(rute)-1]])
    return total

def simulatedAnnealing(rute):
    T= 20
    TMin= 0
    annealingSpeed= 100
    dist= evaluateRute(rute)
    while T> TMin:
        for i in range( 1, annealingSpeed):
            newRute= rute[:]
            i= random.randint(0, len(rute)-1)
            j= random.randint(0, len(rute)-1)
            newRute[j], newRute[i]= newRute[i], newRute[j]
            newDist= evaluateRute(newRute)
            delta= dist- newDist
            if (newDist< dist):
                rute= newRute[:]
                break
            elif random.random()< math.exp(delta/T):
                rute= newRute
                break
        T-= 0.005
    return rute
coord={
    'Malaga': (36.43, -4.24),
    'Sevilla': (37.23, -5.59),
    'Granada': (37.11, -3.35),
    'Valencia': (39.28, -0.22),
    'Madrid': (40.24, -3.41),
    'Salamanca': (40.57, -5.4),
    'Santiago': (42.52, -8.33),
    'Santander': (43.28, -3.48),
    'Zaragoza': (41.39, -0.52),
    'Barcelona': (41.23, 2.11)
}
if __name__== "__main__":
    rute= []
    for city in coord:
        rute.append(city)
    random.shuffle(rute)
    solution= simulatedAnnealing(rute)
    for i in range(0, 10):
        new= simulatedAnnealing(rute)
        if evaluateRute(new)< evaluateRute(rute):
            rute= new
    print(solution)
    print(evaluateRute(solution))