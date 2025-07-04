from services.watsonx_service import call_watsonx

def summarize_code(code):
    return call_watsonx(f"Summarize this Python code:{code}")