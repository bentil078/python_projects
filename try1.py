miles = input("enter milage: ")
for miles in range(10):
    km = miles * 1.609
    print("%d miles --> %3.2f kilometers"%(miles, km))
