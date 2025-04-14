import cv2
import numpy as np

# 輸入影像檔案的路徑
imagePath = "*.jpg"

# 讀取影像
image = cv2.imread(imagePath)

# 轉換公式
contrast = 200
brightness = 0
output = image * (contrast / 127 + 1) - contrast + brightness

# 處理調整後數值大多為浮點數，且可能會小於0或大於255
output = np.clip(output, 0, 255)  # 將數值對應到0～255之間
output = np.uint8(output)  # 轉換成正整數

# 顯示圖片
cv2.imshow("ImageView", output)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉圖片視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有圖片視窗