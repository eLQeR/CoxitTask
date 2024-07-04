import io

from fastapi import APIRouter, UploadFile
from src.summary.config import summarization_text
from src.summary.utils import read_pdf_file

router = APIRouter()


@router.post("/summarize/")
async def get_summary_from_file(file: UploadFile):
    pdf_file = io.BytesIO(await file.read())
    pdf_reader = await read_pdf_file(pdf_file)

    text_pages = ""
    for page_num in range(len(pdf_reader.pages)):
        text_pages += pdf_reader.pages[page_num].extract_text()

    summary = await summarization_text(text_pages)
    return {"summary": summary}
