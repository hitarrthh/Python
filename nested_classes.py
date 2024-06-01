class OuterClass:
    def __init__(self):
        self.outrer_var = "THIS IS FROM OUTER CLASS"
        self.inner_instance  = self.InnerIlass()
    class InnerIlass:
        def __init__(self):
            self.inner_var = "THIS IS FROM INNER CLASS"
        def inner_method(self):
            print("THIS METHOD IS FROM INNER CLASS")

outer_instance = OuterClass()

print(outer_instance.inner_instance.inner_var)

outer_instance.inner_instance.inner_method()