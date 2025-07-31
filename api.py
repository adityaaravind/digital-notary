from fastapi import FastAPI, UploadFile, Form
from blockchain import Blockchain
from auth import authenticate_user
from crypto import sign_data
import hashlib

app = FastAPI()
bc = Blockchain()

@app.post("/notarize")
async def notarize(file: UploadFile, username: str = Form(), password: str = Form()):
    if not authenticate_user(username, password):
        return {"error": "Unauthorized"}

    content = (await file.read()).decode()
    file_hash = hashlib.sha256(content.encode()).hexdigest()
    signature = sign_data(username, file_hash)
    block = bc.add_block(file_hash)
    return {"message": "Notarized", "block": block.to_dict(), "signature": signature}