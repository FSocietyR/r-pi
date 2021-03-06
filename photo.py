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
from activation import start
from datetime import datetime
from rasberry_pi_bot import upload
import os
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
            """
            #mostly turns off all camera properties
            self.flash_modes = 'off'
            self.exposure_mods = 'night'
            self.awb_modes = 'off'
            self.image_effects = 'negativ'
            self.drc_settings = 'off'
            self.stereo_mods = 'off' """

            self.resolution = (640,480)
            self.shutter_speed = shutter_speed #скорость затвора 
            self.framerate = framerate #fps 
            #self.iso = iso #баланс белого
            self.iso = iso
            self.saturation = saturation #насыщенность
            self.sharpness = sharpness #резкость
            self.contrast = contrast #контраст
            self.brightness = brightness #яркость

            
        def rawRGB(self):
                return PiRGBArray(self, size = self.resolution)             

def delete_file(file):
    
    if os.path.exists(file):
        os.remove(file)
        
    		
def taking_photo(img):
    img_name = datetime.now(tz = None)
    img_name = str(str(img_name.year) + '-' + str(img_name.month) + '-' + str(img_name.day) + '-' + str(img_name.hour) + '-'+str(img_name.minute)+'-'+str(img_name.second)+ '.jpg')
    cv.imwrite(img_name, img)
    upload(img_name)
    
    delete_file(img_name)
    
    		
def reworking(img:list) -> np.array:
    """
    So, too use other fucntions and find anything 
    in photos we need to change our main picture
    named as img1, whic is taken from picamera      
    """
    """(height, width) = img[:2]
    Centre = (width/2, height/2)
    unfinished_rotate = cv.getRotationMatrix2D(Centre, 180, 1.0)
    rotated_mask = cv.warpAffine(img, unfinished_rotate, (width, height))"""
    
    flipped_image = cv.flip(img,0)
    
    gray = cv.cvtColor(flipped_image,cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (11,11),50)
    median = cv.medianBlur(blurred,5)
    last = np.around(np.divide(median, 50.0), decimals = 1)
    return last

#remake_to_np_ms = lambda x: np.around(np.divide(x,50.0), decimals = 1)
def Main():
    counter = 0
    camera = Camera(10000000, 20, 100,-100,-100,100,10) #creating a PiCamera object
    raw = camera.rawRGB()
    for frame in camera.capture_continuous(raw,format='bgr', use_video_port = True):
        img1 = frame.array
        
        image = reworking(img1)
        cv.imshow('camera_video', image)\
                                  ;cv.imshow('orig',img1)
        
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
            diff[diff<=0] = 0
            
            
            cropped_img = diff[280:480, 230:460]
            black_img = np.zeros((cropped_img.shape[0],cropped_img.shape[1]))
            cv.circle(black_img,(100,100),100,1,-1)            
            outworked_img = cv.bitwise_and(cropped_img,black_img)
            cv.imshow('cut',outworked_img)
            #starting photo analys
        #res  = photo_analysis(img1)
            
                
        delete_file('activation.pyc')
        raw.truncate(0)
        counter = 1
        time.sleep(0.1)
        k = cv.waitKey(1)
        if k%256 == 27:
            break
        
if __name__ == "__main__":
    Main()


