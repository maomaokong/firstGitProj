'''
Created on 29 Apr 2013

@author: t80006407
'''
class Person(object):
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName
        
    def __str__(self):
        return self.firstName + " " + self.lastName
        

        
#p=Person('maomao','baka')
#print p