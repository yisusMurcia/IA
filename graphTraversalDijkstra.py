def getMin(tags, visited):
    min= 9999
    minTag= None
    for tag in tags.keys():
        if tags[tag][0] < min and (tag not in visited):
            minTag= tag
            min= tags[tag] [0]
    return minTag
def recorreGraphs(graphs, start):
    tags= {}
    visited= []
    noVisited= [start]
    tags[start]= [0, '']
    while len(noVisited)> 0: 
        actualNode= getMin(tags, visited)
        visited.append(actualNode)
        for node, weight in graphs[actualNode].items():
            if node not in visited and node not in noVisited:
                noVisited.append(node)
            newWeight= tags[actualNode] [0]+ weight
            if node not in visited:
                if node not in tags:
                    tags[node]=[newWeight, actualNode]
                else:
                    if tags[node] [0]> newWeight:
                        tags[node]= [newWeight, actualNode]
        del noVisited[noVisited.index(actualNode)]
    return tags
graphs={
    '1': {'2': 3, '3': 6},
    '2': {'1': 3, '3': 2, '4':1},
    '3': {'1': 6, '2': 2, '4': 4, '5': 2},
    '4': {'2': 1, '3': 4, '5': 6},
    '5': {'3': 2, '4': 6, '6': 2, '7': 2},
    '6': {'5': 2, '7': 3},
    '7': {'5': 2, '6': 3}
}
print(recorreGraphs(graphs, '1'))