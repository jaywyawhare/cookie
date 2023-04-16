# put all your fingers down except the index finger and the thumb when you reach the dark brown path
# start tracking the shape, A blue line will start showing following your path
# game is over once the entire shape is traced

import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
intro = ('frames/img1.jpeg')
kill = ('frames/img2.img2.png')
winner = ('frames/img3.png')

# read the camera
cam = cv2.VideoCapture(0)

detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77)
# INITILIZING GAME COMPONENTS
# ----------------------------------------------------------------
sqr_img = ('img/sqr (2).png')  # read img/sqr (1) in the sqr_img variable
mlsa = ('img/mlsa.png')  # read img/mlsa in the mlsa variable

# INTRO SCREEN WILL STAY UNTIL Q IS PRESSED

while True:
    # Capture video from camera
    ret, frame = cam.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hand in the frame
    hand, _ = detector.findHands(frame)
    fingers = detector.fingersUp()

    # Draw intro screen
    cv2.imshow('Intro Screen', intro)

    # Check if index finger and thumb are up
    if len(fingers) == 2 and fingers[1] == 1 and fingers[2] == 1:
        # Draw blue line following the hand path
        overlayPNG(frame, mlsa, [200, 200])

    # Check if entire shape is traced
    # condition to check if entire shape is traced:
    if hand and hand[0]['lmList'][8][1] > rectangle_y and hand[0]['lmList'][8][1] < rectangle_y + rectangle_h and hand[0]['lmList'][8][0] > rectangle_x and hand[0]['lmList'][8][0] < rectangle_x + rectangle_w:
        gameOver = True

    # Check if lost
    if NotWon:
        for i in range(10):
            # show the loss screen from the kill image read before
            cv2.imshow('Loss Screen', kill)
            cv2.waitKey(1)
        while True:
            # show the loss screen from the kill image read before
            cv2.imshow('Loss Screen', kill)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # end it after we press q
                break
    else:
        # Check if won
        # show the win screen from the winner image read before
        cv2.imshow('Win Screen', winner)
        while True:
            # show the win screen from the winner image read before
            cv2.imshow('Win Screen', winner)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # end it after we press q
                break

# destroy all the windows

cv2.destroyAllWindows()
