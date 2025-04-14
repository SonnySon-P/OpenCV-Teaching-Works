import cv2
import numpy as np
import random

# 設定圖像大小
width, height = 400, 400
image = np.zeros((height, width, 3), dtype = "uint8")  # 建立 400x400 黑色背景的圖像

# 計算要變成白色的像素數量(40% 的像素)
whitePixelsNumber = int(width * height * 0.4)

# 隨機選擇像素位置並將其變為白色
for _ in range(whitePixelsNumber):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    image[y, x] = [255, 255, 255]  # 將該位置的像素設為白色

# 存儲並顯示圖片
cv2.imwrite("noise.jpg", image)
cv2.imshow("noise", image)
cv2.waitKey(0)
cv2.destroyAllWindows()