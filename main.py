# -*- coding: utf-8 -*-
"""
Created on Mon May  9 21:18:57 2022

@author: baris
"""

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from button import Button


def normalizasyon(img):
    img = img /255.0
    return img


#load module
model = load_model('model.h5')

# #FOTOĞRAF ÜZERİNDEN SINIFLANDIRMA YAPMA
# img = cv2.imread("dataset/0/700.jpg")
# img = np.asarray_chkfinite(img)
# img = cv2.resize(img , (200,200))
# img = normalizasyon(img)
# img = img.reshape(1,200,200,3)
# predictions = model.predict(img)
# sonuc = np.argmax(predictions)

# if sonuc == 0:
#     print("iki goz kapali")
# elif sonuc ==1:
#     print("sag goz kapali")
# elif sonuc == 2:
#     print("sol goz kapali")
# elif sonuc == 3:
#     print("gozler acik")


#BUTTON OPERATİON
button_window = cv2.imread("background.jpg")
button_window = cv2.resize(button_window,(500,500))

values = ["1.Option","2.Option","3.Option","4.Option"]

buttonList = []
for x in range(4):
    ypos = x * 100 
    buttonList.append(Button((0,ypos),500,100,values[x],button_window))

counter = 0

myEquation = "1.Option"


#WEBCAM 
cap = cv2.VideoCapture(0)
cap.set(3,400)# genişlik ve yükseklik ayarları kameranın
cap.set(4,400)



while True:
    success,frame = cap.read()
    frame = cv2.flip(frame , 1)
    
    img = np.asarray(frame) # frame'i bir array'e çeviriyoruz
    img= cv2.resize(img, (200,200))
    img = normalizasyon(img)
        
    img = img.reshape(1,200,200,3)
        
    #predict
    predictions = model.predict(img)
    classIndex = np.argmax(predictions) # vektör içindeki en büyük değerin index'ini verir yani classı vericek
    predict_value = " "
    
    
    
    if classIndex == 0:
        predict_value = "iki goz kapali"
    elif classIndex ==1:
        predict_value ="sag goz kapali"
    elif classIndex == 2:
        predict_value = "sol goz kapali"
    else:
        predict_value = "gozler acik"
        
    probVal = np.amax(predictions) # array içindeki en büyük değeri verir (tahmin yüzdesi)
    print(classIndex, probVal)
        
    
    #Draw Buttons
    for button in buttonList:
        button.draw()
    cv2.rectangle(button_window, (0,400), (0+500, 400+100), (225,225,225), cv2.FILLED)
    cv2.rectangle(button_window, (0,400), (0+500, 400+100), (50,50,50), 3)
      
    
    #Check for Eye closed
    buttonList[counter].checkClick()
    
    if probVal > 0.7:
        cv2.putText(frame, str(predict_value)+ "   "+ str(probVal), (50,50), cv2.FONT_HERSHEY_DUPLEX, 1,(0,255,0),1)
        if classIndex == 1:
            if counter < 3:
                counter +=1
                buttonList[counter].checkClick()
            elif counter == 3 or counter > 3:
                counter = 3
                buttonList[counter].checkClick()
        elif classIndex == 2:
            if counter > 0:
                counter -=1
                buttonList[counter].checkClick()
            elif counter == 0 or counter < 0:
                counter = 0
                buttonList[counter].checkClick()
        elif classIndex == 0:
            myEquation = values[counter]
        elif classIndex== 3:
            pass
            
    #Display equaliton
    cv2.putText(button_window, myEquation, (15, 400+50), cv2.FONT_HERSHEY_PLAIN, 3 ,(50,50,50),3 )
    
    
     
    #show button window
    cv2.imshow("BUTTON", button_window)
    
    #show webcam window
    cv2.imshow("Classification", frame)
    
    if cv2.waitKey(1) & 0xFF== ord("q"): break
        
cap.release()
cv2.destroyAllWindows()
    
