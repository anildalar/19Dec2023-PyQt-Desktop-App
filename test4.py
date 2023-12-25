


# 1. Class Defination
class Parent():
    #1. Property
    
    #2. Consctructor
    def __init__(self):
        print("Hello from parent constructor")
        pass
    
    #.3. Method
    
    def setWindowTitle(self, title):
        print(f""" Title is {title} """)
        pass
    def show(self):
        print(f""" Hello from show method """)
        pass
    pass


class Child(Parent):
    #1. Property
    
    #2. Consctructor
    def __init__(self): # self is a cio (class internal object)
        # co.member
        super().__init__()
        print("Hello from child constructor")
        self.setWindowTitle('Calculotr') # cio call parent method
        self.setupUi()  # cio call child method
        pass
    
    #.3. Method
    def setupUi(self): # camleCase
        print("Hello from setupUi method")
        pass
    
    def anil(self):
        print("Hello from anil method")
        pass
    pass



# 2. Create class object
ceo = Child() # ceo = class external object

ceo.anil() # I can call/invoke any method from external object
ceo.show() # I can call/invoke any method from external object

