import tensorflow as tf
import os
import pandas as pd
import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
from tensorflow.keras.models import load_model



def image_capture(img_name):
    cam = cv2.VideoCapture(0)
    ret,frame = cam.read()
    cv2.imwrite(img_name,frame)
    cam.release()

def prediction(img_name, model, class_names):
    img = cv2.imread(img_name) # change to direct camera feed
    image_resized = cv2.resize(image , (180,180))
    image_resized= np.expand_dims(image_resized,axis=0)

    pred_val = resnet_model.predict(image)
    print(pred_val)
    output = class_names[np.argmax(x)]
    return output


def action():

    servo1.start(0)
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

if __name__ == "__main__":

    # initial setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50)
    model = load_model("resnet_model.h5")
    class_names = ['Cricket Field', 'Forest Land', 'Grass', 'Hard Sand', 'Road', 'Tiles']

    ideal_class = ['Cricket Field', 'Forest Land', 'Grass']

    print("takeoff in process")
    time.sleep(5) # delay for takeoff
    print("takeoff complete")
    for i in range(100):
        image_name="test_flight_1_{}.png".format(i)
        image_capture(image_name)
        pred_val = prediction(image_name,model,class_names)
        if pred_val in ideal_class :
            print("dropping seed as Ideal Land")
            action()
        else:
            print("Non Ideal land detected")
        time.sleep(1)   # delay to move ahead
        print("Onto next piece of land")

    print("Flight Complete")
