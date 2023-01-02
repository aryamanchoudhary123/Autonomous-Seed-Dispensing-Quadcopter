import cv2
import time

if __name__ == "__main__":

    land_type = "cricket_field"     # ["cricket_field","forest_land","grass_land","hard_sand","road","tiles"]
    cam = cv2.VideoCapture(0)

    time.sleep(10) # 10 seconds delay for takeoff
    for i in range(120): #120 Photos each
        img_name = "{}_{}.png".format(land_type,i)
        result, frame = cam.read()
        cv2.imwrite(img_name, frame)
        time.sleep(1) # 1 second delay for each photo

    cam.release()
