import cv2

# 讀取影像
image = cv2.imread("./*.jpg")

# 影像處理
outputImage1 = cv2.flip(image, 0)  # 0:上下翻轉、1:左右翻轉:、-1:上下左右翻轉
outputImage2 = cv2.transpose(image)  # 逆時針旋轉90度
outputImage3 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)  # output_ROTATE_90_CLOCKWISE、output_ROTATE_90_COUNTERCLOCKWISE、output_ROTATE_180

# 顯示處理後的影像
cv2.imshow("影像上下翻轉", outputImage1)
cv2.imshow("影像逆時針旋轉90度", outputImage2)
cv2.imshow("影像直角", outputImage3)

# 等待按鍵事件，並關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()