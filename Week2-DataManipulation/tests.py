#Q1
def cheaplist(pricelist,n):

    def arrsum(list):
        totsum = 0
        for item in list:
            totsum += item
        return totsum

    pricelist = sorted(pricelist)

    return arrsum(pricelist[0:n])

#Q2
def reverselist(list):

    return list[::-1]

#Q3
def removeletters(str,removechars):
    returnstr = ""
    for letter in str:
        if letter not in removechars:
            returnstr += letter
    return returnstr

#Q4
def commonvallist(list):
    frequencydict = {}
    for val in list:
        if val not in frequencydict.keys():
            frequencydict.update({val:1})
        else:
            frequencydict.update({val:frequencydict[val]+1})
    common = []
    for key in frequencydict:
        if len(common.keys()) == 0:
            common = [key,frequencydict[key]]
        else:
            if common[1] > frequencydict[key]:
                common = [key,frequencydict[key]]
    return common

#Q5
def keyvalscomp(dict):
    for key in dict.keys():
        if key in dict.values():
            return "False"
    return "True"

#Q6
def isUnique(arr):
    for index in range(0,len(arr)):
        if arr[index] in arr[0:index]:
            return False
    return True

#Q7

def matrixvecMult(matrix,vec):
    result = [0 for i in range(0,len(vec))]
    for y in range(0,len(matrix)):
        for x in range(0,len(matrix[0])):
            result[y] += matrix[y][x]*vec[x]
    return result

#Q8

def matrixmatrixMult(matrixA,matrixB):
    n = len(matrixA)
    result = [[0 for i in range(0,n)] for i in range(0,n)]
    for y in range(0,n):
        for x in range(0,n):
                for k in range(0,n):
                    result[y][x] += matrixA[y][k]*matrixB[k][x]
    return result

#Q9

def drinkstocks(drinkstock,drinks):
    resultList = []
    for drink in drinks:
        drinkMakeable = True
        for ingredient in drink:
            if ingredient not in drinkstock.keys():
                drinkMakeable = False
                break
            else:
                if drinkstock[ingredient] < 1:
                    drinkMakeable = False
                    break
        if drinkMakeable:
            for ingredient in drink:
                drinkstock[ingredient] -= 1
            resultList.append("Drink made")
        else:
            resultList.append("Drink not made")
    return resultList
        
#Q10
def smallestVal(dict):
    if len(dict.keys()) > 0:
        return sorted(dict.keys())[0]
    else:
        return 0

print(matrixmatrixMult([[1,2],[3,4]],[[1,2],[3,4]]))