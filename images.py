from PIL import Image
from pytesseract import pytesseract
import enum

class Language(enum.Enum):
    ENG = 'eng'

class ImageReader:

    def __init__(self):
        windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = windows_path
        print('Running...')

    def extract_text(self, image: str, lang: Language) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang.value)
        return extracted_text

if __name__ == '__main__':
    ir = ImageReader()
    text = ir.extract_text('images/asd.png', Language.ENG)
    processed_text = ' '.join(text.split())
    print(processed_text)