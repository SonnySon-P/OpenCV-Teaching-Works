import cv2

# 輸入影片檔案的路徑
imagePath = "image.jpg"

# 讀取圖檔
image = cv2.imread(imagePath)

# 高斯模糊(計算指定區域所有像素的平均值，再將平均值取代中心像素)
output = cv2.GaussianBlur(image, (11, 11), 0, 0)  # 指定區域單位大小為(10px, 10px)，倒數第二個參數為X方向標準差，倒數第一個參數為Y方向標準差。兩者必須是必須是大於1的奇數，預設皆為0。

# 顯示圖片
cv2.imshow("ImageView", output)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉圖片視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有圖片視窗