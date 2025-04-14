import cv2

# 輸入影像檔案的路徑
imagePath = "*.jpg"

# 讀取圖檔
image = cv2.imread(imagePath)

# 取得原始影像的尺寸
size = image.shape

# 縮小比例
level = 15

# 按照比例縮小的尺寸
h = int(size[0] / level)
w = int(size[1] / level)

# 縮小尺寸
output = cv2.resize(image, (w, h), interpolation = cv2.INTER_LINEAR)

# 放大尺寸
output = cv2.resize(output, (size[1], size[0]), interpolation = cv2.INTER_NEAREST)

# 顯示影像
cv2.imshow("ImageView", output)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有影像視窗
