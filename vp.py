import cv2 as cv
import numpy as np
import time
import imutils
from time import sleep
import picamera as pi
from picamera.array import PiRGBArray
from picamera import PiCamera
	#creating window	
window = cv.namedWindow("countrs")
	# creating videocapture from main camera

cap = cv.VideoCapture(0)

counter = 0

class Camera:
	def __init__(self,
				  shutter_speed:int,
				   framerate:int,
				     exposure_mode:str,
					  iso: int,
					   saturation: int,
					    sharpness: int,
						 contrast: int,
						  brightness: int ):
		self = Picamera()
		self.shutter_speed = shutter_speed #скорость затвора 
		self.framerate = framerate #fps
		self.exposure_mode = exposure_mode #экспозиция 
		self.iso = iso #баланс белого
		self.saturation = saturation #насыщенность
		self.sharpness = sharpness #резкость
		self.contrast = contrast #контраст
		self.brightness = brightness #яркость

	def capture(self) -> object:
		return PiRGBarray(self)	

	def  Main(self):
		for frame in self.capture_continious(capture(self), "bgr", use_video_port = True):
			return frame.array


camera = Camera(camera, 10000000, 30, 'night', 100,-100,-100,100,10)

def reworking(img):
	
	gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
	blurred = cv.GaussianBlur(gray, (11,11),50)
	median = cv.medianBlur(blurred,5)
	last = np.around(np.divide(median, 50.0), decimals = 1)
	
	return last

"""

	Основные идеи:

		подклюить гугловский апи

		искать фото в гугле

		взять первые 10 фото

		сравнить схожесть с пооью ИИ или же BFmatcher, но только если бюудет работать,

		да и надо будет как то подклюить интернет к коробоке

	"""

remake_to_np_ms = lambda x: np.around(np.divide(x,50.0), decimals = 1)

while True:

	img1 = Camera.Main(camera)
	image = reworking(img1)
	if counter == 0:
		img_matrix = []
		img_matrix.append(image)
	elif counter % 1 == 0:
		if len(img_matrix) == 1:
			img_matrix.append(image)
		else:
			img_matrix[0] = img_matrix[-1]
			img_matrix[-1] = (image)
		
		diff = img_matrix[-1]-img_matrix[0]
		diff[diff<0] = 0
		
		cv.imshow('a',img_matrix[0])
		cv.imshow('b',img_matrix[-1])
		cv.imshow('c',diff)	 	
	#starting photo analys
	#res  = photo_analysis(img1)

		res = 1

		if res  == 1:

			
			# working with an image
			# creating numpy masssive which takes information from blurreds

			pixels1 = np.around(np.divide(diff, 0.5), decimals = 1)
			# modifying the image
			def draw():
				low_white = np.array(2,np.uint8) #for rasberry use 4

				max_white = np.array(10,np.uint8)

				mask = cv.inRange(pixels1,(low_white), (max_white))	

				cv.imshow('main1', mask)

				cnts,hierarchy = cv.findContours(mask.copy(), cv.RETR_EXTERNAL,

					cv.CHAIN_APPROX_SIMPLE)	

				#cv.drawContours(img1,cnts,-1,(255,0,0),3,cv.LINE_AA,hierarchy,1)
				try:
					for el in range(len(cnts)):
						if cv.contourArea(cnts[el]) > 300:
							cv.drawContours(img1,cnts,el,(255,0,0),3,cv.LINE_AA,hierarchy,1)
				except IndexError:
					pass
			draw()
			cv.imshow('cntr',img1)
			cv.imshow('countrs', image)
			

	

	counter = 1
	time.sleep(0.1)
				

	if  not ret:

		breaK

	k = cv.waitKey(1)

	if k%256 == 27:

	 break

"""

позднее добавить функции аналиха фотографий, в пларне, нужные - оставить, (полезные)

нужные же отпралять на аналих"""
