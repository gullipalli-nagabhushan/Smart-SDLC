import fitz
from services.watsonx_service import call_watsonx

def extract_text_from_pdf(file_bytes: bytes):
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = " ".join([page.get_text() for page in doc])
        doc.close()
        return text.strip() or "⚠️ No text found."
    except Exception as e:
        return f"❌ PDF processing failed: {str(e)}"



def classify_sdlc_phases(text):
    prompt = (
        "You are an AI SDLC assistant.\n"
        "Task: Classify the following text into respective SDLC phases "
        "(Requirements, Design, Implementation, Testing, Deployment, Maintenance).\n\n"
        f"Text:\n{text}\n\n"
        "Output format: List each sentence and its corresponding SDLC phase."
    )
    return call_watsonx(prompt)
