import cv2

# 輸入影片檔案的路徑
videoPath = "*.mp4"

# 使用openCV開啟影片
cap = cv2.VideoCapture(videoPath)  # 替換為您的影片檔案路徑

# 檢查影像是否成功讀取
if not cap.isOpened():
    print("無法開啟影片檔案")
    exit()

 # 輸出的檔案名稱
outputPath = "grayImage.jpg" 

# 播放影片
while True:
    ret, frame = cap.read()
    
    # 如果讀取失敗，則退出
    if not ret:
        print("無法接收影像幀")
        break

    # 將影像轉換為灰階
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 顯示影片
    cv2.imshow("VideoView", grayFrame)  # 使用名為VideoView的視窗標題名稱，顯示每一幀畫面

# 儲存轉換後的灰階影像
cv2.imwrite(outputPath, grayImage)

# 顯示原始影像和灰階影像
cv2.imshow("Gray Image", grayImage)

# 等待任意鍵關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
