import cv2
import numpy

# Press Esc to exit the program.

stream = cv2.VideoCapture(0)
width = stream.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
height = stream.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)

cascade_file = '/home/vamc/src/OpenCV/data/haarcascades/haarcascade_frontalface_alt.xml'
cascade_classifier = cv2.CascadeClassifier(cascade_file)

scale_factor = 4
file_number = 0

while True:
    frame = stream.read()[1]
    gray_image = cv2.cvtColor(frame, cv2.cv.CV_RGB2GRAY)
    gray_image = cv2.resize(gray_image, (int(width/scale_factor), int(height/scale_factor)))
    detected_faces = cascade_classifier.detectMultiScale(gray_image)
    if detected_faces is not None:
        for [x, y, w, h] in detected_faces:
 #           roi = frame[y*scale_factor: (y+h)*scale_factor, x*scale_factor: (x+w)*scale_factor]
 #           file_name = 'faces/vamc/%05d.jpg' % file_number
 #           cv2.imwrite(file_name, roi)
 #           file_number += 1
 #           print "File count:", file_number
            cv2.rectangle(frame, (x*scale_factor, y*scale_factor), ((x+w)*scale_factor, (y+h)*scale_factor), (0, 0, 255), 2)

    cv2.imshow("Face Detection Demo", frame)
    key = cv2.waitKey(delay=10)
    if key == 27:
        exit()