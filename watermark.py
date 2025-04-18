import cv2
import numpy as np

# 讀取影像
image = cv2.imread("image.jpg")
watermark = cv2.imread("car.png", cv2.IMREAD_UNCHANGED)

# 取得影像尺寸
imageWidth , imageHeight = image.shape[0 : 2]
watermarkWidth , watermarkHeight = watermark.shape[0 : 2]

# 計算浮水印擺放位置
x = (imageHeight - watermarkHeight) // 2
y = (imageWidth - watermarkWidth) // 2

# 提取影像要更改區域
changeRegion = image[y : y + watermarkHeight, x : x + watermarkWidth]

# 設定浮水印顏色通道透明度
if watermark.shape[2] == 4:  # 如果浮水印有Alpha通道
    alpha = watermark[:, :, 3] / 255.0
    watermark = watermark[:, :, 0 : 3]  # 移除Alpha通道
else:
    alpha = np.ones((watermarkWidth , watermarkHeight)) * 0.7  # 設定透明度

# 混合浮水印與原影像
for i in range(0, 3):
    changeRegion[:, :, i] = (1 - alpha) * changeRegion[:, :, i] + alpha * watermark[:, :, i]

# 將更改區域放回原影像
image[y : y + watermarkHeight, x : x + watermarkWidth] = changeRegion

# 顯示結果
cv2.imshow("Watermarked", image)

# 等待按鍵事件，按任意鍵關閉影像視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 關閉所有視窗
