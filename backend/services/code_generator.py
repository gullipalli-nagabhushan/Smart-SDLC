from services.watsonx_service import call_watsonx

def generate_code(prompt):
    return call_watsonx(f"Generate  code for: {prompt} in  user specified language or if not specified then in python")

def generate_tests(code):
    return call_watsonx(f"Write test cases for this code using unittest:{code}")
