import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import time
import imutils
	#creating window	
window = cv.namedWindow("countrs")

	# creating videocapture from main camera

cap = cv.VideoCapture(0);
counter = 0
def photo_analysis(im1, im2):
	im1 = np.around(np.divide(im1, 50.0), decimals = 1)
	im2 = np.around(np.divide(im2, 50.0), decimals = 1)
	
	return im2 - im1
"""
	Основные идеи:
		подклюить гугловский апи
		искать фото в гугле
		взять первые 10 фото
		сравнить схожесть с пооью ИИ или же BFmatcher, но только если бюудет работать,
		да и надо будет как то подклюить интернет к коробоке
	"""

while True:

	ret,img1 = cap.read()
				
	
	#starting photo analys
	
	#res  = photo_analysis(img1)
	res = 1
	if res  == 1:
		
		gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

		# working with an image
		blurred = cv.GaussianBlur(gray, (11,11),50)
		median = cv.medianBlur(blurred,5)
		
		# creating numpy masssive which takes information from blurreds
		pixels1 = np.around(np.divide(median, 50.0), decimals = 1)
		# modifying the image
		low_white = np.array(4,np.uint8)
		max_white = np.array(10,np.uint8)
		mask = cv.inRange(pixels1,(low_white), (max_white))	
		cv.imshow('main1', mask)
		cnts,hierarchy = cv.findContours(mask.copy(), cv.RETR_EXTERNAL,
			cv.CHAIN_APPROX_SIMPLE)	
		
		cv.drawContours(img1,cnts,-1,(255,0,0),3,cv.LINE_AA,hierarchy,1)
		cv.imshow('countrs', img1)
		
		counter += 1
					
		if  not ret:
			breaK
		k = cv.waitKey(1)
		if k%256 == 27:
		 break
"""
позднее добавить функции аналиха фотографий, в пларне, нужные - оставить, (полезные)
нужные же отпралять на аналих"""
