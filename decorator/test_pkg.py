def testFun():
    temp = [lambda x, i=i: i*x for i in range(4)]
    return temp
    
for everylambda in testFun():
    print(everylambda(2))