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
#    Classic Pong game written using OpenCV library.
#    
#    Key Bindings:
#        Use 'a' and 'd' keys to control bottom paddle
#        Use 'j' and 'l' keys to control top paddle
#
#    TODO
#    Maintain score of players individually.
#############################################################################

import cv2
import numpy as np
import random, sys

fieldWidth = 800
fieldHeight = 600
ballRad = 30
speed = 20

paddleHeight = 20
paddleWidth = 100
template = np.empty((fieldHeight, fieldWidth, 3), np.uint8)
template.fill(255)

xMove, yMove = random.randint(-5, 5), random.randint(-5, 5)
#xPos, yPos = random.randint(ballRad, fieldWidth-ballRad), random.randint(ballRad, fieldHeight-ballRad)
xPos, yPos = fieldWidth/2, fieldHeight/2

paddleOne = [fieldWidth/2, fieldHeight-paddleHeight/2]
paddleTwo = [fieldWidth/2, paddleHeight/2]

while True:
    field = np.copy(template)
    cv2.circle(field, (xPos, yPos), ballRad, (0, 190, 0), thickness = -1)
    cv2.rectangle(field, (paddleOne[0]-paddleWidth/2, paddleOne[1]+paddleHeight/2), 
                  (paddleOne[0]+paddleWidth/2, paddleOne[1]-paddleHeight/2), (100, 40, 40), -1)
    cv2.rectangle(field, (paddleTwo[0]-paddleWidth/2, paddleTwo[1]+paddleHeight/2), 
                  (paddleTwo[0]+paddleWidth/2, paddleTwo[1]-paddleHeight/2), (100, 40, 40), -1)
    
    if xPos-ballRad <= 0 or xPos+ballRad >= fieldWidth:
        xMove = -xMove
    elif yPos-ballRad <= paddleHeight or yPos+ballRad >= fieldHeight-paddleHeight:
        if xPos in xrange(paddleOne[0]-paddleWidth/2, paddleOne[0]+paddleWidth/2) or xPos in xrange(paddleTwo[0]-paddleWidth/2, paddleTwo[0]+paddleWidth/2):
            yMove = -yMove
        elif yPos-ballRad <= 0 or yPos+ballRad >= fieldHeight:
            cv2.waitKey(1000)
            sys.exit()
        
    xPos, yPos = xPos+xMove, yPos+yMove
    cv2.imshow("Pong", field)
    k = cv2.waitKey(speed)
    if k == 97:
        paddleOne[0] = paddleOne[0]-10
    if k == 100:
        paddleOne[0] = paddleOne[0]+10
        
    if k == 106:
        paddleTwo[0] = paddleTwo[0]-10
    if k == 108:
        paddleTwo[0] = paddleTwo[0]+10

