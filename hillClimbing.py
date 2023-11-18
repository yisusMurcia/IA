import random
import math
def getDistance(coord1, coord2):
    lat1= coord1[0]
    lon1= coord[1]
    lat2= coord2[0]
    lon2= coord2[1]
    return math.sqrt((lat1-lat2)**2+(lon1-lon2)**2)
def evaluateRute(rute):
    total= 0
    for i in range(0, len(rute)-1):
        city1= rute[i]
        city2= rute[i+1]
        total+= getDistance(city1, city2)
    total+= getDistance(rute[0], rute[len(rute)-1])
    return total
def hillClimbing():
    #Make a random rute
    rute=[]
    for city in coord:
        rute.append(city)
    random.shuffle(rute)
coord= {
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