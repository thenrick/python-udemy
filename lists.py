'''
Created on Aug 6, 2018

@author: thenricksen
'''
shoppingList = ["apples","oranges","bananas","cheese"]
print(shoppingList)
print(shoppingList[0])
print(shoppingList[0:2])
shoppingList.append("blueberries")
print(shoppingList)
shoppingList[0] = "cherries"
print(shoppingList)
del shoppingList[1]
print(shoppingList)
print(len(shoppingList))
listNum = [1,3,5,7,8,10]
print(max(listNum))
print(min(listNum))