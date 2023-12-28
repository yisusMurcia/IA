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

def tabuSearch(rute):
    bestRute= rute
    iterations= 100
    time= 5
    tabu= {}
    mejora= True
    while iterations> 0:
        iterations-= 1
        dist= evaluateRute(bestRute)
        mejora= False
        for i in range(0, len(rute)-1):
            if mejora:
                break
            for j in range(0, len(rute)-1):
                if j!= i:
                    newRute= rute[:]
                    newRute[i], newRute[j]= newRute[j], newRute[i]
                    newDist= evaluateRute(newRute)
                    if (newDist< dist):
                        inTabu= False
                        tabuKey= None
                        for key in tabu:
                            if newRute[j] in key and newRute[i] in key:
                                inTabu= True
                                tabuKey= key
                                break
                        if not inTabu or tabu[tabuKey]==0:
                            rute= newRute
                            bestRute= newRute
                            mejora= True
                            tabu[newRute[j], newRute[i]]= time
            if len(tabu)!= 0:
                for key in tabu:
                    if tabu[key]> 0:
                        tabu[key]-= 1
    return bestRute

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
    solution= tabuSearch(rute)
    print(solution)
    print(evaluateRute(solution))