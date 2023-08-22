class Node:
    def __init__(self, data):
        self.data= data
        self.father= None
        self.children= None
        self.cost= 0
        self.comeFrom= None
    def setChildren(self, children):
        self.children= children
        if self.children!= None:
            for i in self.children:
                i.father= self
    def getChildren(self):
        return self.children
    def setFather(self, father):
        self.father= father
    def getFather(self):
        return self.father
    def setData(self, data):
        self.data= data
    def getData(self):
        return self.data
    def equal(self, node):
        if self.getData()== node.getData():
            return True
        else:
            return False
    def inArray(self, array):
        inTheArray= False
        for i in array:
            if self.equal(i):
                inTheArray= True
        return inTheArray
    def setCost(self, cost):
        self.cost= cost
    def getCost(self):
        return self.cost
    def setComeFrom(self, comeFrom):
        self.comeFrom= comeFrom
    def getComeFrom(self):
        return self.comeFrom