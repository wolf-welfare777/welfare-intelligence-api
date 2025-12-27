import asyncio
import json
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# === CONFIG ===
TOKEN_A = "8488837085:AAGD9g2k_rT_i046HD3q3vBaKWguR18QFiM" # Finance (@C4ar4k2_Bot)
TOKEN_B = "8369647120:AAE0S7oP9s2hhqMh4b3bGFvKtJaRfIzdgJE" # Scanner (@C4ar4kX_Bot)
ADMIN_USER = "Charak_777"
UPI_ID = "charak777@ybl"
LEAK_API_TOKEN = "NDiqpXCQOnVgfeP5XYEXkt6bGNOYCgGo"
LEAK_URL = "https://leakosintapi.com/"

# Helper for Masking
def mask_data(val):
    val = str(val)
    return val[:2] + "*" if len(val) > 2 else "*"

async def send_msg(token, chat_id, text, markup=None):
    async with httpx.AsyncClient() as client:
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        if markup: payload["reply_markup"] = markup
        await client.post(f"https://api.telegram.org/bot{token}/sendMessage", json=payload)

# === BOT A (FINANCE) ===
@app.post("/webhook_a")
async def finance(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        msg = ("🏛️ C4-X SECURE ACCESS\n---\nReport ready hai. Unlock karne ke liye ₹19 pay karein.")
        markup = {"inline_keyboard": [
            [{"text": "💳 Pay via PhonePe/GPay", "url": f"upi://pay?pa={UPI_ID}&pn=C4X_NODE&am=19&cu=INR"}],
            [{"text": "🛰️ Back to Scanner", "url": "https://t.me/C4ar4kX_Bot"}]
        ]}
        await send_msg(TOKEN_A, chat_id, msg, markup)
    return {"ok": True}

# === BOT B (SCANNER) ===
@app.post("/webhook_b")
async def scanner(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text.isdigit():
            await send_msg(TOKEN_B, chat_id, "🛰️ Searching...")
            async with httpx.AsyncClient() as client:
                res = await client.post(LEAK_URL, json={"token": LEAK_API_TOKEN, "request": text, "limit": 1})
                # Teaser Logic here...
                teaser = "🎯 Target Found!\nName: As**** (Locked)\n"
                markup = {"inline_keyboard": [[{"text": "🔓 Unlock Now", "url": "https://t.me/C4ar4k2_Bot"}]]}
                await send_msg(TOKEN_B, chat_id, teaser, markup)
    return {"ok": True}

# === WEB UI (MATRIX + NEWS) ===
@app.get("/", response_class=HTMLResponse)
async def home():
    return "<html><body style='background:black;color:green;'><h1>Matrix System Active</h1><marquee>🚨 NEWS: SYSTEM STABLE...</marquee></body></html>"

@app.get("/setup")
async def setup():
    base = "https://welfare-intelligence-api.onrender.com"
    async with httpx.AsyncClient() as client:
        await client.get(f"https://api.telegram.org/bot{TOKEN_A}/setWebhook?url={base}/webhook_a")
        await client.get(f"https://api.telegram.org/bot{TOKEN_B}/setWebhook?url={base}/webhook_b")
    return {"status": "Webhooks Linked!"}