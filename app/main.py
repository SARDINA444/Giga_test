from fastapi import FastAPI
from .gigachat_api.api import request_to_giga
from .models.text_model import Text
import asyncio

app = FastAPI()


@app.post('/retelling/')
async def get_retelling(text: Text):
    result = await request_to_giga(text.text)
    return {'result': result.generations[0][0].text}
