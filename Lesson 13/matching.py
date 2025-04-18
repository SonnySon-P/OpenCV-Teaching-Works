import cv2
import numpy as np

# 讀取圖檔
image1 = cv2.imread("*.jpg")
image2 = cv2.imread("**.jpg")

# 創建ORB檢測器
orb = cv2.ORB_create()

# 檢測特徵點和計算描述符
keypoints1, descriptors1 = orb.detectAndCompute(image1, None)
keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

# 使用暴力匹配器來匹配描述符
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 匹配特徵點
matches = bf.match(descriptors1, descriptors2)

# 根據匹配的數量來計算相似度
matches = sorted(matches, key = lambda x: x.distance)

# 根據匹配數量來判斷相似度
similarity = len(matches)
print(f"兩張影像的特徵匹配點數量: {similarity}")
if similarity > 50:
    print("影像相似度高")
elif similarity > 20:
    print("影像相似度中等")
else:
    print("影像相似度低")

# 顯示匹配結果
resultImage = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches[0 : 50], None, flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# 顯示結果
cv2.imshow("Matches", resultImage)

# 等待按鍵事件，按任意鍵關閉圖片視窗
cv2.waitKey(0)  # 按下任意鍵
cv2.destroyAllWindows()  # 結束所有圖片視窗
