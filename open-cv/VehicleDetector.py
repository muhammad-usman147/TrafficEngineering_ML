import cv2

img = cv2.imread('Cropped frames with serial numbers/9.png')

harclassifier = 'carClassifier.xml'
car_cascade = cv2.CascadeClassifier(harclassifier)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray,1.1,1)
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)

cv2.imshow('fg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()