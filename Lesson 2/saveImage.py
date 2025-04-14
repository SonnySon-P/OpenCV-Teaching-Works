import cv2

# 讀取圖片
image = cv2.imread("*.jpg", cv2.IMREAD_GRAYSCALE)  # 以灰階模式開啟圖片，可選擇cv2.IMREAD_COLOR、cv2.IMREAD_GRAYSCALE、cv2.IMREAD_UNCHANGED、cv2.IMREAD_ANYCOLOR、cv2.IMREAD_ANYDEPTH、cv2.IMREAD_REDUCED_GRAYSCALE_2、cv2.IMREAD_REDUCED_COLOR_2、cv2.IMREAD_REDUCED_GRAYSCALE_4、cv2.IMREAD_REDUCED_COLOR_4、cv2.IMREAD_REDUCED_GRAYSCALE_8、cv2.IMREAD_REDUCED_COLOR_8

# 儲存圖片
cv2.imwrite("testSave.png", image)  # imwrite() 有三個參數，第一個參數為檔案的路徑和名稱，第二個參數為要寫入的資料內容，第三個參數為圖片壓縮品質的設定
