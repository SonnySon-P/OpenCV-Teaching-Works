import cv2
import numpy as np

# 輸入影像檔案的路徑
imagePath = "*.jpg"

# 讀取影像
image = cv2.imread(imagePath)

# 轉換成灰階色彩
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 轉換成二值化，其中變數ret是否成功轉換(成功會顯示閾值)，output轉換後的影像
ret, output = cv2.threshold(imageGray, 127, 255, cv2.THRESH_BINARY)  # 如果大於127就等於 255，反之等於0

# 顯示圖片
cv2.imshow("ImageView", output)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉圖片視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有圖片視窗