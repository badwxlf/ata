import pytesseract as ocr

ocr.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

from PIL import Image
    
phrase = ocr.image_to_string(Image.open('C:\\Users\\rqa\\Desktop\\Rodrigo\\projetinho_map_geo\\ocrs\\ata 3 - Copy - Copy(melhor res).jpeg'), lang='por')

print(phrase)   
