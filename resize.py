import cv2
import imutils

img = cv2.imread("docker.jpg")
resizeImg = imutils.resize(img, width=50)
cv2.imwrite("resized.png", resizeImg)

cv2.imshow("ori", img)
cv2.imshow("", resizeImg)

cv2.waitKey(0)

cv2.destroyAllWindows()
