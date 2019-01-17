def raisedtopower(x, y):
    z = x ** y
    print("%d raised to the power %d is %d"%(x,y,z))
    return z



first = int(input("enter the base number: "))
second = int(input("enter the exponential number: "))

raisedtopower(first, second)