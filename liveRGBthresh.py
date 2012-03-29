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
        self.stream = cv.CaptureFromCAM(0)
        self.thresh = cv.CreateImage((640, 480), 8, 1)
        while True:
            self.frame = cv.QueryFrame(self.stream)
            cv.ShowImage("Input Image", self.frame)
            cv.InRangeS(self.frame, (tb.h, tb.s, tb.v), (tb.H, tb.S, tb.V), self.thresh)
            cv.ShowImage("Threshold", self.thresh)
            cv.WaitKey(10)

class trackBar():

    def __init__(self):
        self.h = self.s = self.v = 0
        self.H = self.S = self.V = 255
        cv.CreateTrackbar("red", "Trackbar", 0, 255, self.hue)
        cv.CreateTrackbar("green", "Trackbar", 0, 255, self.sat)
        cv.CreateTrackbar("blue", "Trackbar", 0, 255, self.val)
        cv.CreateTrackbar("RED", "Trackbar", 0, 255, self.Hue)
        cv.CreateTrackbar("GREEN", "Trackbar", 0, 255, self.Sat)
        cv.CreateTrackbar("BLUE", "Trackbar", 0, 255, self.Val)
        cv.SetTrackbarPos("RED", "Trackbar", 255)
        cv.SetTrackbarPos("GREEN", "Trackbar", 255)
        cv.SetTrackbarPos("BLUE", "Trackbar", 255)

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
    cv.NamedWindow("Trackbar", cv.CV_WINDOW_AUTOSIZE)
    tb = trackBar()
    vs = videoStream()


