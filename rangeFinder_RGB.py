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
#    A program to find RGB values to threshold a color.
#
#    Usage: python rangeFinder_RGB <path/to/image>
#           Press any key to exit.
#
#############################################################################


import cv
import sys

def threshold(valueList):
    cv.InRangeS(frame, (valueList[0], valueList[1], valueList[2]),
               (valueList[3], valueList[4], valueList[5]), threshFrame)
    cv.ShowImage("Thresholded Image", threshFrame)


def maxBlue(pos):
    valueList[3] = pos
    threshold(valueList)


def maxGreen(pos):
    valueList[4] = pos
    threshold(valueList)


def maxRed(pos):
    valueList[5] = pos
    threshold(valueList)


def minBlue(pos):
    valueList[0] = pos
    threshold(valueList)


def minGreen(pos):
    valueList[1] = pos
    threshold(valueList)


def minRed(pos):
    valueList[2] = pos
    threshold(valueList)

valueList = [0, 0, 0, 0, 0, 0]
cv.NamedWindow("Trackbars", cv.CV_WINDOW_NORMAL)

frame = cv.LoadImage(sys.argv[1])
cv.ShowImage("Original Image", frame)

#Required Images
threshFrame = cv.CreateImage(cv.GetSize(frame), 8, 1)

threshold(valueList)

#Create Trackbars
cv.CreateTrackbar("MIN_Red", "Trackbars", 0, 255, minRed)
cv.CreateTrackbar("MIN_Green", "Trackbars", 0, 255, minGreen)
cv.CreateTrackbar("MIN_Blue", "Trackbars", 0, 255, minBlue)
cv.CreateTrackbar("MAX_Red", "Trackbars", 0, 255, maxRed)
cv.CreateTrackbar("MAX_Green", "Trackbars", 0, 255, maxGreen)
cv.CreateTrackbar("MAX_Blue", "Trackbars", 0, 255, maxBlue)


#Set values of maxBlue, maxGreen and maxRed to maximum
cv.SetTrackbarPos("MAX_Blue", "Trackbars", 255)
cv.SetTrackbarPos("MAX_Green", "Trackbars", 255)
cv.SetTrackbarPos("MAX_Red", "Trackbars", 255)

cv.WaitKey()
