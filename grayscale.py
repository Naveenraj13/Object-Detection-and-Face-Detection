import cv2

img = cv2.imread("docker.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayImage.png", grayImg)

gaussianBlurImg = cv2.GaussianBlur(img, (21,21), 0)
cv2.imwrite("gaussianBlurImg.jpg",gaussianBlurImg)

cv2.imshow("Original", img)
cv2.imshow("Gray", grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
