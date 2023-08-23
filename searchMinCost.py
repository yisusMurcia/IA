from tree import Node
def compare(x):
    estimateCost= x.getCost()
    notVisit=[x.getData()]
    for type in types.get(x.getComeFrom(), []):
        if type != None:
            bestVal= getMin(values, type, notVisit)
            estimateCost= estimateCost+bestVal[0]
            notVisit.append(bestVal[1])
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
def searchSolution(typeArray, values, start, end):
    solved= False
    noVisited=[]
    visited=[]
    for val in values[start]:
        node= Node(val)
        node.setCost(values[start][val])
        node.setComeFrom(start)
        noVisited.append(node)
    while (not solved) and len(noVisited)!= 0:
        noVisited.sort(key=compare)
        node= noVisited.pop(0)
        visited.append(node)
        if node.getComeFrom()== end:
            solved= True
            return node
        children=[]
        nextType= typeArray[node.getComeFrom()][0]
        if nextType== None:
            break
        for val in values[nextType]:
            childNode= Node(val)
            childNode.setComeFrom(nextType)
            childNode.setCost(node.getCost()+ values[nextType][val])
            children.append(childNode)
            if not childNode.inArray(visited):
                if childNode.inArray(noVisited):
                    for n in noVisited:
                        if childNode.equal(n) and childNode.getCost()< n.getCost():
                            noVisited.remove(n)
                noVisited.append(childNode)
        node.setChildren(children)
if __name__== '__main__':
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
    solution= searchSolution(typeArray, values, start, end)
    totalCost= str(solution.getCost())
    options=[]
    while solution.getFather()!= None:
        options.append(solution.getComeFrom()+ ': '+ solution.getData()+'='+\
         str(values[solution.getComeFrom()][solution.getData()]))
        solution= solution.getFather()
    options.append(solution.getComeFrom()+ ': '+ solution.getData()+'='+\
         str(values[solution.getComeFrom()][solution.getData()]))
    options.reverse()
    print(options)
    print('Total cost: '+ totalCost)