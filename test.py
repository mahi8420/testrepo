"""class A:
    def __init__(self,x):
        self.x=x
        x=44
a=A(4)
print(a,x)"""

'''class A:
    def __init__(self,i=1):
        self.i=i
        
class B(A):
    def __init__(self,j=2):
        super().__init__()
        self.j=j
    def main():
        b=B()
        print(b.i,b.j)
main()'''
"""
class A:
    def __init__(self,param):
        self.a1=param
        
class B(A):
    def __init__(self,param):
        self.b1=param
obj=B(100)
print("%d %d" % (obj.a1,obj.b1))"""
"""
class A:
    def __init__(self):
        self.calculate(30)
    def calculate(self,i):
        self.i=2*i
        
class B(A):
    def __init__(self):
        super().__init__()
        print("i in class b is", self.i)
    def calculate(self,i):
        self.i=3*i
        
b=B()"""



"""



for i in range(1,6):
    if i%4==0:
        print("X")
    elif i%2==0:
        print("X")
    else:
        print("XXXXX")
""""

def country(*abc):
    if len(abc)==1:
        item=abc[0]
        def f(obj):
            return obj[item]
    else:
        def f(obj):
        return tuple(obj[item] for item in abc)
        return f
selection=[]
selection=coutry(slic(2,None))'AUSTRALIA')

print(selection)





















