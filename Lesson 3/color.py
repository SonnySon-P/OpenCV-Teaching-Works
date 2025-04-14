import cv2

# 讀取圖像
image = cv2.imread("*.jpg")

# 創建各顏色的副本
blueImage = image.copy()  # 藍色圖片
greenImage = image.copy()  # 綠色圖片
redImage = image.copy()  # 紅色圖片

# 去除其他顏色通道，保留藍色
blueImage[:, :, 1] = 0  # 將綠色通道設為0
blueImage[:, :, 2] = 0  # 將紅色通道設為0

# 去除其他顏色通道，保留綠色
greenImage[:, :, 0] = 0  # 將藍色通道設為0
greenImage[:, :, 2] = 0  # 將紅色通道設為0

# 去除其他顏色通道，保留紅色
redImage[:, :, 0] = 0  # 將藍色通道設為0
redImage[:, :, 1] = 0  # 將綠色通道設為0

# 顯示處理後的圖片
cv2.imshow("只保留藍色", blueImage)
cv2.imshow("只保留綠色", greenImage)
cv2.imshow("只保留紅色", redImage)

# 等待按鍵事件，並關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()