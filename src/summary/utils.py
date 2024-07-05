import PyPDF2
from fastapi import HTTPException
from PyPDF2.errors import PdfReadError
from src.summary.config import client


async def read_pdf_file(pdf_file):
    try:
        return PyPDF2.PdfReader(pdf_file)
    except PdfReadError:
        raise HTTPException(
            detail="Provide a valid PDF file",
            status_code=400
        )


async def summarization_text(text: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are helpful research assistant, "
                           "that helps people to summarize documents",
            },
            {
                "role": "user",
                "content": f"Please summarize this : ({text})",
            }
        ]
    )
    return response.choices[0].message.content
