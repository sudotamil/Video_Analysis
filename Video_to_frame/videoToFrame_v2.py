
import cv2
import math
videoFile = "/home/bigtapp/projects/MY_Project/SampleVideo_1280x720_2mb.mp4"

cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = '/home/bigtapp/projects/MY_Project/frames/' +  str(int(x)) + ".jpg";x+=1
        cv2.imwrite(filename, frame)

cap.release()
print ("Done!")
