class Parent:
    def func1(self):
        print("This is function 1")
        
class Parent2:
    def func2(self):
        print("This is function 2")
        
class child(Parent, Parent2):
    def func3(self):
        print("This is function 3")
        
ob = child()
ob.func1()
ob.func2()
ob.func3()