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
#    A program to find HSV values to threshold a color.
#
#    Usage: python rangeFinder_HSV <path/to/image>
#           Press any key to exit.
#
#############################################################################


import cv
import sys

def threshold(valueList):
    cv.InRangeS(hsvFrame, (valueList[0], valueList[1], valueList[2]),
                          (valueList[3], valueList[4], valueList[5]), threshFrame)
    cv.ShowImage("Thresholded Image", threshFrame)

def maxHue(pos):
    valueList[3] = pos
    threshold(valueList)

def maxSat(pos):
    valueList[4] = pos
    threshold(valueList)

def maxVal(pos):
    valueList[5] = pos
    threshold(valueList)

def minHue(pos):
    valueList[0] = pos
    threshold(valueList)

def minSat(pos):
    valueList[1] = pos
    threshold(valueList)

def minVal(pos):
    valueList[2] = pos
    threshold(valueList)

valueList = [0, 0, 0, 0, 0, 0]
cv.NamedWindow("Trackbars", cv.CV_WINDOW_NORMAL)

frame = cv.LoadImage(sys.argv[1])
cv.ShowImage("Original Image", frame)

#Required Images
hsvFrame = cv.CreateImage(cv.GetSize(frame), 8, 3)
threshFrame = cv.CreateImage(cv.GetSize(frame), 8, 1)

#Convert input image to HSV
cv.CvtColor(frame, hsvFrame, cv.CV_BGR2HSV)
threshold(valueList)

#Create Trackbars
cv.CreateTrackbar("MIN_HUE", "Trackbars", 0, 180, minHue)
cv.CreateTrackbar("MIN_SAT", "Trackbars", 0, 255, minSat)
cv.CreateTrackbar("MIN_VAL", "Trackbars", 0, 255, minVal)
cv.CreateTrackbar("MAX_HUE", "Trackbars", 0, 180, maxHue)
cv.CreateTrackbar("MAX_SAT", "Trackbars", 0, 255, maxSat)
cv.CreateTrackbar("MAX_VAL", "Trackbars", 0, 255, maxVal)

#Set values of maxHue, maxSat and maxVal to maximum
cv.SetTrackbarPos("MAX_HUE", "Trackbars", 180)
cv.SetTrackbarPos("MAX_SAT", "Trackbars", 255)
cv.SetTrackbarPos("MAX_VAL", "Trackbars", 255)

cv.WaitKey()
