import PyPDF2
from fastapi import HTTPException
from PyPDF2.errors import PdfReadError


async def read_pdf_file(pdf_file):
    try:
        return PyPDF2.PdfReader(pdf_file)
    except PdfReadError:
        raise HTTPException(
            detail="Provide a valid PDF file",
            status_code=400
        )
