from fastapi import FastAPI, Request, Form

from fastapi.responses import HTMLResponse, StreamingResponse

from fastapi.responses import HTMLResponse

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from pydantic import BaseModel
import os

from bot import getAnswer, getAnswerStream # Import the llm, prompt, and chain from bot.py

from bot import getAnswer # Import the llm, prompt, and chain from bot.py


load_dotenv()
chatbot_db_url = os.getenv("CHATBOT_DB_URL")
chatbot_db_token = os.getenv("CHATBOT_DB_TOKEN")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

chat_history = []  
@app.get("/", response_class=HTMLResponse)
async def bot_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"chat_history": chat_history})

@app.post("/",response_class=HTMLResponse)
async def user_chat(request: Request, user_input: str = Form(...)):
    
    bot_response = getAnswer(user_input)
    chat_history.append({"user": user_input, "bot": bot_response})
    return templates.TemplateResponse("index.html", {"request": request, "chat_history": chat_history})



@app.post("/stream")
async def stream_chat(user_input: str = Form(...)):
    def event_generator():
        full_response = ""
        for chunk in getAnswerStream(user_input):
            full_response += chunk
            yield chunk
        chat_history.append({"user": user_input, "bot": full_response})

    return StreamingResponse(event_generator(), media_type="text/plain")


        
    
    

