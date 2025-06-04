#Q1

def sum(articles):
    total = 0
    for article in articles.keys():
        total += articles[article]
    return total

def sumtest(func):
    inputs = [({"Apple":5, "Tomato":9,"Bread":18},),
              ({"Honey":5},),
              ({"Soda":2,"Cookies":27},),
              ({},)]
    test(inputs,sum,func)

#Q2

def distance(pos1,pos2):
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    dz = pos1[2] - pos2[2]
    return (dx**2 + dy**2 + dz**2)**(1/2)

def distancetest(func):
    inputs = [((1,2,3),(0,0,0)),
              ((0,0,0),(0,0,0)),
              ((9,2,3),(6,2,3)),
              ((10,9,2),(-10,-1,-2)),
              ((-1,-3,-1),(-1,-1,-2))]
    test(inputs,distance,func)

#Q3

def price(name,originalprice,discount):
    price = originalprice*(1-(discount/100))
    price = round(price,2)

    return f"{name} : {price}"

def pricetest(func):
    inputs = [("Tomato",15,80),
              ("Beer",20,40),
              ("Cough syrup",10,20),
              ("Pasta",100,0),
              ("Expired meat",0,100)]
    test(inputs,price,func)

#Q4

def measurementProcessing(measurementList):
    resultList = []
    for measurement in measurementList:
        if measurement > 10:
            resultList.append(True)
        else:
            resultList.append(False)
    return resultList

def listtest(func):
    inputs = [([25.17, 40.79, 57.82, 75.87, 96.51, 28.88, 60.91],),
    ([7.71, 50.35, 25.19, 67.81, 21.67, 69.76, 60.18],),
    ([12.97, 87.34, 2.49],),
    ([2.66, 81.33, 11.62, 53.97, 36.62, 79.71, 88.01, 61.55, 47.22],),
    ([30.3, 8.59, 14.73, 77.9, 18.28, 97.94],),
    ([65.94, 55.44, 90.66, 74.82, 70.94, 62.9, 15.26, 59.41, 98.83, 30.17, 55.77, 42.06],),
    ([10.27, 67.37, 83.9, 17.5, 71.06, 12.84, 6.84],),
    ([14.99, 30.6, 36.6, 98.24, 94.36, 6.99, 73.8, 19.33, 45.77, 61.58, 38.62],),
    ([18.96, 33.76, 52.99, 48.32],),
    ([66.33, 11.02, 43.91, 57.96, 40.49, 98.44, 60.85, 78.01, 25.6, 84.36],),
    ([85.15, 91.24, 3.77, 11.36, 66.17, 13.47, 36.58, 99.27, 84.17],),
    ([22.6, 81.4, 84.3],),
    ([8.01, 28.72, 16.97, 88.17, 96.65, 5.46, 47.58],),
    ([64.62, 36.03, 77.5, 70.62, 79.65, 31.18, 3.94, 67.77, 43.97, 5.03, 91.53, 85.99],),
    ([83.04, 49.55, 17.11, 34.46, 13.02, 31.38, 85.87],),
    ([],)]
    test(inputs,measurementProcessing,func)

#Q5

def fibbinaci(n):
    nums = [0,1]
    while n > 1:
        n -= 1
        nums = [nums[1], nums[0] + nums[1]]
    if n == 0:
        return 0
    else:
        return nums[1]

def fibtest(func):
    inputs = [(2,),
              (0,),
              (1,),
              (10,),
              (20,)]
    test(inputs,fibbinaci,func)


def test(inputs, evalfunc, testfunc):
    for input in inputs:
        if evalfunc(*input) != testfunc(*input):
            print(f"With inputs {input}, {evalfunc(*input)} is expected. Got {testfunc(*input)} instead.")
            return
    print("Passed all tests")
    return