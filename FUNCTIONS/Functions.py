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