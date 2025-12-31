import asyncio
import json
import httpx
import random
import string
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# --- CONFIG ---
TOKEN_A = "8488837085:AAGD9g2k_rT_i046HD3q3vBaKWguR18QFiM" # Bot 2 (Finance)
TOKEN_B = "8369647120:AAE0S7oP9s2hhqMh4b3bGFvKtJaRfIzdgJE" # Bot 1 (Scanner)
ADMIN_USER_ID = "7856837434"
UPI_ID = "charak777@ybl"

def generate_key():
    return "CHX-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

async def send_msg(token, chat_id, text, markup=None):
    async with httpx.AsyncClient() as client:
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        if markup: payload["reply_markup"] = markup
        await client.post(f"https://api.telegram.org/bot{token}/sendMessage", json=payload)

# --- BOT B LOGIC (Gatekeeper) ---
@app.post("/webhook_b")
async def scanner_bot(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            msg = "🛡 *Charak-X OSINT System Active*\nJoin our channel to unlock the scanner."
            markup = {"inline_keyboard": [[{"text": "📢 Join Channel", "url": "https://t.me/YourChannel"}], [{"text": "✅ Joined", "callback_data": "menu"}]]}
            await send_msg(TOKEN_B, chat_id, msg, markup)
    return {"ok": True}

# --- BOT A LOGIC (Finance) ---
@app.post("/webhook_a")
async def finance_bot(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_text = data["message"].get("text", "")
        if user_text == "/start":
            pay_msg = f"⚡ *Charak-X Premium*\nPlan: ₹19 / ₹299 / ₹699\nUPI: {UPI_ID}\nSend Screenshot/TXN ID after payment."
            await send_msg(TOKEN_A, chat_id, pay_msg)
        elif user_text.startswith("/approve"):
            if str(chat_id) == ADMIN_USER_ID:
                target = user_text.split(" ")[1]
                key = generate_key()
                await send_msg(TOKEN_A, target, f"✅ Verified! Your Key: {key}")
    return {"ok": True}

# --- WEBSITE ---
@app.get("/", response_class=HTMLResponse)
async def home():
    return "<html><body style='background:black;color:#0f0;text-align:center;'><h1>CHARAK-X OSINT</h1><a href='https://t.me/C4ar4kX_Bot' style='color:#0f0;'>ENTER SYSTEM</a></body></html>"