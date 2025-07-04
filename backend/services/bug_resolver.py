from services.watsonx_service import call_watsonx

def fix_code(code):
    return call_watsonx(f"Fix the following buggy code:{code}")