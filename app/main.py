from fastapi import FastAPI
from .gigachat_api.api import request_to_giga
from .models.text_model import Text

app = FastAPI()


@app.post('/retelling/')
async def get_retelling(text: Text):
    return {'result': request_to_giga(text.text)}
