import random
import math
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
def hillClimbing():
    #Make a random rute
    rute=[]
    for city in coord:
        rute.append(city)
    random.shuffle(rute)
    better= True
    while better:
        better= False
        for i in range(0, len(rute)-1):
            if better:
                break    
            for j in range (0, len(rute)-1):
                if i!= j:
                    city1= rute[i]
                    city2= rute[j]
                    newRute= rute[:]
                    newRute[i]= city2
                    newRute[j]= city1
                    if evaluateRute(newRute)< evaluateRute(rute):
                        rute= newRute
                        better= True
                        break
    return rute
def iterateHillClimbing(times=10):
    rute= hillClimbing()
    for i in range(0, 10):
        newRute= hillClimbing()
        if evaluateRute(newRute)< evaluateRute(rute):
            rute= newRute
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
    bestRute= iterateHillClimbing()
    print(bestRute)
    print(evaluateRute(bestRute))