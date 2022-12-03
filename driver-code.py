import tensorflow as tf
import os
import pandas as pd
import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
from tensorflow.keras.models import load_model



def image_capture(img_name):
    cam = cv2.VideoCapture(1)
    ret,frame = cam.read()
    cv2.imwrite(img_name,frame)
    cam.release()

def prediction(img_name):
    img = cv2.imread(img_name) # change to direct camera feed
    resize = tf.image.resize(img,(256,256))
    pred_val = new_model.predict(np.expand_dims(resize/255,0))
    return pred_val


def action(pred_val):
    print(pred_val)

    servo1.start(0)
    if pred_val > 0.5 :
        print("rotate motor as ideal")
        # to open the funnel
        angle = float(0)
        servo1.ChangeDutyCycle((2+(angle/18)))
        time.sleep(0.35)
        servo1.ChangeDutyCycle(0)
        # to close the funnel
        angle = float(110)
        servo1.ChangeDutyCycle((2+(angle/18)))
        time.sleep(0.35)
        servo1.ChangeDutyCycle(0)

        servo1.stop()
        GPIO.cleanup()
    else:
        print("Dont Rotate motor as non ideal")


if __name__ == "__main__":

    # initial setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50)
    new_model = load_model("imageclassifiernewversionlive.h5")

    print("takeoff in process")
    time.sleep(5) # delay for takeoff
    print("takeoff complete")
    for i in range(100):
        image_name="test_flight_1_{}.png".format(i)
        image_capture(image_name)
        pred_val = prediction(image_name)
        action(pred_val)
        time.sleep(1)   # delay to move ahead
        print("next part of land")
