def findTheDifference(s:str, t:str):
    sortedS = sorted(s)
    sortedT = sorted(t)

    for i in range(len(sortedS)):
        if sortedS[i] != sortedT[i]:
            return sortedT[i]
    
    return sortedT[len(sortedT) - 1]
    
      

        


print(findTheDifference("","y"))
