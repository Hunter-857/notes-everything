import cv2
import numpy as np

webcam = False
path = './asset/sqaure.png'
filter=4
minArea=1000
while True:
    img = cv2.imread(path)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 100, 100)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=3)
    imgThre = cv2.erode(imgDial, kernel, iterations=2)
    cv2.namedWindow('Canny', 0)
    cv2.imshow('Canny', imgThre)
    cv2.waitKey(0)
    contours, hiearchy = cv2.findContours(imgThre, cv2.RETR_EXTERNAL,   cv2.CHAIN_APPROX_SIMPLE)
    finalCountours = []#创建最终列表
    for i in contours:
        area = cv2.contourArea(i)
        if area > minArea:
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            bbox = cv2.boundingRect(approx)#左上角得坐标以及宽和高即得到边框
            if filter > 0:
                if len(approx) == filter:
                    finalCountours.append([len(approx), area, approx, bbox, i])
            else:
                finalCountours.append([len(approx), area, approx, bbox, i])
        finalCountours = sorted(finalCountours, key=lambda x: x[2], reverse=True)#依照面积排轮廓最大轮廓到最小
        for con in finalCountours:
            cv2.drawContours(img, con[4], -1, (0, 0, 255), 3)#con[4]是bbx
            cv2.imshow("1",img)
            # print(bbox)
            # print(len(finalCountours))
            biggest = finalCountours[0][2]#已经降序排列过了[0]为最大轮廓，即最大轮廓得四个角的坐标print(approx)
            # print(biggest)
            print(approx)