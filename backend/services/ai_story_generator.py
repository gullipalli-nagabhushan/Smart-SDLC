import fitz
from services.watsonx_service import call_watsonx

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = " ".join([page.get_text() for page in doc])
    return text

def classify_sdlc_phases(text):
    prompt = f"Classify each sentence into SDLC phases:\n{text}"
    return call_watsonx(prompt)
