'''import os
os.environ['OPENCV_IO_MAX_IMAGE_PIXELS']=str(2**64)'''
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\Master-Admin\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("C:\\Users\\Master-Admin\\Desktop\\ocr\\bigsleep.jpg",0)
cv2.imshow("img",img)
cv2.waitKey(0)
text = pytesseract.image_to_string(img)
print(text)

img1 = cv2.imread("C:\\Users\\Master-Admin\\Desktop\\ocr\\book_page.jpg",0)
cv2.imshow("img1",img1)
cv2.waitKey(0)
img1 = cv2.resize(img1, None, fx=0.5, fy=0.5)
img1= cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
cv2.imshow("gray",gray)
cv2.waitKey(0)
config = "--psm 3"
text1 = pytesseract.image_to_string(adaptive_threshold, config=config)
print(text1)
