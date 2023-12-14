#Python Program to find prime numbers
def prime(value):
    new=2
    for i in range(new,value):
        if(value%new==0):
            return False
        else:
            new=new+1
    return True

prime_num=prime(8)
print(prime_num)