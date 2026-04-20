import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

# -------------------------------
# 1. 이미지 읽기 & 리사이즈
# -------------------------------
img = cv.imread(r'C:\study-portfolio\Computer_Vision\practice\rose.png')
img = cv.resize(img, dsize=(0,0), fx=0.5, fy=0.5)

# -------------------------------
# 2. 중심 기준 시계방향 30도 회전
# -------------------------------
h, w = img.shape[:2]
cx, cy = w / 2, h / 2

theta = -30 * math.pi / 180

cos = math.cos(theta)
sin = math.sin(theta)

tx = cx - cx*cos + cy*sin
ty = cy - cx*sin - cy*cos

M = np.array([
    [cos, -sin, tx],
    [sin,  cos, ty]
], dtype=np.float32)

rotated = cv.warpAffine(img, M, (w, h))

# -------------------------------
# 3. 그레이 변환
# -------------------------------
gray = cv.cvtColor(rotated, cv.COLOR_BGR2GRAY)

# -------------------------------
# 4. 이진화
# -------------------------------
t, bin_img = cv.threshold(gray, 0, 255,
                          cv.THRESH_BINARY + cv.THRESH_OTSU)

# -------------------------------
# 5. 영역 자르기
# -------------------------------
b = bin_img[bin_img.shape[0]//2:bin_img.shape[0],
            0:bin_img.shape[1]//2]

# -------------------------------
# 6. 구조 요소
# -------------------------------
se = np.uint8([[0,0,1,0,0],
               [0,1,1,1,0],
               [1,1,1,1,1],
               [0,1,1,1,0],
               [0,0,1,0,0]])

# -------------------------------
# 7. 모폴로지 연산
# -------------------------------
b_dilation = cv.dilate(b, se, iterations=1)
b_erosion = cv.erode(b, se, iterations=1)
b_closing = cv.morphologyEx(b, cv.MORPH_CLOSE, se)

# -------------------------------
# 8. 한 화면에 모두 출력
# -------------------------------
fig, axes = plt.subplots(2, 4, figsize=(20,10))

axes[0,0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
axes[0,0].set_title("Original Color")
axes[0,1].imshow(cv.cvtColor(rotated, cv.COLOR_BGR2RGB))
axes[0,1].set_title("Rotated Color 30° CW")
axes[0,2].imshow(gray, cmap='gray')
axes[0,2].set_title("Grayscale")
axes[0,3].imshow(bin_img, cmap='gray')
axes[0,3].set_title("Binary (Otsu)")

axes[1,0].imshow(b, cmap='gray')
axes[1,0].set_title("Cropped Region")
axes[1,1].imshow(b_dilation, cmap='gray')
axes[1,1].set_title("Dilation")
axes[1,2].imshow(b_erosion, cmap='gray')
axes[1,2].set_title("Erosion")
axes[1,3].imshow(b_closing, cmap='gray')
axes[1,3].set_title("Closing")

for ax in axes.flatten():
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
