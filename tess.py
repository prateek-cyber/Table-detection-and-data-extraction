import cv2 
import pytesseract

img = cv2.imread('2.jpg')

# Adding custom options
# custom_config = r'--oem 3 --psm 6'
tessdata_dir_config = r'--tessdata-dir "/usr/local/Cellar/tesseract/5.2.0/share/tessdata"'

text = pytesseract.image_to_string(img, config=tessdata_dir_config)
print(text)