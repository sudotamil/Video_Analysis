import cv2
import sys
import os

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))
'''
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("image", image)
    #cv2.imwrite("roi.jpg", roi)
'''
count = 1
for f in faces:
    x, y, w, h = [ v for v in f ]
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    sub_face = image[y:y+h, x:x+w]
    filename, file_extension = os.path.splitext(imagePath)
    cv2.imwrite(filename+str(count)+file_extension, sub_face)
    count = count + 1
    

cv2.imshow("Faces found", image)
cv2.waitKey(0)
