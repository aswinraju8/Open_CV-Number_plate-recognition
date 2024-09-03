# Open_CV Number_Plate recognition
## Project Overview
This project captures an image using a webcam, extracts text from the image using Optical Character Recognition (OCR) with Tesseract, and then matches the extracted text with vehicle details stored in a CSV file. The main goal of this project is to detect a vehicle's registration number from an image and retrieve the corresponding vehicle details such as the motorist's name and any associated amount due.
## Prerequisites
Before running the code, ensure that you have the following installed:

1. Python (version 3.6 or higher)
2. OpenCV for Python (cv2)
3. Pillow (Python Imaging Library)
4. pytesseract (Python wrapper for Tesseract-OCR)
5. Tesseract-OCR executable installed on your machine
## Installation
1. Install the required Python libraries:
```
pip install opencv-python pillow pytesseract
```
2. Install Tesseract-OCR:

Download and install Tesseract-OCR from this link (https://github.com/tesseract-ocr/tesseract).

Note the installation path as it will be needed in the code.
## Code Explanation
1. Import Libraries
The necessary libraries for capturing images, processing images, and handling CSV files are imported.
```
import cv2 as cv
from PIL import Image
from pytesseract import pytesseract
import csv
```
2. Image Capture
Open Webcam: Opens the default webcam (cv.VideoCapture(0)).
Capture Image: Continuously captures frames until the 'q' key is pressed.
Save Image: The captured frame is saved to the specified imgpath.
```
imgpath = r'C:\path'#path to store the image captured
capture = cv.VideoCapture(0)
while True:
    boolean, img = capture.read()
    cv.imshow('Text detection', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.imwrite(imgpath, img)
        break
capture.release()
cv.destroyAllWindows()
```
3. Text Extraction
Tesseract Configuration: Sets the path to the Tesseract-OCR executable.
Extract Text: Reads the image file and extracts text using Tesseract-OCR.
Print Extracted Text: Displays the extracted vehicle number.
```
def tessract():
    path_to_tessract = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #path where the tesseract file is stored
    pytesseract.tesseract_cmd = path_to_tessract
    text = pytesseract.image_to_string(Image.open(imgpath))
    
    return text[:-1].strip()

vehi_num = tessract()
print(vehi_num)
```
4. CSV File Lookup
Open CSV File: Reads the CSV file containing vehicle details.
Match Vehicle Number: Compares each row's vehicle number with the extracted text. If a match is found, the details are printed.
```
with open(r"C:\vehicle_details") as vehicle_det:
    vehicle_details_data = csv.reader(vehicle_det)
    next(vehicle_details_data)
    for row in vehicle_details_data:
        if row[0].strip() == vehi_num.strip():
            print("Vehicle Details\n")
            print("Vehicle Number :%s \nMotorist Name : %s \nAmount : %s" % (row[0], row[1], row[2]))
            break
```

