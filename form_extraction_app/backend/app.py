from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from ocr import run_ocr
from llm_extractor import extract_with_llm
from config import APP_NAME, APP_VERSION

app = FastAPI(title=APP_NAME, version=APP_VERSION)

@app.post("/extract")
async def extract_form(file: UploadFile = File(...)):
    """
    Accepts a scanned form image or PDF,
    extracts text using OCR,
    sends text to LLM,
    returns structured JSON.
    """
    file_bytes = await file.read()
    ocr_text = run_ocr(file_bytes)
    extracted_data = extract_with_llm(ocr_text)
    return JSONResponse(content=extracted_data)
