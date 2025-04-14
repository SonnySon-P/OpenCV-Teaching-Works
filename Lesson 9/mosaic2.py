import cv2

# 輸入影像檔案的路徑
imagePath = "*.jpg"

# 讀取影像
image = cv2.imread(imagePath)

# 剪裁區域的尺寸
x = 800  # 剪裁區域起點x座標
y = 500  # 剪裁區域起點y座標
cw = 300  # 剪裁區域寬度
ch = 300  # 剪裁區域高度

# 取得剪裁區域
mosaic = image[y : y + ch, x : x + cw]

# 縮小比例
level = 20

# 按照比例縮小的尺寸
h = int(ch / level)
w = int(cw / level)

# 縮小尺寸
mosaic = cv2.resize(mosaic, (w, h), interpolation = cv2.INTER_LINEAR)

# 放大尺寸
mosaic = cv2.resize(mosaic, (cw, ch), interpolation = cv2.INTER_NEAREST)

# 將影像的剪裁區域，換成馬賽克的圖
image[y : y + ch, x : x + cw] = mosaic

# 顯示影像
cv2.imshow("ImageView", image)  # 使用名為ImageView的視窗標題名稱

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有影像視窗
