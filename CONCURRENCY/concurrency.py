# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:57:22 2019

@author: vramach1
"""

#starting and stopping threads
#Code to execute an independant thread

import time
def countdown(n):
    while n>0:
        print('T-minus',n)
        n -=1
        time.sleep(5)
        
        
#Create and launch a thread
from threading import Thread
t=Thread(target = countdown,args=(10,))
t.start()

if t.is_alive():
    print("still running")
else:
    print("Completed")
    
    
    
    
    