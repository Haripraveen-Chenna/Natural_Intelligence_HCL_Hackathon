import pytesseract
from PIL import Image
import io
from config import OCR_LANGUAGE

def run_ocr(file_bytes: bytes) -> str:
    """
    Converts image bytes to raw text using OCR.
    """
    image = Image.open(io.BytesIO(file_bytes))
    text = pytesseract.image_to_string(image, lang=OCR_LANGUAGE)
    return text
