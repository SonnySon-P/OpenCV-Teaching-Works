import cv2
import numpy as np

# 輸入影片檔案的路徑
imagePath = "*.jpg"

# 讀取圖檔
image = cv2.imread(imagePath)

# 轉換為灰階圖像
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 創建ORB檢測器
orb = cv2.ORB_create()

# 檢測特徵點和計算描述符
keypoints, descriptors = orb.detectAndCompute(grayImage, None)

# 在圖像上繪製特徵點
imageWithKeypoints = cv2.drawKeypoints(image, keypoints, None, color = (0, 255, 0), flags = cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

# 顯示結果
cv2.imshow("ORB KeyPoints", imageWithKeypoints)

# 等待按鍵事件，按任意鍵關閉圖片視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有圖片視窗