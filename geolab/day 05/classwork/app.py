class rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height=height

    def __repr__(self):
        return f'width : {self.width}  height: {self.height}'
    
    def __add__(self,other):  
        new_width = self.width + other.width
        new_height = self.height + other.height 
        new_r = rectangle(new_width,new_height)
        return new_r
# dunder method
    





r1 = rectangle(5,9)
r2 = rectangle(7,11)
r3 = r1 + r2

print(r3)