import cv2 as cv

img = cv.imread("Photos/park.jpg")

cv.imshow("park", img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Image Grayscale", gray)

# Blur 이미지 흐림
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow("Resized", resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
