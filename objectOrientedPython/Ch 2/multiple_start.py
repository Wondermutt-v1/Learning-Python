# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"


class C(A, B):  # the parser will pick class a first in this instance but because the name property is not clear on the inheritance the  compiler will not be consistent
    def __init__(self):
        super().__init__()

    def show_props(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)

c = C()
print(C.__mro__) ## a special class attribute that shows the resolution order
c.show_props()
