def input_val(func,x):
    return func(x)
def convert(x):
    return x*83
def get_multiplier(factor):
    def multiplier(x):
        return x*factor
    return multiplier
n = int(input("ENTER THE VALUE TO CONVERT:"))
print(input_val(convert,n))
p = int(input("ENTER THE VALUE FOR FACTOR"))
q = int(input("ENTER VALUE FOR MULTIPLIER"))
r = get_multiplier(p)
s = r(q)
print("RESULT:")
print(s)