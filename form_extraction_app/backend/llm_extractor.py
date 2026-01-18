import json
import requests
from config import HF_API_KEY, HF_MODEL, HF_TEMPERATURE, HF_MAX_NEW_TOKENS
from prompt import SYSTEM_PROMPT
from schemas import EXPECTED_JSON_SCHEMA

HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

def extract_with_llm(ocr_text: str) -> dict:
    """
    Sends OCR text to Hugging Face LLM and returns structured JSON.
    """
    payload = {
        "inputs": f"{SYSTEM_PROMPT}\nOCR TEXT:\n{ocr_text}\nReturn JSON only.",
        "parameters": {
            "max_new_tokens": HF_MAX_NEW_TOKENS,
            "temperature": HF_TEMPERATURE
        },
    }

    response = requests.post(HF_API_URL, headers=HEADERS, json=payload)
    try:
        raw_output = response.json()[0]["generated_text"]
        parsed_output = json.loads(raw_output)
    except (KeyError, json.JSONDecodeError, IndexError):
        parsed_output = EXPECTED_JSON_SCHEMA

    return parsed_output
