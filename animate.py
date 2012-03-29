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
#    A program that can make a picture scroll across the window horizontally.
#
#    Usage: python animate <path/to/image>
#           Press ESC key to exit.
#
#############################################################################

import cv
import sys

img = cv.LoadImage(sys.argv[1])

width = img.width
height = img.height

sliceList = []
x = 0
i = 0
while x in range(width):
    slice = cv.GetSubRect(img, (x, 0, 1, height))
    sliceList.append(slice)
    x = x + 1

animImage = cv.CreateImage((width, height), 8, 3)
partList = []
x = 0
while x in range(width):
    part = cv.GetSubRect(animImage, (x, 0, 1, height))
    partList.append(part)
    x = x + 1

j = 0
i = 0
while True:
    for i in range(len(sliceList)):
        cv.Copy(sliceList[i], partList[j])
        j = j + 1
        if j >= len(partList):
            j = 0
    j = j + 1
    if j >= len(partList):
        j = 0
    cv.ShowImage('Window', animImage)
    k = cv.WaitKey(50) % 0x100
    if k == 27:
        break

