import cv2 as cv
from PIL import Image
from pytesseract import pytesseract
import csv
imgpath = r'C:\Users\aswin\Face_detecton_foler\dtectedface.png'
capture = cv.VideoCapture(0)
while True:
    boolean, img = capture.read()
    cv.imshow('Text detection',img)
    if cv.waitKey(1)& 0xFF==ord('q'):
        cv.imwrite(imgpath,img)
        break
capture.release()
cv.destroyAllWindows()

def tessract():
    path_to_tessract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = path_to_tessract
    text = pytesseract.image_to_string(Image.open(imgpath))
    
    return text[:-1].strip()
vehi_num = tessract()
print(vehi_num)
with open(r"C:\Users\aswin\PycharmProjects\pythonProject\vehicle_details.csv") as vehicle_det:
    vehicle_details_data = csv.reader(vehicle_det)
    next(vehicle_details_data)
    for row in vehicle_details_data:
        #print(row[0])
        if row[0].strip()==vehi_num.strip():
            print("Vehicle Details\n")
            print("Vehicle Number :%s \nMotorist Name : %s \nAmount : %s"%(row[0],row[1],row[2]))
            break
        '''else:
            print("Vehicle Details\n")
            print("Vehicle Number :KLA12345 \nMotorist Name : Aswin Raju \nAmount :150")
            break'''

