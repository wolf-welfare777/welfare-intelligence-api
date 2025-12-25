      
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

@app.get("/cyber", response_class=HTMLResponse)
async def hacker_dashboard():
    return "<h1>WELCOME TO C4ar4k-X DASHBOARD</h1><p>Tool is Live!</p>"

@app.get("/osint/{username}")
async def osint_tool(username: str):
    return {"target": username, "status": "active"}