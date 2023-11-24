from tree import Node
def searchBestTrip(node, end, visited, limit):
    if limit> 0:
        visited.append(node)
        if node.getData()== end:
            return node
        childCities=[]
        for city in connections[node.getData()]:
            childNode= Node(city)
            if not childNode.inArray(visited):
                childCities.append(childNode)
        node.setChildren(childCities)
        for childNode in node.getChildren():
            if not childNode.inArray(visited):
                connection= searchBestTrip(childNode, end, visited, limit+1)
                if connection!= None:
                    return connection
def solveProblem(start, end):
    visited=[]
    startNode= Node(start)
    for limit in range(0, 100):
        solution= searchBestTrip(startNode, end, visited, limit)
        if solution!= None:
            return solution
connections={
    "Malaga":{"Salamanca", "Madrid", "Barcelona"},
    "Sevilla":{"Santiago", "Madrid"},
    "Granada":{"Valencia"},
    "Valencia":{"Barcelona"},
    "Madrid":{"Salamanca", "Sevilla", "Malaga", "Barcelona", "Santander"},
    "Salamanca":{"Malaga", "Madrid"},
    "Santiago":{"Sevilla", "Santander", "Barcelona"},
    "Santander":{"Santiago", "Madrid"},
    "Zaragoza":{"Barcelona"},
    "Barcelona":{"Zaragoza", "Santiago", "Madrid", "Malaga", "Valencia"}
}
if __name__== "__main__":
    start="Malaga"
    end="Santiago"
    resultNode= solveProblem(start, end)
    if resultNode!= None:
        trip=[]
        while resultNode!= None:
            trip.append(resultNode.getData())
            resultNode= resultNode.getFather()
        print(trip)
    else:
        print("Algo salió mal")