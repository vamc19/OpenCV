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

import cv

class videoStream():

    def __init__(self):
        self.stream=cv.CaptureFromCAM(1)
        cv.SetCaptureProperty(self.stream, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
        cv.SetCaptureProperty(self.stream, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
        cv.SetCaptureProperty(self.stream, cv.CV_CAP_PROP_FPS, 30)
        self.hsv = cv.CreateImage((640, 480), 8, 3)
        self.thresh = cv.CreateImage((640, 480), 8, 1)
        while True:
            self.frame = cv.QueryFrame(self.stream)
            cv.ShowImage("Input Image", self.frame)
            cv.CvtColor(self.frame, self.hsv, cv.CV_BGR2HSV)
            #cv.ShowImage("HSV Image", self.hsv)
            cv.InRangeS(self.hsv, (tb.h, tb.s, tb.v), (tb.H, tb.S, tb.V), self.thresh)
            cv.ShowImage("Threshold", self.thresh)
            cv.WaitKey(10)

class trackBar():

    def __init__(self):
        self.h = self.s = self.v = 0
        self.H = 180
        self.S = self.V = 255
        cv.CreateTrackbar("hue", "Trackbar", 0, 180, self.hue)
        cv.CreateTrackbar("sat", "Trackbar", 0, 255, self.sat)
        cv.CreateTrackbar("val", "Trackbar", 0, 255, self.val)
        cv.CreateTrackbar("HUE", "Trackbar", 0, 180, self.Hue)
        cv.CreateTrackbar("SAT", "Trackbar", 0, 255, self.Sat)
        cv.CreateTrackbar("VAL", "Trackbar", 0, 255, self.Val)
        cv.SetTrackbarPos("HUE", "Trackbar", 180)
        cv.SetTrackbarPos("SAT", "Trackbar", 255)
        cv.SetTrackbarPos("VAL", "Trackbar", 255)

    def hue(self, pos):
        self.h = pos

    def sat(self, pos):
        self.s = pos

    def val(self, pos):
        self.v = pos

    def Hue(self, pos):
        self.H = pos

    def Sat(self, pos):
        self.S = pos

    def Val(self, pos):
        self.V = pos

if __name__ == '__main__':
    cv.NamedWindow("Trackbar", cv.CV_WINDOW_NORMAL)
    tb = trackBar()
    vs = videoStream()
