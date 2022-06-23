# -*- coding: utf-8 -*-
"""
Created on Sun May 15 16:06:20 2022

@author: baris
"""

import cv2

class Button:
    def __init__(self, pos, width, height,value,button_window):
        
        self.pos = pos 
        self.width = width
        self.height = height
        self. value = value
        self.button_window = button_window
        
    def draw(self):
        cv2.rectangle(self.button_window, self.pos, (self.pos[0]+self.width,self.pos[1]+self.height), (225,225,225), cv2.FILLED)
        cv2.rectangle(self.button_window, self.pos, (self.pos[0]+self.width,self.pos[1]+self.height), (50,50,50), 3)
        cv2.putText(self.button_window, self.value, (self.pos[0]+200, self.pos[1]+60), cv2.FONT_HERSHEY_PLAIN, 2 ,(50,50,50),2 )
    
    def checkClick(self):
            cv2.rectangle(self.button_window, self.pos, (self.pos[0]+self.width,self.pos[1]+self.height), (255,255,255), cv2.FILLED)
            cv2.rectangle(self.button_window, self.pos, (self.pos[0]+self.width,self.pos[1]+self.height), (50,50,50), 3)
            
            cv2.putText(self.button_window, self.value, (self.pos[0]+150, self.pos[1]+75), cv2.FONT_HERSHEY_PLAIN, 5 ,(0,0,0),5 )

            
        
        
    
    
    