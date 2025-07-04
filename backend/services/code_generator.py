from services.watsonx_service import call_watsonx

def generate_code(prompt):
    return call_watsonx(f"Generate Python code for: {prompt}")

def generate_tests(code):
    return call_watsonx(f"Write test cases for this code using unittest:{code}")
