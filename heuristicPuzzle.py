from tree import Node
def improvement(fatherNode, childNode):
    #calificated the order of the puzzle in both nodes
    father=0
    child=0
    fatherData= fatherNode.getData()
    childData= childNode.getData()
    for n in range(1, len(fatherData)):
        if fatherData[n]> fatherData[n-1]:
            father= father+ 1
        if childData[n]> childData[n-1]:
            child= child+ 1
    if child>= father:
        return True
    else:
        return False
def solvePuzzle(startNode, solution, visited):
    visited.append(startNode.getData())
    if startNode.getData()== solution:
        return startNode
    else:
        nodeData= startNode.getData()
        firstChild= [nodeData[1], nodeData[0], nodeData[2], nodeData[3]]
        secondChild=[nodeData[0], nodeData[2], nodeData[1], nodeData[3]]
        thirdChild=[nodeData[0], nodeData[1], nodeData[3], nodeData[2]]
        firstChild= Node(firstChild)
        secondChild= Node(secondChild)
        thirdChild= Node(thirdChild)
        startNode.setChildren([firstChild, secondChild, thirdChild])
        for node in startNode.getChildren():
            if not (node.getData() in visited) and improvement(startNode, node):
                solved= solvePuzzle(node, solution, visited)
                if solved!= None:
                    return solved
if __name__== "__main__":
    start= [4, 2, 3, 1]
    solution=[1, 2, 3, 4]
    startNode= Node(start)
    visited=[]
    solved= solvePuzzle(startNode, solution, visited)
    steps=[]
    while solved.getFather()!= None:
        steps.append(solved.getData())
        solved= solved.getFather()
    steps.append(start)
    steps.reverse()
    print("steps:"+ str(steps))