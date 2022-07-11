import cv2

haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

while True:
    data,image = camera.read()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImage, 1.3, 4)
    for(x,y,w,h) in face:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("Detected Face...", image)
    key = cv2.waitKey(10)
    if key == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()
