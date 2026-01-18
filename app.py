import streamlit as st
import json
import os
from extractor import run_extraction

st.set_page_config(page_title="Document Text Extractor", layout="centered")

st.title("📄 Universal Document Text Extractor")
st.write("Upload any document (PDF/Image) → Extract structured JSON")

api_key = st.text_input("Enter Cerebras API Key", type="password")

uploaded_file = st.file_uploader("Upload Document", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file and api_key:
    os.makedirs("temp", exist_ok=True)
    file_path = f"temp/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("🔍 Extract Information"):
        with st.spinner("Processing document..."):
            try:
                result = run_extraction(file_path, api_key)

                st.success("Extraction completed")

                st.json(result)

                os.makedirs("output", exist_ok=True)
                output_path = "output/extracted_report.json"

                with open(output_path, "w") as f:
                    json.dump(result, f, indent=4)

                with open(output_path, "r") as f:
                    st.download_button(
                        label="⬇️ Download JSON Report",
                        data=f,
                        file_name="extracted_report.json",
                        mime="application/json"
                    )

            except Exception as e:
                st.error(f"Error: {e}")
