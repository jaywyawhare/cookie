import os
import cv2
import time
import numpy as np
from cvzone import overlayPNG
from module import HandTrackingModule

folderpath = 'frames'
mylist = os.listdir(folderpath)
graphic = [cv2.imread(f'{folderpath}/{impath}') for impath in mylist]

intro = graphic[0]
kill = graphic[1]
win = graphic[2]
mlsa = graphic[3]
square = graphic[4]

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77)

gameOver = False
NotWon = True

while not gameOver:
    success, frame = cap.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hand, handBox = detector.findHands(gray)
    if hand:
        lmList = hand["lmList"]
        fingertips = [lmList[4], lmList[8]]

        if fingertips[0][1] < handBox[1] and fingertips[1][1] < handBox[1]:
            cv2.line(frame, fingertips[0], fingertips[1], (255, 0, 0), 3)

            if handBox[1] > hand["bbox"][1] + hand["bbox"][3] // 2:
                gameOver = True
                NotWon = False

    cv2.imshow("Game", frame)
    cv2.waitKey(1)

if NotWon:
    for i in range(10):
        cv2.imshow("Game", kill)
        cv2.waitKey(1)
    while True:
        cv2.imshow("Game", kill)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

else:
    for i in range(10):
        cv2.imshow("Game", win)
        cv2.waitKey(1)
    while True:
        cv2.imshow("Game", win)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
