from tree import Node
def bestTrip(start, end):
    visited= []
    noVisited=[]
    startNode= Node(start)
    noVisited.append(startNode)
    solved= False
    while not solved and len(noVisited)!= 0:
       node= noVisited.pop(0)
       if node.getData()== end:
          solved= True
          return node
       
conections={
    "Malaga":{"Salamanca", "Madrid", "Barcelona"},
    "Sevilla":{"Santiago", "Madrid"},
    "Granada":{"Valencia"},
    "Valencia":{"Barcelona"},
    "Madrid":{"Salamanca", "Sevilla", "Malaga", "Barcelona", "Santander"},
    "Salamanca":{"Malaga", "Madrid"},
    "Santiago":{"Sevilla", "Santander", "Barcelona"},
    "Santander":{"Santiago", "Madrid"},
    "Zaragoza":{"Barcelona"},
    "Barcelona":{"Zaragoza", "Santiago", "Madrid", "Malaga", "Valencia"}
}
if __name__== "__main__":
 result= conections