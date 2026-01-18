📄 Universal Document Text Extractor

A Streamlit-based application that performs OCR + LLM-powered structured data extraction from any type of document (PDFs or images), such as:

Banking & KYC forms

Government IDs

Education & employment forms

Insurance & utility documents

Unknown or mixed-format forms

The system converts unstructured OCR text into strict, validated JSON output with high reliability.

✨ Key Features

📤 Upload PDF / Image documents

🔍 OCR using Tesseract

🧠 Structured extraction using Cerebras LLM (LLaMA 3.1)

📊 Auto-detected document type

🧾 Strict JSON output (no hallucinations)

⬇️ Downloadable JSON extraction report

🖥️ Clean Streamlit UI

🧪 Hard JSON parsing for reliability

🏗️ Project Structure
document-text-extractor/
│
├── app.py                     # Streamlit UI
├── extractor.py               # OCR + LLM extraction logic
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore
│
├── temp/                      # Temporarily uploaded files
└── output/
    └── extracted_report.json  # Final downloadable output

⚙️ System Requirements
Operating System

Windows / Linux / macOS

System Dependencies (Mandatory)
Windows

Install Tesseract OCR (UB Mannheim build)
👉 https://github.com/UB-Mannheim/tesseract/wiki

Make sure:

✔ “Add Tesseract to PATH” is checked

Installed at:

C:\Program Files\Tesseract-OCR\

Linux
sudo apt update
sudo apt install -y tesseract-ocr poppler-utils

macOS
brew install tesseract poppler

🐍 Python Setup
1️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate    # Linux / macOS

2️⃣ Install Python Dependencies
pip install -r requirements.txt

🔑 API Key Requirement

This project uses Cerebras Cloud SDK.

You will need a Cerebras API Key, which is entered securely in the UI at runtime.

No API keys are hardcoded in the application.

▶️ Running the Application

From the project root:

streamlit run app.py


Then open your browser at:

http://localhost:8501

🧑‍💻 How to Use

Enter your Cerebras API Key

Upload a document (PDF / JPG / PNG)

Click “Extract Information”

View structured JSON output

Download the final extraction report as a .json file

📤 Output Format (Sample)
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

🛡️ Reliability Guarantees

Hard JSON parsing (json.loads)

Temperature set to 0.0 (deterministic output)

No hallucinated fields

Unrecognized fields safely placed in additional_fields

Extraction confidence score included

🚀 Use Cases

Banking automation

KYC document processing

Enterprise form digitization

Hackathons & POCs

Resume / application form parsing

AI-powered document intelligence systems

🔮 Future Enhancements

Batch document upload

CSV / PDF report export

OCR quality tuning controls

Multi-language OCR support

Dockerized deployment

Cloud deployment (AWS / GCP)

👤 Author

Developed as part of a hackathon-grade document intelligence solution
by Srikar

⭐ Final Note

This project prioritizes functionality, stability, and correctness over unnecessary abstractions — making it ideal for real-world usage, demos, and evaluations.
