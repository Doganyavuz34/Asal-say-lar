# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:16:30 2024

@author: Fujitsu
"""
import math
class AsalSayilar2:
    def AsalSayiBul(a, b):
        for i in range(a, b):
            y = True
            for j in range(2, int(math.sqrt(i))+1):
                if(i % j == 0):
                    y = False
                    break
            if y:
                print(i)
                

class AsalSayilar3:
    def AsalSayiBul(a, b):
        for i in range(a, b):
            y = True
            for j in range(2, int(math.sqrt(i))+1):
                if(i % j == 0):
                    y = False
                    break
            if y:
                print(i)