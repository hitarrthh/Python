def mean(a):
    n = len(a)
    avg = sum(a)/n
    print("MEAN: ",avg)
set = []
x = int(input("ENTER TOTAL NUMBER OF ELEMENTS"))
for i in range(0,x):
    num = int(input())
    set.append(num)
mean(set)