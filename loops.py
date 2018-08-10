'''
Created on Aug 10, 2018

@author: tomhenricksen
'''
list1 = ["Apples","Oranges","Bananas"]
tup1 = (12,14,15)

for item in list1:
    print(item)

for item in tup1:
    print(item)
    
for i in range(0,10):
    print(i)
    
for i in range(0,10,2):
    print(i)
    
for i in range(0,51,5):
    print(i)
    
for i in range(0,5):
    for j in range(0,3):
        print(i*j)