'''
Created on Aug 7, 2018

@author: tomhenricksen
'''
students = ["Bob",12,"Joe",22,"Rachel",33]
print(students)
studentsD = {"Bob":12,"Joe":22,"Rachel":33}
print(studentsD)
studentsD["Rachel"] = 35 
print(studentsD)
print(len(studentsD))
del studentsD["Bob"]
print(studentsD)
print(len(studentsD))
studentsBob = {"Bob":12,"Bob":22,"Bob":33}
print(studentsBob["Bob"])