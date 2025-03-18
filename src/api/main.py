from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageResponse(BaseModel):
    message: str = "Phishing Detection API Running!"

@app.get("/", response_model=MessageResponse)
def home():
    return MessageResponse()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8080, reload=True)
