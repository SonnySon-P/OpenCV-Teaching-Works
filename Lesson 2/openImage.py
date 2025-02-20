import cv2

# 輸入影片檔案的路徑
imagePath = "image.jpg"

# 讀取圖檔
image = cv2.imread(imagePath)  # 預設使用cv2.IMREAD_COLOR模式

# 顯示圖片
cv2.imshow("ImageView", image)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉圖片視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有圖片視窗