import cv2

# 開啟攝影機
cap = cv2.VideoCapture(0)  #  0代表預設的攝影機，若有多個攝影機可改成其它數字嘗試看看

# 檢查攝影機是否成功開啟
if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

# 顯示攝影機畫面
while True:
    ret, frame = cap.read()

    # 如果無法讀取影像
    if not ret:
        print("無法從攝影機讀取畫面")
        break

    # 顯示畫面
    cv2.imshow("CameraView", frame)

    # 等待按鍵事件，按q關閉影片視窗
    if cv2.waitKey(1) == ord("q"):
        break

# 釋放攝影機資源，並關閉視窗
cap.release()
cv2.destroyAllWindows()