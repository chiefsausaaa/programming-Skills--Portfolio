# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:52:28 2024

@author: DELL
"""


days = int(input("Please enter book return day: "))
if days == 0:
    print ("No fine")
    
elif days>=1 and days<=5:
    print ("Fine amount: AED", days*3)
    
elif days>=6 and days<=10:
        print ("Fine amount: AED", days*16)
        
elif days>=11 and days<=15:
    print ("Fine amount: AED", days*20)
        
else:
    print ("cooked")
    

