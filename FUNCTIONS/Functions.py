# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:50:20 2019

@author: vramach1
"""


#function that uses any number of positional arguments
def avg (first ,*rest):
    result = (first + sum(rest))/(1 + len(rest))
    print(type(result))
    print(type(first))
    print(type(rest))
    #print(type(*rest))
    return result
       
print(avg(1,2,3,4))


#function accepting any number of keyword argumrnts

import html
def make_element(name,value,**attrs):
    keyvals = [' %s = "%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
            name = name,attrs = attr_str,
            value = html.escape(value))
    return element


print(make_element('item','Albatross',size = 'large' ,quantity = 6))

#Writing Functions that only accept Keyword arguments

def recv(maxsize,*,block):
    print('Receives a message')
    pass


#recv(1024,True)      #Type error
recv(1024,block=True)


def minimum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1,2,3,4,-5,clip = 1))

#Attaching Informational Metadata to Function arguments

def add (x:int,y:int) ->int:
    return x+y


print(add(1,2))
print(add('a','bee')) #still works

#Returning Multiple values from a Function

def my_func():
    return 1,2,3

a = my_func()
b,c,d = my_func() #returns a tuple
print (a)
print (c)


#Defining Functions With Default Arguments
_no_value = object() #Creates empty object
def spam(a,b =_no_value):
    if b is _no_value:
        print('no b value supplied')
        
spam(1)
spam(1,2)

#The values assigned as a default are bound only once at the time of function definition

x = 42
def spam1(a,b=x):
    print(a,b)
    
spam1 (1)
x= 34  #has no effect
spam1(2)
        
#Defaults should always be immutable objects

def spam3(a,b=[]) :#default is a list
    print(b)
    return b

x = spam3(1)
x.append(99)
x.append('Yow!')
print(x)
spam3(2) #b list value is updated


#Defining Anonymous or Inline functions
# use lambda where ever single expression is evaluated and returned
add = lambda x,y : x+y
add(3,2)


names = ['David Beazley','Brian Jones','Raymond Hettinger','Ned Batchelder']
# sorted  Syntax : sorted(iterable, key, reverse)
print(sorted(names))
# split str.split(separator, maxsplit)
word = 'geeks, for, geeks, Pawan'
print(word.split(', ', 1)) 
print(word.split(', ', 4)) 
print(word.split()[-1])
print(word.split()[-1].lower())
print(sorted(names,key = lambda name: name.split()[-1].lower()))
print(sorted(names, key = lambda name:name.split()[-1].lower(),reverse =True))
