#Python Program to print all Prime numbers in an Interval
value=1
new=50
for i in range(value,new+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)