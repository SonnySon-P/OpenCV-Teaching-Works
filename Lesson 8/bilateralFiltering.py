import cv2

# 輸入影像檔案的路徑
imagePath = "image.jpg"

# 讀取影像
image = cv2.imread(imagePath)

# 雙邊模糊(使用非線性的雙邊濾波器，同時保留影像內容的邊緣)
output = cv2.bilateralFilter(image, 60, 20, 40)  # 第二個參數為相鄰像素的直徑;第二個參數為相鄰像素的顏色混合，數值越大，會混合更多區域的顏色;第三個參數為區域單位大小

# 顯示影像
cv2.imshow("ImageView", output)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有影像視窗