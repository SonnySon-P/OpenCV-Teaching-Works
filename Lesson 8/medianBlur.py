import cv2

# 輸入影像檔案的路徑
imagePath = "image.jpg"

# 讀取影像
image = cv2.imread(imagePath)

# 中值模糊(使用像素點周圍灰度值的中值，來代替該像素點的灰度值)
output = cv2.medianBlur(image, 9)  # 倒數第一個參數為模糊程度，必須是大於1的奇數

# 顯示影像
cv2.imshow("ImageView", output)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有影像視窗
