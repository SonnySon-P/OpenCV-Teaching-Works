import cv2
import numpy as np

# 輸入影像檔案的路徑
imagePath = "*.jpg"

# 讀取影像
image = cv2.imread(imagePath)

# 轉換成灰階色彩
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 模糊化
imageGray = cv2.medianBlur(imageGray, 7)

# 邊緣偵測
output = cv2.Sobel(imageGray, -1, 1, 1, 1, 7)  # 參數分別為：影像, x軸抓取邊緣, y軸抓取邊緣, 影像深度(設定為-1，表示使用圖片原本影像深度), 運算區域大小(預設是1，必須是正奇數), 縮放比例常數(預設是1，必須是正奇數)

# 顯示影像
cv2.imshow("ImageView", output)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有影像視窗
