class A():
    #1.Property
    
    #2.Constructor
    def __init__(self):
        print("Hello from A Constructor")
    
    #3 
    pass

class B(A):
    #1.Property
    
    #2.Constructor
    def __init__(self):
        #co.member
        #co.constructor
        co.__init__()
        print("Hello from B Constructor") 
    #3 
    pass


co = B()