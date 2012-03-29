#!/usr/bin/python
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Author: Vamsi Krishna Atluri <vamc19@gmail.com>
#############################################################################


#############################################################################
#    This is a basic drawing program named after one of my favorite
#    painters, M.F. Hussain.
#
#    Key Bindings:
#        Press 'a' to save the image as 'image.jpg'
#        Press 'Esc' to exit the program
#
#    TODO
#    Add color chart instead of trackbars.
#############################################################################
import cv

#Default valuues of blue, green, red and radius of brush respectively.
values = [0, 0, 0, 5]


def onMove(event, x, y, flags, params):
    drawBrush(x, y)
    global i, lastX, lastY
    if i == 0:
        lastX = x
        lastY = y
    if flags == cv.CV_EVENT_FLAG_LBUTTON:
        drawLine(x, y, lastX, lastY, values)
        lastX = x
        lastY = y
        i = 2

    if event == cv.CV_EVENT_LBUTTONUP:
        i = 0


def drawBrush(x, y):
    tempImg = cv.CloneImage(img)
    cv.Circle(tempImg, (x, y), values[3]/2, (0, 0, 0), 1, 8, 0)
    cv.ShowImage("Huzain", tempImg)


def drawLine(x, y, lastX, lastY, values):
    cv.Line(img, (x, y), (lastX, lastY), (values[0], values[1], values[2]), values[3], 8, 0)


def drawPoint(x, y, values):
    cv.Circle(img, (x, y), values[3], (values[0], values[1], values[2]), -1, 8, 0)


def blue(value):
    values[0] = value
    changeSample(values)


def green(value):
    values[1] = value
    changeSample(values)


def red(value):
    values[2] = value
    changeSample(values)


def radius(value):
    values[3] = value


def changeSample(values):
    cv.Set(sample, (values[0], values[1], values[2]), None)
    cv.ShowImage("Tools", sample)


i = 0
img = cv.CreateImage((640, 480), 8, 3)
sample = cv.CreateImage((20, 20), 8, 3)
cv.Set(img, cv.CV_RGB(255, 255, 255), None)
cv.Set(sample, cv.CV_RGB(0, 0, 0), None)
cv.NamedWindow("Huzain", 1)
cv.NamedWindow("Tools", 1)

cv.CreateTrackbar("Red", "Tools", 0, 255, red)
cv.CreateTrackbar("Green", "Tools", 0, 255, green)
cv.CreateTrackbar("Blue", "Tools", 0, 255, blue)
cv.CreateTrackbar("Brush Size", "Tools", 1, 40, radius)
cv.SetTrackbarPos("Brush Size", "Tools", 5)

while True:
    cv.ShowImage("Huzain", img)
    cv.ShowImage("Tools", sample)
    cv.SetMouseCallback("Huzain", onMove, None)
    key = cv.WaitKey()
    if key == 97:
        cv.SaveImage("image.jpg", img)
        print "Image saved"
    if key == 27:
        exit()
