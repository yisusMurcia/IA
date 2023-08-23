def verifyConditions(variableArray):
    var1= variableArray[0]
    var2= variableArray[1]
    condition1= 7*var1+ 4*var2<=150
    condition2= 6*var1+ 5*var2<=160
    if condition1 and condition2:
        return True
    return False
def evalueSolution(variableArray):
    var1= variableArray[0]
    var2= variableArray[1]
    value= 6*var1+ 4*var2
    return value
def backtrackingSearch(values, parameters, bestSolution, valueIndex):
    valueIndex= (valueIndex)
    min= parameters[valueIndex][0]
    max= parameters[valueIndex][1]
    for n in range(min, max):
        values[valueIndex]=n
        #verify first num
        if valueIndex< len(values)-1:
            if verifyConditions(values):
                bestSolution= backtrackingSearch(values[:], parameters, bestSolution, valueIndex+1)
        else:
            solution= evalueSolution(values)
            if solution> evalueSolution(bestSolution)  and verifyConditions(values):
                bestSolution= [values[0], values[1]]
    return bestSolution
values= [0,0]
parameters=[(0, 51), (0,76)]
bestSolution=[0,0]
solution= backtrackingSearch(values[:], parameters, bestSolution, 0)
print(str(solution)+ " with a value of: "+ str(evalueSolution(solution)))
