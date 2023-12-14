#Python Program to find Perfect number between 1 to 1000
start=1
end=1000
perfect=[]
for num in range(start,end):
    sum=0
    for n in range (1,num):
        if(num%n==0):
            sum+=n
    if(sum==num):
        perfect.append(num)
print(perfect)