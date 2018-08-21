'''
Created on Aug 21, 2018

@author: tomhenricksen
'''
def HelloWorl():
    print("HelloWorld")

HelloWorl()

def Greeting(name):
    print("Hi " + name + "!")

Greeting("Tom")

def AddTwo(num1,num2):
    sum1 = num1 + num2
    print(sum1)
    
AddTwo(1, 2)

def returnTwo(num1,num2):
    return(num1 + num2)

sum2 = returnTwo(40, 50)
print(sum2)