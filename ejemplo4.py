import cv2 as cv
import numpy as np

img = np.ones((300, 300), dtype=np.uint8)*255
""" 
i=y
j=x 
"""
""" superior """
for i in range (20,35 ):
    for j in range(80, 220):
        img[i,j]=50
""" 2 linea """
for i in range (35,50 ):
    for j in range(65, 80):
        img[i,j]=50

for i in range (35,50 ):
    for j in range(220, 235):
        img[i,j]=50

""" 3 linea """
for i in range (50,80 ):
    for j in range(50, 65):
        img[i,j]=50

for i in range (50,80 ):
    for j in range(235, 250):
        img[i,j]=50

""" extremos laterales """
for i in range (80,125 ):
    for j in range(35, 50):
        img[i,j]=50

for i in range (80,125 ):
    for j in range(250, 265):
        img[i,j]=50

""" 4linea """
for i in range (125,155 ):
    for j in range(50, 65):
        img[i,j]=50

for i in range (125,155 ):
    for j in range(235, 250):
        img[i,j]=50

""" 5linea """
for i in range (155,170 ):
    for j in range(65, 95):
        img[i,j]=50

for i in range (155,170 ):
    for j in range(205, 235):
        img[i,j]=50

""" mandibula """
for i in range (170,200 ):
    for j in range(95, 110):
        img[i,j]=50

for i in range (170,200 ):
    for j in range(190, 205):
        img[i,j]=50

for i in range (200,215 ):
    for j in range(110, 190):
        img[i,j]=50

""" Dientes """
for i in range (185,200 ):
    for j in range(160, 175):
        img[i,j]=50

for i in range (185,200 ):
    for j in range(125, 140):
        img[i,j]=50

""" nariz """
for i in range (140,170 ):
    for j in range(140, 160):
        img[i,j]=50

""" ojos """
for i in range (95,125 ):
    for j in range(80, 125):
        img[i,j]=50

for i in range (95,125 ):
    for j in range(175, 220):
        img[i,j]=50

for i in range (125,135 ):
    for j in range(95, 125):
        img[i,j]=50

for i in range (125,135 ):
    for j in range(190, 220):
        img[i,j]=50

""" sombras sgitgit"""
for i in range (50, 155):
    for j in range(65, 80):
        img[i,j]=180
        
for i in range (80, 125):
    for j in range(50, 65):
        img[i,j]=180

for i in range (80, 95):
    for j in range(80, 95):
        img[i,j]=180


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()