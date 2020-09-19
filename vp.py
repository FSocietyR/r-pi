from import cv2 as cv
import numpy as np
import time
import imutils
import io
from time import sleep
import picamera as pi
from picamera import PiCamera
from picamera.array import PiRGBArray

	#creating window	

window = cv.namedWindow("countrs")

	# creating videocapture from main camera
counter = 0

class Camera(PiCamera):

	def __init__(self,
				  shutter_speed:int,
				   framerate:int,
				     exposure_mode:str,
					  iso: int,
					   saturation: int,
					    sharpness: int,
						 contrast: int,
						  brightness: int):
		
		PiCamera.__init__(self)

		self.resolution = (640,480)
		self.shutter_speed = shutter_speed #скорость затвора 
		self.framerate = framerate #fps
		self.exposure_mode = exposure_mode #экспозиция 
		self.iso = iso #баланс белого
		self.saturation = saturation #насыщенность
		self.sharpness = sharpness #резкость
		self.contrast = contrast #контраст
		self.brightness = brightness #яркость 
		
		



	def rawRGB(self):

		return PiRGBArray(self, size = (640,480)) 					

camera = Camera(10000000, 30, 'night', 100,-100,-100,100,10)

def reworking(img):

	

	gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

	blurred = cv.GaussianBlur(gray, (11,11),50)

	median = cv.medianBlur(blurred,5)

	last = np.around(np.divide(median, 50.0), decimals = 1)

	

	return last



def taking_photo(img):

	pass

"""

	Основные идеи:
		подклюить гугловский апи
		искать фото в гугле
		взять первые 10 фото
		сравнить схожесть с пооью ИИ или же BFmatcher, но только если бюудет работать,
		да и надо будет как то подклюить интернет к коробоке

	"""



remake_to_np_ms = lambda x: np.around(np.divide(x,50.0), decimals = 1)

"""

camera = PiCamera()
camera.resolution = (640,320)
camera.shutter_speed = 10000000
camera.exposure_mode = 'off'
camera.drc_strength = 'off'
camera.sharpness = 0
camera.contrast = 0
camera.awb_mode = 'off'
camera.iso = 100f
raw = PiRGBArray(camera, size = camera.resolution)"""

raw = camera.rawRGB()

print(raw)

while True:
	for frame in camera.capture_continuous(raw,format='bgr', use_video_port = True):
		img1 = frame.array
		cv.imshow('rand',img1)
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
				cv.imshow("pixels",pixels1)
				# modifying the image

				def draw():

					low_white = np.array(4,np.uint8) #for rasberry use 4
					max_white = np.array(10,np.uint8)
					mask = cv.inRange(pixels1,(low_white), (max_white))	
					cv.imshow('main1', mask)
					cnts,hierarchy = cv.findContours(mask.copy(), cv.RETR_EXTERNAL,
						cv.CHAIN_APPROX_SIMPLE)	



					#cv.drawContours(img1,cnts,-1,(255,0,0),3,cv.LINE_AA,hierarchy,1)

					try:
						for el in range(len(cnts)):
							if cv.contourArea(cnts[el]) > 300 and cv.contourArea(cnts[el]) <= (640*320 / 10):
								cv.drawContours(img1,cnts,el,(255,0,0),3,cv.LINE_AA,hierarchy,1)
					except IndexError:
						pass

				draw()
				cv.imshow('cntr',img1)
				cv.imshow('countrs', image)

			raw.truncate(0)
			counter = 1
			time.sleep(0.1)
			k = cv.waitKey(1)
			if k%256 == 27:
				break

