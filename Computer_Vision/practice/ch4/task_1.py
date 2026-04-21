import cv2 as cv
import numpy as np

# 1. 이미지 불러오기
img = cv.imread('apples.jpg')
if img is None:
    print("이미지 로드 실패")
    exit()

# 2. 그레이스케일 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 3. Sobel 엣지 검출
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)

sobel = cv.magnitude(sobelx, sobely)
sobel = np.uint8(np.clip(sobel, 0, 255))

# 4. Canny 엣지 검출
canny = cv.Canny(gray, 100, 200)

# 5. Contour 추출
# (Canny 결과를 사용)
contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# 6. Contour 그리기
contour_img = img.copy()
cv.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

# 7. 결과 출력
cv.imshow('Original', img)
cv.imshow('Gray', gray)
cv.imshow('Sobel Edge', sobel)
cv.imshow('Canny Edge', canny)
cv.imshow('Contour', contour_img)

cv.waitKey(0)
cv.destroyAllWindows()