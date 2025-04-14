import cv2
import numpy as np

# 設定畫布
width, height = 400, 400
image = np.zeros([width, height, 3])

# 從上往下的藍色漸層
for i in range(height):
    image[i, :, 0] = int(256 * i / height)   # 從上往下填入綠色漸層

# 類型轉換
image = image.astype("float32") / 255

# 顯示影像
cv2.imshow("漸成影像", image)

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有影像視窗