from tree import Node
def compare(x):
    return x.getCost()
def searchSolution(connections, start, end):
    solved= False
    visited=[]
    noVisited=[]
    firstNode= Node(start)
    firstNode.setCost(0)
    noVisited.append(firstNode)
    while (not solved) and len(noVisited)!=0:
        noVisited.sort(key=compare)
        node= noVisited.pop(0)
        visited.append(node)
        if node.getData()== end:
            solved=True
            return node
        nodeData= node.getData()
        childrenList=[]
        for cities in connections[nodeData]:
            city= Node(cities)
            cost= connections[nodeData][cities]
            city.setCost(node.getCost()+ cost)
            childrenList.append(city)
            if not city.inArray(visited):
                if city.inArray(noVisited):
                    for nodes in noVisited:
                        if nodes.equal(city) and nodes.getCost()> city.getCost():
                            noVisited.remove(nodes)
                noVisited.append(city)
            node.setChildren(childrenList)
if __name__== '__main__':
    connections={
       'Malaga':{'Granada': 125, 'Madrid':513},
       'Sevilla':{'Madrid': 514},
       'Granada':{'Malaga': 125, 'Madrid': 423, 'Valencia': 513},
       'Valencia':{'Granada': 513, 'Madrid': 356, 'Zaragoza':309, 'Barcelona': 346},
       'Madrid':{'Salamanca': 203, 'Sevilla': 514, 'Malaga': 513, 'Granada': 423, 'Barcelona': 603, 'Santander': 437,\
                 'Valencia': 356, 'Zaragoza': 313, 'Santiago': 599},
        'Salamanca':{'Santiago': 390, 'Madrid': 203},
        'Santiago':{'Salamanca': 390, 'Madrid': 599},
        'Santander':{'Madrid': 437, 'Zaragoza': 394},
        'Zaragoza':{'Barcelona': 296, 'Valencia': 309, 'Madrid': 313},
        'Barcelona':{'Zaragoza': 296, 'Madrid': 603, 'Valencia': 346}
    }
    start= 'Malaga'
    end= 'Santiago'
    solution= searchSolution(connections, start, end)
    cost= solution.getCost()
    trip=[]
    while solution.getFather()!= None:
        trip.append(solution.getData())
        solution= solution.getFather()
    trip.append(start)
    trip.reverse()
    print(trip)
    print('Km:'+ str(cost))