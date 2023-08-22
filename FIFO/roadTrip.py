from tree import Node
def searchSolution(start, final):
    solved= False
    visited=[]
    noVisited=[]
    initialNode= Node(start)
    noVisited.append(initialNode)
    while not solved and len(noVisited)!=0:
        node= noVisited.pop(0)
        visited.append(node)
        if node.getData()== final:
            solved= True
            return node
        else:
            nodeData= node.getData()
            children=[]
            for i in cities[nodeData]:
                child= Node(i)
                children.append(child)
                if not child.inArray(visited) and not child.inArray(noVisited):
                    noVisited.append(child)
            node.setChildren(children)
if __name__== '__main__':
    cities={
        'Malaga':{ 'Salamanca', 'Madrid', 'Barcelona'},
        'Sevilla': {'Santiago', 'Madrid'},
        'Granada': {'Valencia'},
        'Valencia': {'Barcelona'},
        'Madrid':{'Salamanca', 'Sevilla', 'Malaga', 'Barcelona', 'Santander'},
        'Salamanca':{'Malaga', 'Madrid'},
        'Santiago':{'Sevilla', 'Santander', 'Barcelona'},
        'Santander': {'Santiago', 'Madrid'},
        'Zaragoza': {'Barcelona'},
        'Barcelona': {'Zaragoza', 'Santiago', 'Madrid', 'Malaga', 'Valencia'}
    }
    start= 'Zaragoza'
    end= 'Madrid'
    trip=[]
    solution= searchSolution(start, end)
    while solution.getFather()!= None:
        trip.append(solution.getData())
        solution= solution.getFather()
    trip.append(start)
    print(trip)