from tree import Node
def solvePuzzle(node, end, visited:list):
    visited.append(node)
    #retornar el resultado
    if node.getData()== end:
        return node
    #Obtener hijos del nodo para una busqueda recursiva-
    nodeArray= node.getData()
    firstChild= [nodeArray[1], nodeArray[0], nodeArray[2], nodeArray[3]]
    firstNode= Node(firstChild)
    secondChild= [nodeArray[0], nodeArray[2], nodeArray[1], nodeArray[3]]
    secondNode= Node(secondChild)
    thirdChild= [nodeArray[0], nodeArray[1], nodeArray[3], nodeArray[2]]
    thirdNode= Node(thirdChild)
    node.setChildren([firstNode, secondNode, thirdNode])
    for child in node.getChildren():
        if not child.inArray(visited):
            #Hacer una busqueda recursiva si el nodo no esta visitado
            sol= solvePuzzle(child, end, visited)
            if sol!= None:
                return sol
    #Si no se llega a la solución, el código retorna None
    return None
if __name__== "__main__":
    start= [4, 2, 3, 1]
    solution= [1, 2, 3, 4]
    visited=[]
    #Crear el nodo inicial
    startNode= Node(start)
    result= solvePuzzle(startNode, solution, visited)
    #Añadir los pasos y mostrarlos en la pantalla
    steps= []
    while result.getFather()!= None:
        steps.append(result.getData())
        result= result.getFather()
    steps.append(start)
    steps.reverse()
    print(steps)