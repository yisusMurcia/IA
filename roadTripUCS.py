from tree import Node
def compare(x):
    return x.getCost()
def serachTrip(start, end):
    visited=[]
    noVisited=[]
    startNode= Node(start)
    startNode.setCost(0)
    noVisited.append(startNode)
    solved= False
    while (not solved and len(noVisited)>0):
        #Sort list by cost
        #Ordenar lista por coste
        noVisited.sort(key= compare)
        node= noVisited.pop(0)
        if (node.getData()== end):
            solved= True
            return node
        children= []
        for city in connections[node.getData()]:
            #Add near cities
            #Añadir las ciudades cercanas
            childNode= Node(city)
            childNode.setCost(node.getCost()+ connections[node.getData()][city])
            children.append(childNode)
            if not childNode.inArray(visited):
                #if the cost is less than the cost of the same city in noVisited replace it
                #Si el coste de la ciudad es menor que el que esta en noVidited remplazarlo
                if childNode.inArray(noVisited):
                    for n in noVisited:
                        if childNode.equal(n) and childNode.getCost()< n.getCost():
                            noVisited.remove(n)
                            noVisited.append(childNode)
                else:
                    noVisited.append(childNode)
        node.setChildren(children)
connections={
    "Malaga":{"Madrid": 513, "Barcelona": 125},
    "Sevilla":{"Madrid": 514},
    "Granada":{"Valencia": 491, "Malaga": 125, "Madrid": 423},
    "Valencia":{"Granada": 491, "Madrid": 356, "Zaragoza": 309, "Barcelona": 346},
    "Madrid":{"Salamanca": 203, "Sevilla": 514, "Malaga": 513, "Barcelona": 603, "Santander": 437, "Granada": 423, "Valencia": 356, "Santiago": 599},
    "Salamanca":{"Madrid": 203, "Santiago": 390},
    "Santiago":{"Madrid": 599, "Salamanca": 390},
    "Santander":{"Zaragoza": 394, "Madrid": 437},
    "Zaragoza":{"Barcelona": 296, "Madrid": 313, "Valencia": 309, "Santander": 394},
    "Barcelona":{"Zaragoza": 296, "Madrid": 603, "Malaga": 125, "Valencia": 346}
}
if __name__== "__main__":
    start= "Malaga"
    end= "Santiago"
    solution= serachTrip(start, end)
    print("cost:"+ str(solution.getCost()))
    trip= []
    while solution.getFather()!= None:
        trip.append(solution.getData())
        solution= solution.getFather()
    trip.append(start)
    trip.reverse()
    print(trip)