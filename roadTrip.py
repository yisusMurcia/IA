from math import cos, sin, acos
from tree import Node
def getGeodeticDistance(lat1, lon1, lat2, lon2):
    length= lon1- lon2
    value= (sin(lat1*0.01745329)*sin(lat2*0.01745329))+(cos(lat1*0.01745329)*cos(lat2*0.01745329)*cos(length*0.01745329))
    return(acos(value)*57.29577951)*111.32
def compare(x):
    lat1= coord[x.getData()][0]
    lon1= coord[x.getData()][1]
    lat2= coord[end][0]
    lon2= coord[end][1]
    dist= int(getGeodeticDistance(lat1, lon1, lat2, lon2))
    return (x.getCost()+dist)
def searchSolution(start, end):
    visited=[]
    noVisited=[]
    solved= False
    startNode= Node(start)
    noVisited.append(startNode)
    while (not solved) and len(noVisited)!= 0:
        noVisited.sort(key= compare)
        node= noVisited.pop(0)
        visited.append(node)
        if node.getData()== end:
            solved= True
            return node
        nodeData= node.getData()
        children=[]
        for city in cities[nodeData]:
            childNode= Node(city)
            cost= cities[nodeData][city]
            childNode.setCost(node.getCost()+ cost)
            children.append(childNode)
            if not childNode.inArray(visited):
                if childNode.inArray(noVisited):
                    for n in noVisited:
                        if childNode.equal(n) and n.getCost()> childNode.getCost():
                            noVisited.remove(n)
                noVisited.append(childNode)
        node.setChildren(children)
if __name__== '__main__':
    cities= {
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
    end= 'Santiago'
    start= 'Malaga'
    solution= searchSolution(start, end)
    steps=[]
    print(solution.getCost())
    while solution.getFather()!= None:
        steps.append(solution.getData())
        solution= solution.getFather()
    steps.append(start)
    steps.reverse()
    print(steps)