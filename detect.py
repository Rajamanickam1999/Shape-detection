''' Importing computer vision and glob modules '''
import numpy as np
import cv2
import sys
import glob
#File name -->  To get the images in the particular folder
filename='images'
for imgs in glob.glob(filename+'/*.*'):
    # img variable to read the image 
    img = cv2.imread(imgs)
    ''' Since grey scale images are easy to draw contours  ''' 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',img) 
    '''Threshold -- > Since the image pixel values range from 0 - 255 , We need binary image to draw contours ,so we set a threshold value so that 
                      the pixel values above the threshold value is set to a particular color and below is set to a particular color, we now get a 
                      binary image (image of 2 colors) 
                      '''
    ret,thresh = cv2.threshold(gray,127,255,1) # threshold value is 127 
     
    ''' Findcoutours is to find points of same pixel values '''
    j,contours,h = cv2.findContours(thresh,1,2)
    ''' variables to record the number of shapes in a particular image'''
    s=0
    c=0
    t=0
    hc=0
    p=0

    for cnt in contours:
        ''' approxPolyDP --> function to connect the contour points of same pixel values.This uses  'Ramer–Douglas–Peucker' algorithm 
                              https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm '''

        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

       ''' Depending upon the number of vertices we increment the shape values ''' 

        if len(approx)==5:
            p+=1
            cv2.drawContours(img,[cnt],0,255,-1)
        elif len(approx)==3:
            t+=1
            cv2.drawContours(img,[cnt],0,(0,255,0),-1)
            break
        elif len(approx)==4:
            s+=1
            cv2.drawContours(img,[cnt],0,(0,0,255),-1)
        elif len(approx) == 9:
            hc+=1
            cv2.drawContours(img,[cnt],0,(255,255,0),-1)
        elif len(approx) > 15 or len(approx)==8:
            c+=1
            cv2.drawContours(img,[cnt],0,(0,255,255),-1)

''' Finally we print the count of each shapes present in the particular image''' 

    ans="""
        CIRCLE = {}
        RECTANGLE={}
        TRIANGLE={}
        PENTAGON={}
        HALFCIRCLE={}
        """
    print(ans.format(c,s,t,p,hc))
    ''' imshow --> to show the output image '''
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
