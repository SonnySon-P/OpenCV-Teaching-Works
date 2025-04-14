import cv2

# 輸入影像檔案的路徑
imagePath = "image.jpg"

# 讀取影像
image = cv2.imread(imagePath)

# 平均模糊(計算指定區域所有像素的平均值，再將平均值取代中心像素)
output = cv2.blur(image, (10, 10))  # 指定區域單位大小為(10px, 10px)

# 顯示影像
cv2.imshow("ImageView", output)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有影像視窗