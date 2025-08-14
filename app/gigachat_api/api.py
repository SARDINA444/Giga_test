from langchain_community.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
env_dir = os.path.join(current_dir, '...', '.env')

load_dotenv()

key = os.getenv("GIGA_KEY")

giga = GigaChat(
    credentials=key,
    verify_ssl_certs=False)

system_msg = SystemMessage(content='Тебе необходимо проанализировать текст и кратко пересказать его')


async def request_to_giga(text):
    result = await giga.agenerate([[system_msg, HumanMessage(content=text)]])
    return result
