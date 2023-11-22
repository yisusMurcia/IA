from tree import Node
def bestTrip(start, end, connections):
    visited= []
    noVisited=[]
    startNode= Node(start)
    noVisited.append(startNode)
    solved= False
    while not solved and len(noVisited)!= 0:
       node= noVisited.pop(0)
       if node.getData()== end:
          solved= True
          return node
       #get child
       children=[]
       for city in connections[node.getData()]:
            childNode= Node(city)
            if not childNode.inArray(visited)and not childNode.inArray(noVisited):
                noVisited.append(childNode)
            children.append(childNode)
       node.setChildren(children)
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
    start= "Malaga"
    end= "Santiago"
    result= bestTrip(start, end, connections)
    steps= []
    while result.getFather()!= None:
        steps.append(result.getData())
        result= result.getFather()
    steps.append(start)
    steps.reverse()
    print(steps)