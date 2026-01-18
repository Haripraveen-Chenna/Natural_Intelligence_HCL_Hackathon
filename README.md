# 📄 Universal Document Text Extractor

A Streamlit-based application that performs OCR and LLM-powered structured data extraction from any type of document (PDFs or images).

Supported document types include:
•⁠  ⁠Banking / KYC / Financial forms
•⁠  ⁠Government & Identity documents
•⁠  ⁠Education & Employment forms
•⁠  ⁠Insurance & Utility documents
•⁠  ⁠Unknown or mixed-format documents

---

## ✨ Features

•⁠  ⁠Upload PDF or image documents  
•⁠  ⁠OCR using Tesseract  
•⁠  ⁠Structured data extraction using Cerebras LLM (LLaMA 3.1)  
•⁠  ⁠Automatic document type inference  
•⁠  ⁠Strict JSON output (no hallucinations)  
•⁠  ⁠Downloadable JSON extraction report  
•⁠  ⁠Clean Streamlit UI  
•⁠  ⁠Deterministic output (temperature = 0.0)  

---

## 📁 Project Structure

document-text-extractor/  
├── app.py  
├── extractor.py  
├── requirements.txt  
├── README.md  
├── .gitignore  
├── temp/  
└── output/  
  └── extracted_report.json  

---

## ⚙️ System Requirements

### Operating System
•⁠  ⁠Windows / Linux / macOS

### System Dependencies

#### Windows
Install Tesseract OCR (UB Mannheim build):  
https://github.com/UB-Mannheim/tesseract/wiki  

During installation:
•⁠  ⁠Check “Add Tesseract to PATH”
•⁠  ⁠Default install path:  
  C:\Program Files\Tesseract-OCR\

#### Linux
Run:  
sudo apt update  
sudo apt install -y tesseract-ocr poppler-utils  

#### macOS
Run:  
brew install tesseract poppler  

---

## 🐍 Python Setup

### Create Virtual Environment (Recommended)

Run:  
python -m venv venv  

Activate:  
Windows → venv\Scripts\activate  
Linux/macOS → source venv/bin/activate  

---

### Install Dependencies

Run:  
pip install -r requirements.txt  

---

## 🔑 API Key

This project uses the Cerebras Cloud SDK.

You will need a valid Cerebras API key.  
The API key is entered securely through the Streamlit UI at runtime.  
No API keys are hardcoded in the source code.

---

## ▶️ Run the Application

Run:  
streamlit run app.py  

Then open your browser at:  
http://localhost:8501  

---

## 🧑‍💻 Usage Instructions

1.⁠ ⁠Enter your Cerebras API key  
2.⁠ ⁠Upload a document (PDF / JPG / PNG)  
3.⁠ ⁠Click *Extract Information*  
4.⁠ ⁠View the structured JSON output  
5.⁠ ⁠Download the JSON extraction report  

---

## 📤 Output Format (Example)

Example JSON output:

{
  "document_type": "banking",
  "person_details": {
    "full_name": "John Doe",
    "date_of_birth": "1995-04-12",
    "gender": "Male"
  },
  "contact_details": {
    "address": "Bangalore, India",
    "phone_number": "9876543210",
    "email": null
  },
  "identifiers": {
    "id_number": null,
    "registration_number": null,
    "account_number": "1234567890"
  },
  "transaction_details": {
    "transaction_amount": null,
    "transaction_type": null
  },
  "institution_or_organization": "XYZ Bank",
  "additional_fields": {},
  "extraction_confidence": 0.89
}

---

## 🛡️ Reliability

•⁠  ⁠Hard JSON parsing using json.loads  
•⁠  ⁠Deterministic LLM output  
•⁠  ⁠No hallucinated values  
•⁠  ⁠Unrecognized fields stored safely in additional_fields  
•⁠  ⁠Confidence score included for every extraction  

---

## 🚀 Use Cases

•⁠  ⁠Document digitization  
•⁠  ⁠Banking and KYC automation  
•⁠  ⁠Form processing systems  
•⁠  ⁠Enterprise document intelligence  
•⁠  ⁠Hackathons and proof-of-concepts  

---
