class ZeroDivision(Exception):
    pass
a = float(input("ENTER VALUE A "))  
b = float(input("ENTER VALUE B "))
c = float(input("ENTER VALUE C "))
d = float(input("ENTER VALUE D "))
try:
    if((b*d) == 0):
        raise ZeroDivision
except:
    print("denominator cannot be zero")
else:
    ans = ((a+d)+(b*c))/(b*d)
    print("RESULT: ",ans)