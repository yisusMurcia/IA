from tree import Node
types={
    'typeT': {'typeH', 'typeV', 'typeW'},
    'typeH': {'typeV', 'typeW'},
    'typeV': {'typeW'},
    'typeW': {}
}
values={
    'typeT': {'val1': 20, 'val2': 50, 'val3': 60, 'val4': 100},
    'typeH': {'val1': 30, 'val2': 50, 'val3': 55, 'val4': 80},
    'typeV': {'val1': 20, 'val2': 40, 'val3': 50, 'val4': 60},
    'typeW': {'val1': 40, 'val2': 50, 'val3': 60, 'val4': 70}
}
typeArray= {
    'typeT': ['typeH', 'typeV', 'typeW'],
    'typeH': ['typeV', 'typeW'],
    'typeV': ['typeW'],
    'typeW': {} 
}
start= 'typeT'
end= 'typeW'
noVisited=[]
def compare(x):
    estimateCost= x.getCost()
    notVisit=[x.getData()]
    for type in types.get(x.getComeFrom(), []):
        if type != None:
            bestVal= getMin(values, type, notVisit)
            estimateCost= estimateCost+bestVal[0]
            notVisit.append(bestVal[1])
    print(x.getData()+ str(estimateCost))
    return estimateCost
def getMin(dict, type, notVisit):
    bestVal= None
    min= 101
    for name, val in dict[type].items():
        if name not in notVisit:
            if val< min:
                min= val
                bestVal= name
    return [min, bestVal]
for val in values[start]:
        node= Node(val)
        node.setCost(values[start][val])
        node.setComeFrom(start)
        noVisited.append(node)
noVisited.sort(key=compare)
for node in noVisited:
     print(node.getData()+typeArray[node.getComeFrom()][0])