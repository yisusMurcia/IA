from tree import Node
def searchSolution(start, solution):
    solved= False
    visited=[]
    noVisited=[]
    initialNode= Node(start)
    noVisited.append(initialNode)
    while not solved and len(noVisited)!=0:
        node= noVisited.pop(0)
        visited.append(node)
        if node.getData()== solution:
            solved= True
            return node
        else:
            items= node.getData()
            firstChild= [items[1], items[0], items[2], items[3]]
            firstChild= Node(firstChild)
            if not firstChild.inArray(visited) and not firstChild.inArray(noVisited):
                noVisited.append(firstChild)
            secondChild= [items[0], items[2], items[1], items[3]]
            secondChild= Node(secondChild)
            if not secondChild.inArray(visited) and not secondChild.inArray(noVisited):
                noVisited.append(secondChild)
            thirdChild= [items[0], items[1], items[3], items[2]]
            thirdChild= Node(thirdChild)
            if not thirdChild.inArray(visited) and not thirdChild.inArray(noVisited):
                noVisited.append(thirdChild)
            node.setChildren([firstChild, secondChild, thirdChild])
if __name__== '__main__':
    solution= [1, 3, 2, 4]
    puzzle= [4,3,2,1]
    steps=[]
    solve= searchSolution(puzzle, solution)
    while solve.getFather()!= None:
        steps.append(solve.getData())
        solve= solve.getFather()
    steps.append(puzzle)
    steps.reverse()
    print(steps)