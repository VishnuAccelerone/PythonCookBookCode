# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:19:14 2019

@author: vramach1
"""
#Terminating a thread
import time
from threading import Thread
class CountDownTask:
    def __init__(self):
        self.running = True
        
    def terminate(self):
        self.running = False
        
    def run(self,n):
        while self.running and n>0:
            print('T-minus',n)
            n -=1
            time.sleep(5)
            
c = CountDownTask()

t = Thread(target = c.run,args =(10,))
t.start()

#c.terminate()
#t.join()