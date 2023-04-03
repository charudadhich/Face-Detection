#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install openv-python


# In[ ]:





# In[ ]:


# imports cv2 module
import cv2
# loading cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# reads the specified image
img = cv2.imread("download (2).jfif")
# converts the RGB image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# detects faces in image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# drawing rectangle for coordinates in faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# shows the image in a window named img
cv2.imshow("img", img)
# to display window until any key is pressed
cv2.waitKey()


# In[ ]:





# In[ ]:




