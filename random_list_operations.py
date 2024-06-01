import random
i=1
a=[]
for i in range (1,10) :
    c=random.randint(100,200)
    a.append(c)
    k=a[0]
    j=1
    while j<len(a):
        if a[j]<k:
            k=a[j]
        j=j+1
print("\n smallest value is",k)
print("\n Final list",a)


                                                                                                                                                                                                    