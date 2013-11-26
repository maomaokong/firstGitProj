'''
Created on 29 Apr 2013

@author: t80006407
'''
from com.maomaogong.Person import Person

p=Person('maomao', 'baka')
print p
print ("My first Python code!")
print ("easier than I expected")
print (1+5)

a = 3
b = 4
print ("Variable")
print ("a = " + str(a) + "; b = " + str(b) + "; total = " + str(a * b))
print

print ("Operator")
a = 1
a += 2
print (a)
print

print ("If Statement")
a = 20
if a >= 22:
    print ("if")
elif a >= 21:
    print ("elif")
else:
    print ("else")
print

print ("Function 1")
def someFunction1():
    print ("boo")

someFunction1()
print

print ("Function 2")
def someFunction2(a, b):
    print (a + b)
    
someFunction2(12, 451)
print

'''
print ("Function 3: Local Variable")
def someFunction3():
    aa = 10
    
someFunction3()
print (aa)
print
'''

print ("Function 4: Global Variable")
bb = 10
def someFunction4():
    print (bb)
    
someFunction4()
print

print ("For Loop")
for liI in range(1, 4):
    print liI
    
print

print ("While Loop")
cc = 1
while cc < 10:
    print cc
    cc += 1
    
print

print ("Strings 1")
myString = "Abcaa "
print (type(myString))
print (myString.count("a"))
print (myString.find("c"))
print (myString.lower())
print (myString.upper())
print (myString.replace("a", "z"))
print (myString.strip())

print

print ("String 2")
dd = "string"
print (dd[1:3])
print (dd[:-1])

print

print ("Lists")
sampleList = [1,2,3,4,5,6,7,8]
print (sampleList[1])

print

for a in sampleList:
    print (a)
    
    
print

print ("Tuple")
myTuple = (1,2,3)
print (myTuple)

print

print ("Dictionary")
myExample1 = {
             'someItem':2
             , 'otherItem':20
             }
print (myExample1['otherItem'])

print

myExample2 = {
              'someItem':2
              , 'otherItem':20
              }
myExample2['newItem'] = 400
for a in myExample2:
    print (a, myExample2[a])
    
print

print ("Format Number to String")
print ('The 1st order total comes to %f' % 123.444)
print ('The 2nd order total comes to %.2f' % 123.444)

print 

print ("Format Strings")
a = "abcdefghijklmnopqrstuvwxyz"
print ('%.20s' % a)

print

print ("Exception vs Error")
var1 = '1'
try:
    var1 = var1 + 1 #since var1 is a string, it cannot be added to the number 1
except:
    print (var1, " is not a number") #so we execute this


print

print ("Elegant Error Handling")
var1 = '1'
try:
    var2 = var1 + 1 #since var1 is a string, it cannot be added to the number 1
except:
    var2 = int(var1) + 1
    print var2
    
