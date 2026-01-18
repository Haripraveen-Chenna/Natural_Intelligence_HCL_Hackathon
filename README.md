# Natural_Intelligence_HCL_Hackathon
# Information Extraction from Scanned User-Filled Forms

## Project Overview

**Name:** Information Extraction from Scanned User-Filled Forms

**Domain:**
- Document Processing
- OCR
- Information Extraction
- Automation

---

## Problem Statement

Many organizations rely on scanned user-filled forms for onboarding and operational workflows. These forms often contain handwritten or printed text, varying layouts, and low-quality scans. Manual data entry from such forms is slow, error-prone, and costly.

**Objective:** Build an automated system that extracts structured information from scanned forms and outputs it in a machine-readable JSON format.

---

## Solution Overview

**Approach:** End-to-end pipeline-based design

**Capabilities:**
- Accept scanned images and PDFs
- Extract text using OCR
- Identify key fields
- Validate and normalize data
- Output structured JSON

---

## Architecture

**Design Style:** Modular and extensible

**Processing Flow:**
1. User Upload
2. Document Preprocessing
3. OCR Text Extraction
4. Field Extraction
5. Validation and Normalization
6. Structured JSON Output

---

## Components

### 1. Input Layer
Simple web interface for uploading scanned images or PDFs.


### 2. Preprocessing
**Responsibilities:**
- Noise reduction
- Deskewing
- Orientation correction
- Resolution normalization

**Purpose:** Improve OCR accuracy

### 3. OCR Engine
Converts scanned documents into raw text.

**Technology:** Pretrained OCR engines (e.g., Tesseract)


### 4. Field Extraction
**Target Fields:**
- Name
- Date of Birth
- Phone Number
- Address
- Form Type

**Approach:** LLM-based semantic extraction


### 5. Validation and Normalization
**Functions:**
- Date format standardization
- Phone number validation
- Address cleanup
- Confidence score calculation


### 6. Output
**Format:** JSON

**Example Output:**
```json
{
  "name": "John Doe",
  "dob": "1992-07-14",
  "phone": "+1 234 567 890",
  "form_type": "banking_application",
  "extraction_confidence": 0.91
}
```

---

## Design Principles

- **Simplicity First:** Build a working solution before adding intelligence
- **Modular Architecture:** Each component is independent and replaceable
- **Pretrained Models:** Leverage existing OCR and LLMs
- **Scalable Design:** Supports future enhancements

---

## Training Strategy

The system uses pretrained OCR engines and optional pretrained LLMs. The focus is on pipeline orchestration.

**Techniques Used:**
- Zero-shot extraction
- Rule-based parsing
- Optional few-shot prompting

---

## Future Enhancements

### Extraction
- Layout-aware field detection
- Handwriting-optimized OCR
- LLM-based semantic understanding

### Validation
- Domain-specific rules
- Adaptive confidence scoring

### System
- Multi-form type support
- User feedback loop
- Enterprise system integration


# Hari Praveen – Backend Orchestrator	API & Pipeline	
- Implement app.py (FastAPI)
- Integrate OCR & LLM modules
- Handle file uploads
- Return JSON responses	Fully working API that connects all components
# Aravind siddhartha – LLM & Prompt Engineer	Intelligent Extraction
- Write prompt.py with instructions for LLM
- Implement llm_extractor.py using Hugging Face
- Ensure strict JSON output
- Optional: tune temperature / few-shot examples	Clean LLM-based extraction module that produces structured JSON
# Dhairyesh pande – OCR & Preprocessing	Text Extraction
- Implement ocr.py
- Preprocess images (deskew, denoise, resize)
- Handle multiple image/PDF formats
- Optional: confidence scoring / field highlighting	High-quality text extraction from forms for the LLM








---

# 🧠 What We Have Built (Big Picture)

We have built a **Form Extraction System** that can:

✅ Take **scanned forms / photos**
✅ Handle **printed text + handwriting + checkboxes**
✅ Convert the image into **raw text (OCR)**
✅ Send the text to an **LLM (Groq / LLaMA)**
✅ Extract **structured JSON data**
✅ Serve everything via a **FastAPI backend**
✅ Test it using **Swagger UI (`/docs`)**

---

# 🏗️ Architecture Overview

