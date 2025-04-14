import cv2

# 讀取影像
image = cv2.imread("./*.jpg")

# 影像處理
outputImage = cv2.resize(image, (200, 200))  # 改成200x200的影像大小

# 顯示處理後的圖片
cv2.imshow("更改尺寸後的影像", outputImage)

# 等待按鍵事件，並關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()