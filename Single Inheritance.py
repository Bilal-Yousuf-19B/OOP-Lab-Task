class parent:
    def first(self):
        print("Single Inheritance:")
        
class child(parent):
    def second(self):
        print("This is an example of single inheritance")
        
ob = child()
ob.first()
ob.second()

