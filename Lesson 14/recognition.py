import cv2

# 輸入影片檔案的路徑
imagePath = "*.jpg"

# 讀取圖檔
image = cv2.imread(imagePath)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 載入人臉模型
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 偵測人臉
faces = faceCascade.detectMultiScale(grayImage)

for (x, y, width, height) in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

# 顯示圖片
cv2.imshow("人臉辨識", image)

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有影像視窗