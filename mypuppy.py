# Open images using opencv in the shell directly the CV2 from the notebook
import cv2

img = cv2.imread('Desktop/Anaconda/Computer-Vision-with-Python/DATA/00-puppy.jpg')
while True:
    cv2.imshow('mypuppy.py',img)
#IF we have waited at alteast 1ms AND we have pressed the Esc
    if cv2.waitKey(1) & 0xFF ==27:
        break
cv2.destroyAllWindows()