from tree import Node
def solve(start, end):
    solved= False
    visited= []
    noVisited= []
    startNode= Node(start)
    noVisited.append(startNode)
    while (not solved) and len(noVisited)!= 0:
        node= noVisited.pop(0)
        visited.append(node)
        if node.getData()== end:
            solved= True
            return node
        else:
            #get childs
            nodeArray= node.getData()
            firstChild= [nodeArray[1], nodeArray[0], nodeArray[2], nodeArray[3]]
            firstNode= Node(firstChild)
            if (not firstNode.inArray(visited)) and (not firstNode.inArray(noVisited)):
                noVisited.append(firstNode)
            secondChild= [nodeArray[0], nodeArray[2], nodeArray[1], nodeArray[3]]
            secondNode= Node(secondChild)
            if (not secondNode.inArray(visited)) and (not secondNode.inArray(noVisited)):
                noVisited.append(secondNode)
            thirdChild= [nodeArray[0], nodeArray[1], nodeArray[3], nodeArray[2]]
            thirdNode= Node(thirdChild)
            if (not thirdNode.inArray(visited)) and (not thirdNode.inArray(noVisited)):
                noVisited.append(thirdNode)
            node.setChildren([firstNode, secondNode, thirdNode])
if __name__== "__main__":
    start= [4, 2, 3, 1]
    solution= [1, 2, 3, 4]
    result= solve(start, solution)
    steps= []
    while result.getFather()!= None:
        steps.append(result.getData())
        result= result.getFather()
    steps.append(start)
    steps.reverse()
    print(steps)