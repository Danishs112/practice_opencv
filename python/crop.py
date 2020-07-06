import cv2

img = cv2.imread("img/run.jpg")

h,w = img.shape[:2]

#print(h,w)

cv2.imshow("original",img) 


y = int(h) -100

x = int(w) -100

output = img[0:y,0:x]

cv2.imshow("output",output)

cv2.waitKey(0)