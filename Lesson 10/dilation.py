import cv2

# 輸入影像檔案的路徑
imagePath = "*.jpg"

# 讀取影像
image = cv2.imread(imagePath)

# BGR轉換為灰階與創建結構元素
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))

# 侵蝕處理
image = cv2.erode(image, kernel)
cv2.imshow("侵蝕處理影像", image)

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有影像視窗
