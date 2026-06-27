from fastapi import FastAPI, Body
from ollama import Client

client = Client(host="http://localhost:11434")

app = FastAPI()


@app.get("/hello")
def printHello():
    return {"hello": "world"}


@app.post("/chat")
def chat(message: str = Body(..., description="The Message")):
    response = client.chat(
        model="deepseek-r1:1.5b",
        messages=[
            {"role": "system", "content": "You are ai assistant name GETAA"},
            {"role": "user", "content": message},
        ],
        think=False,
    )

    return {"response": response.message.content}
