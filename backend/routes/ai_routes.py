from fastapi import APIRouter, UploadFile, File, Form
from services import ai_story_generator, code_generator, bug_resolver, doc_generator

router = APIRouter()

@router.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):
    text = ai_story_generator.extract_text_from_pdf(file)
    result = ai_story_generator.classify_sdlc_phases(text)
    return {"classified_tasks": result}

@router.post("/generate-code")
def generate_code(prompt: str = Form(...)):
    return {"code": code_generator.generate_code(prompt)}

@router.post("/generate-tests")
def generate_tests(code: str = Form(...)):
    return {"tests": code_generator.generate_tests(code)}

@router.post("/fix-bugs")
def fix_bugs(code: str = Form(...)):
    return {"fixed_code": bug_resolver.fix_code(code)}

@router.post("/summarize-code")
def summarize_code(code: str = Form(...)):
    return {"summary": doc_generator.summarize_code(code)}