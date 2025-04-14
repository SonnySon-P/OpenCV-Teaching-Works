import cv2
import numpy as np

# 輸入影像檔案的路徑
imagePath = "image.jpg"

# 讀取圖檔
image = cv2.imread(imagePath)

# 取得圖片的總像素
rows = image.shape[0]  # 高度的像素
cols = image.shape[1]  # 寬度的像素

for y in range(0, rows):
    for x in range(0, cols):
        image[y, x, 0] = 255 - image[y, x, 0]  # 255 - 藍色
        image[y, x, 1] = 255 - image[y, x, 1]  # 255 - 綠色
        image[y, x, 2] = 255 - image[y, x, 2]  # 255 - 紅色

# 顯示圖片
cv2.imshow("ImageView", image)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉圖片視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有圖片視窗