```
User uploads image
        ↓
FastAPI (/extract)
        ↓
OCR Pipeline (OpenCV + Tesseract)
        ↓
Cleaned & chunked text
        ↓
LLM (Groq / LLaMA)
        ↓
Structured JSON
        ↓
API response + saved output
```

---

# 📂 Project Structure (Why it looks like this)

```
form_extraction_app/
├── backend/
│   ├── app.py              ← API entry point
│   ├── ocr.py              ← Image → text (printed + handwritten)
│   ├── llm_extractor.py    ← Text → structured JSON (Groq)
│   ├── prompt.py           ← Prompt rules for the LLM
│   ├── schemas.py          ← Data validation (Pydantic)
│   ├── config.py           ← Environment & secrets
│   ├── report_generator.py ← (PDF later)
│   └── outputs/            ← Saved results
│
├── frontend/               ← UI (not active now)
├── venv/                   ← Python environment
```

---

# 🧾 What Happens When You Upload a File

## 1️⃣ FastAPI receives the image (`app.py`)

Endpoint:

```
POST /extract
```

What it does:

* Validates file type (`jpg/png`)
* Saves the image temporarily
* Calls OCR
* Calls LLM
* Validates output
* Returns JSON

This makes backend **clean, testable, and scalable**.

---

## 2️⃣ OCR Pipeline (This is the MOST important part)

### Why OCR is hard

Forms contain:

* Printed text
* Handwriting
* Checkboxes
* Noise (scans, shadows)

So you **combined tools** (this is smart):

### 🛠 Tools used

| Tool      | Purpose            |
| --------- | ------------------ |
| OpenCV    | Image cleaning     |
| Tesseract | Printed text       |
| EasyOCR   | Handwritten text   |
| Contours  | Checkbox detection |

### OCR flow

```
Image
 → grayscale
 → thresholding
 → morphology
 → printed OCR
 → handwritten OCR
 → checkbox detection
```

Final OCR output is **not just text**, but:

```json
{
  "printed_text": "...",
  "handwritten_text": "...",
  "checkboxes": [...],
  "layout_blocks": [...]
}
```

---

## 3️⃣ Prompt Engineering (prompt.py)

we forced the LLM to:

✔ Output **ONLY JSON**
✔ Use fixed fields
✔ Avoid explanations
✔ Give confidence score

This avoids:

* Markdown
* Hallucinations
* Random text

---

## 4️⃣ Token Chunking (Why this mattered)

OCR text can be **huge**.

LLMs have token limits → so you implemented:

```python
chunk_text(text, max_chars=3000)
```

This ensures:

* No request failure
* Works for large forms
* First valid chunk wins

---

## 5️⃣ LLM Layer (Groq)

we **correctly abandoned OpenAI & Cerebras** and switched to **Groq** because:

* Fast
* Free tier
* Open models
* REST-based

We now:

* Use environment variables
* Validate config strictly
* Fail safely (fallback JSON)

Even if Groq fails:

```json
{
  "name": "N/A",
  "confidence": 0.3
}
```
---

## 6️⃣ Config Management (This saved you)

### Why `config.py` matters

Instead of hardcoding:

* API keys
* Models
* Paths

You use:

```python
BaseSettings + env vars
```

This:

* Prevents leaks
* Makes deployment easy
* Catches mistakes early (`extra="forbid"`)

Your earlier errors were actually **good signs** — config validation was protecting you.

---

## 7️⃣ Why GPU warnings appeared (and why it’s OK)

You saw:

```
pin_memory not supported on MPS
```

This came from:

* Torch inside EasyOCR
* Apple Silicon fallback

You explicitly forced:

```bash
CUDA_VISIBLE_DEVICES=""
```

So:

* ❌ No GPU used
* ✅ CPU-only inference
* ✅ Stable
* ✅ Hackathon-safe

---

## 8️⃣ Swagger (`/docs`) = Your Testing Tool

We can now:

* Upload images
* See responses
* Validate schemas
* Debug fast

This replaces:

* Postman
* Curl
* Frontend debugging

For hackathons, **Swagger = gold**.

---

# 🎯 What We’ve Actually Achieved

You built:

✅ A **real document AI backend**
✅ OCR for handwriting + checkboxes
✅ LLM extraction with chunking
✅ Environment-safe configuration
✅ API with validation & fallbacks

---
