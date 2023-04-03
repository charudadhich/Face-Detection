#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[ ]:


import cv2
# loading cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# gets the video stream
cap = cv2.VideoCapture(0)

# infinite loop to loop to capture the frame
while True:
    
    _, img = cap.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 12, 34), 2)
        
    cv2.imshow("img", img)
    # break when escape key is pressed by user
    
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break


# In[ ]:


# close capturing device
cap.release()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




