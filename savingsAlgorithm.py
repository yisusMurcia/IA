import math
from operator import itemgetter
def getDistance(coord1, coord2):
    lat1= coord1[0]
    lat2= coord2[0]
    lon1= coord1[1]
    lon2= coord2[1]
    return math.sqrt((lat1-lat2)**2+ (lon1-lon2)**2)
def inRoute(a, routes):
    route= None
    for route in routes:
        if a in route:
           route= a
    return route
def calculateWeight(route):
    weight= 0
    for r in route:
        weight=  weight+ orders[r]
    return weight
def order(x):
    return x[1]
def createRoutes():
    saves={}
    for order1 in coord:
        for order2 in coord:
            if order1!= order2:
                if not (order1, order2) in saves:
                    distStoreOrder1= getDistance(coord[order1], store)
                    distStoreOrder2= getDistance(coord[order2], store)
                    distOrder1Order2= getDistance(coord[order1], coord[order2])
                    saves[order1, order2]= distStoreOrder1+distStoreOrder2-distOrder1Order2
    routes= []
    saves= sorted(saves.items(), key= itemgetter(1), reverse=True)
    for key, value in saves:
        r1= inRoute(key[0], routes)
        r2= inRoute(key[1], routes)
        if r1== None and r2== None:
            if calculateWeight([key[0], key[1]])<= maxWeight:
                routes.append([key[0], key[1]])
        elif r1!=None and r2== None:
            if r1[0]== key[0]:
                if calculateWeight(r1)+ calculateWeight([key[1]])<= maxWeight:
                    routes[routes.index(r1)].insert(0, key[1])
            elif r1[len(r1)-1]== key[0]:
                if calculateWeight(r1)+ calculateWeight([key[1]])<= maxWeight:
                    routes[routes.index(r1)].append(key[1])
        elif r1== None and r2!= None:
            if r2[0]== key[1]:
                if calculateWeight(r2)+ calculateWeight([key[0]])<= maxWeight:
                    routes[routes.index(r2)].insert(0, key[0])
            elif r2[len(r2)-1]== key[1]:
                if calculateWeight(r2)+ calculateWeight([key[0]])<= maxWeight:
                    routes[routes.index(r2)].append(key[0])
        elif r1!=None and r2!=None and r1!= r2:
            if r1[0]== key[0] and r2[len(r2)-1]== key[1]:
                if calculateWeight(r1)+ calculateWeight(r2)<= maxWeight:
                    routes[routes.index(r2)].extend(r1)
                    routes.remove(r1)
            elif r1[len(r1)-1]== key[0] and r2[0]== key[1]:
                if calculateWeight(r1)+ calculateWeight(r2)<= maxWeight:
                    routes[routes.index(r1)].extend(r2)
                    routes.remove(r2)
    return routes
if __name__== "__main__":
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
    orders={
        'Malaga': 10,
        'Sevilla': 13,
        'Granada': 7,
        'Valencia': 11,
        'Madrid': 15,
        'Salamanca': 8,
        'Santiago': 6,
        'Santander': 7,
        'Zaragoza': 8,
        'Barcelona': 14
    }
    store= (40.23, -3.4)
    maxWeight= 40
    routes= createRoutes()
    for r in routes:
        print(routes)