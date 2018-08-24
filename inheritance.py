'''
Created on Aug 24, 2018

@author: tomhenricksen
'''

class Parent:
    def __init__(self):
        print("This is the parent class")
    def parentFunc(self):    
        print("This is the parent function")
p = Parent()
p.parentFunc()

class Child(Parent):
    def __init__(self):
        print("This is the child class")
    def childFunc(self):    
        print("This is the child function")
c = Child()
c.childFunc()

class Parent2:
    def __init__(self):
        pass
    def test(self):
        print("Parent")
p2 = Parent2()
p2.test()
class Child2(Parent2):
    def __init__(self):
        pass
    def test(self):
        print("Child")
c2 = Child2()
c2.test()