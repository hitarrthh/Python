def division(x,y):
    assert y != 0, "CANNOT DIVIDE BY ZERO"
    return x/y
a = float(input("ENTER NUMERATOR"))
b = float(input("ENTER DENOMINATOR"))
ans = division(a,b)
print("DIVISION IS: ",ans)