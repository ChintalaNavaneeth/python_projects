import qrcode
import os
import cv2
import time

i=0

while True:
    img = qrcode.make("18MIS7042/harkishan/f+tf/11:00/qr1/present/"+str(i))
    img.save(r"C:\Users\navan\OneDrive\Desktop\imags.jpg")
    d = cv2.QRCodeDetector()
    val, points, staraight_qrcode = d.detectAndDecode(cv2.imread(r"C:\Users\navan\OneDrive\Desktop\imags.jpg"))
    print(val)
    time.sleep(5)
    i=i+1
    os.remove(r"C:\Users\navan\OneDrive\Desktop\imags.jpg")
    if(i == 5):
        break




#reading image


#
# d = cv2.QRCodeDetector()
# val,points,staraight_qrcode = d.detectAndDecode(cv2.imread(r"C:\Users\navan\OneDrive\Desktop\images.jpg"))
# print(val)