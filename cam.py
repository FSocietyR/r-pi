import cv2 as cv
import numpy as np
import time
import imutils
import io
from time import sleep
import picamera as pi
from picamera.array import PiRGBArray
from picamera import PiCamera

class Camera(PiCamera):
	def __init__(self,
				  shutter_speed:int,
				   framerate:int,
				     exposure_mode:str,
					  iso: int,
					   saturation: int,
					    sharpness: int,
						 contrast: int,
						  brightness: int ):
		self = PiCamera()
		self.shutter_speed = shutter_speed #скорость затвора 
		self.framerate = framerate #fps
		self.exposure_mode = exposure_mode #экспозиция 
		self.iso = iso #баланс белого
		self.saturation = saturation #насыщенность
		self.sharpness = sharpness #резкость
		self.contrast = contrast #контраст
		self.brightness = brightness #яркость 
		


"""with PiCamera() as camera:
	camera.shutter_speed = 10000000
	camera.framerate = 30
	camera.exposure_mode = 'night'
	camera.start_preview()
	with PiRGBArray(camera) as stream:
		camera.capture(stream,format='bgr',use_video_port=True)
		while 1:
			image = stream.array
			cv.imshow("test",image)
			
			k = cv.waitKey(1)
			
			if k%256 == 27:
				break
"""

camera = PiCamera()
camera.resolution=(1280,720)
camera.framerate=(30)
camera.shutter_speed = 10000000
camera.exposure_mode = 'night'
camera.iso = 0
camera.contrast = -50
camera.brightness = 50
camera.sharpness = 0
raw = PiRGBArray(camera, size = (1280,720))	

cap = cv.VideoCapture(0)

for frame in camera.capture_continuous(raw,format='bgr', use_video_port = True):

	image = frame.array
	cv.imshow("Frame", image)
	k = cv.waitKey(1)
	raw.truncate(0)
			
	if k%256 == 27:
		break
	
