import cv2

# 輸入影片檔案的路徑
videoPath = "*.mp4"

# 使用openCV開啟影片
cap = cv2.VideoCapture(videoPath)  # 替換為您的影片檔案路徑

# 檢查影像是否成功讀取
if not cap.isOpened():
    print("無法開啟影片檔案")
    exit()

# 播放影片
while True:
    ret, frame = cap.read()
    
    # 如果讀取失敗，則退出
    if not ret:
        print("無法接收影像幀")
        break

    # 顯示影片
    cv2.imshow("VideoView", frame)  # 使用名為VideoView的視窗標題名稱，顯示每一幀畫面

    # 等待5秒後，關閉影片視窗
    if cv2.waitKey(5000):
        break

# 釋放圖片機資源，並關閉視窗
cap.release()
cv2.destroyAllWindows()
