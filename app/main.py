import os

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

from langchain_core.messages import HumanMessage

from dotenv import load_dotenv

from app.agent import agent

from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import HTMLResponse



load_dotenv()


app = FastAPI(

    title="AlgoRhythm Agent API",

    description="A content creator agent powered by LangGraph",

    version="1.0.0"

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tighten this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):

    message: str


class ChatResponse(BaseModel):

    response: str


@app.get("/health")

async def health_check():

    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)

async def chat(request: ChatRequest):

    try:

        result = agent.invoke({

            "messages": [HumanMessage(content=request.message)]

        })

        return ChatResponse(response=result["messages"][-1].content)

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("index.html") as f:
        return f.read()
