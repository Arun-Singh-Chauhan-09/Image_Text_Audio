import cv2
import pytesseract
import os
os.chdir('C:/Users/ARUN/Downloads/text-from-image--master')



pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

image = cv2.imread('WAPP_3.jpeg',0)
thresh = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]

blur = cv2.GaussianBlur(thresh, (3,3), 0)
result = 255 - blur

data = pytesseract.image_to_string(result, lang='eng', config='--psm 6')

print(data)
# import re
# dates = re.search("([0-9]{2}\-[A-z]{3}\-[0-9]{4})", data) or re.search("([0-9]{2}\/[0-9]{2}\/[0-9]{4})", data)
# print("Date : " + dates[0])

# ddmmyyyy = dates[0]
# yyyymmdd = ddmmyyyy[7:] + "-" + ddmmyyyy[3:6] + "-" + ddmmyyyy[:2]
# print("Date : " + yyyymmdd)



# dates = str(dates)
# print("Date : " + dates)
cv2.imshow('thresh', thresh)
cv2.imshow('result', result)

cv2.waitKey()

# cv2.imwrite('result.jpeg',result)
#cv2.destroyAllWindows()