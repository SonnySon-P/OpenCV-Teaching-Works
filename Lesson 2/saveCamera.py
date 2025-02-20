import cv2

# 開啟攝影機
cap = cv2.VideoCapture(0)  #  0代表預設的攝影機，若有多個攝影機可以改成其他數字

# 檢查攝影機是否成功開啟
if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

# 取得影像的寬度和高度
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 取得影像的寬度
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像的高度

# 定義影片的編碼格式與輸出檔案名稱
fourcc = cv2.VideoWriter_fourcc(*"XVID") # 使用XVID編碼，也可以使用MJPG
savePath = "output.mp4"  # 儲存影片檔案的路徑
out = cv2.VideoWriter(savePath, fourcc, 20.0, (frameWidth, frameHeight))  # 創建一個VideoWriter對象來保存錄製的影片

while True:
    ret, frame = cap.read()  # 讀取每一幀影像

    # 如果讀取不到攝影機畫面
    if not ret:
        print("無法接收影像幀")
        break

    # 寫入每一幀影像到影片檔案中
    out.write(frame)

    # 顯示畫面
    cv2.imshow("CameraView", frame)

    # 等待按鍵事件，按q關閉影片視窗
    if cv2.waitKey(1) == ord("q"):
        break

# 釋放攝影機資源，並關閉視窗
cap.release()
out.release()
cv2.destroyAllWindows()