class Node:
    def __init__(self, data):
        self.data= data
        self.children= None
        self.father= None
    def setChildren(self, children):
        self.children= children
        if self.children!= None:
            for child in self.children:
                child.father= self
    def getChildren(self):
        return self.children
    def setFather(self, father):
        self.father= father
    def getFather(self):
        return self.father
    def getData(self):
        return self.data
    def equal(self, node):
        if self.getData()== node.getdata():
            return True
        return False
    def inArray(self, array):
        inTheArray= False
        for element in array:
            if self.equal(element):
                inTheArray= True
        return inTheArray