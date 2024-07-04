import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

client = AsyncOpenAI(api_key=os.environ['OPENAI_API_KEY'])


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


