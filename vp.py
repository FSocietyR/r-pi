import cv2 as cv
import random
import numpy as np
import time
import imutils
import io
from time import sleep
import picamera as pi
from picamera import PiCamera
from picamera.array import PiRGBArray

# from any_file import func()

#PiCamera class
class Camera(PiCamera):

        def __init__(self,
                    shutter_speed:int,
                    framerate:int,
                        iso: int,
                        saturation: int,
                            sharpness: int,
                            contrast: int,
                            brightness: int) -> object:
            
            PiCamera.__init__(self)

            #mostly turns off all camera properties
            self.flash_modes = 'off'
            self.exposure_mods = 'night'
            self.awb_modes = 'off'
            self.image_effects = 'negativ'
            self.drc_settings = 'off'
            self.stereo_mods = 'off' 

            self.resolution = (640,480)
            self.shutter_speed = shutter_speed #скорость затвора 
            self.framerate = framerate #fps 
            self.iso = iso #баланс белого
            self.saturation = saturation #насыщенность
            self.sharpness = sharpness #резкость
            self.contrast = contrast #контраст
            self.brightness = brightness #яркость

            
        def rawRGB(self) -> NoneType:
                return PiRGBArray(self, size = self.resolution)				



if __name__ == '__name__':


    window = cv.namedWindow("countrs") #main_frame
    counter = 0
    camera = Camera(10000000, 30, 100,-100,-100,100,10) #creating a PiCamera object

    def reworking(img:list) -> np.array:
    	"""
		So, too use other fucntions and find anything 
		in photos we need to change our main picture
		named as img1, whic is taken from picamera		

    	"""
        gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(gray, (11,11),50)
        median = cv.medianBlur(blurred,5)
        last = np.around(np.divide(median, 50.0), decimals = 1)
        return last

    remake_to_np_ms = lambda x: np.around(np.divide(x,50.0), decimals = 1)

    raw = camera.rawRGB()
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
                pixels1 = np.around(np.divide(diff, 0.1), decimals = 1)
                cv.imshow("pixels",pixels1)
                # modifying the image

                def draw():

                    low_white = np.array(4,np.uint8) #for rasberry use 4
                    max_white = np.array(10,np.uint8)
                    mask = cv.inRange(pixels1,(low_white), (max_white))	
                    cv.imshow('main1', mask)
                    cnts,hierarchy = cv.findContours(mask.copy(), cv.RETR_EXTERNAL,
                        cv.CHAIN_APPROX_SIMPLE)	

                    try:
                        for el in range(len(cnts)):
                            if cv.contourArea(cnts[el]) > 300 and cv.contourArea(cnts[el]) <= (640*320 / 10):
                                if cv.arcLength((cnts[el])**2 / cv.contourArea(cnts[el]))>= 60 and 300 >= cv.arcLength(cnts[el])**2 / cv.contourArea(cnts[el]):
                                    
                                    ((x, y), radius) = cv.minEnclosingCircle(cnts[el])
                                    M = cv.moments(cnts[el])
                                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                                    l = [ (lambda i: random.randrange(0,256))(i) for i in range(3)]
                                    cv.circle(img1, (int(x), int(y)), int(radius),
                                                    (l[0],l[1],l[-1]), 2)
                                    cv.circle(img1, center, 5, (0, 0, 255), -1)
                                    cv.putText(img1, cv.contourArea(cnts[el]), (int(x), int(y)), cv.FONT_HERSHEY_SIMPLEX, (l[0],l[1],l[-1]), 2)

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
