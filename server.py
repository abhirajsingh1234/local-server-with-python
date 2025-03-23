from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class UserRequest(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/execute")
def execute():
    return {"message": "Hyy myy name is Abhiraj Singh"}

@app.post("/greet")
def greet_user(user: UserRequest):
    if not user.name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    return {"message": f"Hello, {user.name}!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
