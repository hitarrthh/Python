class Invalid_Marks(Exception):
    pass
marks = float(input("ENTER MARKS OF STUDENT"))
try:
    if(marks > 100):
        raise Invalid_Marks
except:
    print("MARKS CANNOT BE ABOVE 100")
else:
    print("MARKS OF STUDENT IS: ",marks)