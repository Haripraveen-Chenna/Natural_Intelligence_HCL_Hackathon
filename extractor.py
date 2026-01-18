import json
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from cerebras.cloud.sdk import Cerebras

MODEL_NAME = "llama3.1-8b"

def extract_text(file_path):
    text = ""
    if file_path.lower().endswith(".pdf"):
        pages = convert_from_path(file_path)
        for page in pages:
            text += pytesseract.image_to_string(page) + "\n"
    else:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
    return text.strip()


def run_extraction(file_path, cerebras_api_key):
    client = Cerebras(api_key=cerebras_api_key)

    ocr_text = extract_text(file_path)

    prompt = f"""
You are a document understanding system that outputs STRICT JSON.

TASK:
Analyze the OCR text of a filled form or document and extract structured information.

The document can be of ANY type.

OUTPUT RULES (STRICT):
- Output ONLY valid JSON
- NO explanations
- NO markdown
- NO code blocks
- NO extra text
- Use null if a field is not present
- Do NOT hallucinate values

JSON SCHEMA:
{{
  "document_type": string,
  "person_details": {{
    "full_name": string | null,
    "date_of_birth": string | null,
    "gender": string | null
  }},
  "contact_details": {{
    "address": string | null,
    "phone_number": string | null,
    "email": string | null
  }},
  "identifiers": {{
    "id_number": string | null,
    "registration_number": string | null,
    "account_number": string | null
  }},
  "transaction_details": {{
    "transaction_amount": number | null,
    "transaction_type": string | null
  }},
  "institution_or_organization": string | null,
  "additional_fields": {{
    "field_name": "field_value"
  }},
  "extraction_confidence": number
}}

OCR TEXT:
\"\"\"
{ocr_text}
\"\"\"
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You must output ONLY valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )

    raw_output = response.choices[0].message.content.strip()
    structured_data = json.loads(raw_output)

    return structured_data
