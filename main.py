import os
import json
import asyncio
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# ================= CONFIGURATION =================
TOKEN = "7757973795:AAEx_f7E6G9yV2yv_Xy0p6UshYlqG9N6l_M"
BOT_USERNAME = "C4ar4kX_Bot"
ADMIN_USER = "@Charak_777"
UPI_ID = "charak777@ybl"

# NAVEEN'S API (REAL POWER)
LEAK_API_TOKEN = "NDiqpXCQOnVgfeP5XYEXkt6bGNOYCgGo"
LEAK_URL = "https://leakosintapi.com/"

# ================= WELCOME UI =================
WELCOME_TEXT = f"""
🛰️ C4AR4K-X GLOBAL INTELLIGENCE 🛰️
------------------------------------------
🌐 NODE: Proxy Earth Active
🛡️ SYSTEM: Dark Web Scraper v4.5
------------------------------------------
Bhai, full investigation reports unlock karne ke liye apna plan choose karein:

⚡ STARTER: ₹19 (2 Scans - Trial)
📅 MONTHLY: ₹199 (Unlimited - 30 Days)
👑 LIFETIME: ₹699 (Permanent Access)

📌 Payment: {UPI_ID}
Screenshot {ADMIN_USER} ko bhejien.
------------------------------------------
"""

@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data.get("message", {}).get("text", "").strip()

        async with httpx.AsyncClient() as client:
            if text == "/start":
                await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                 json={"chat_id": chat_id, "text": WELCOME_TEXT, "parse_mode": "Markdown"})
            
            elif text.isdigit() or "@" in text:
                # 1. SCARY ANIMATIONS (Sanki XD Style)
                animations = [
                    "🛰️ Connecting to Proxy Earth Node...",
                    "⛓️ Decrypting Dark-Web SQL Layers... [45%]",
                    "🎯 Target Found! Scanning Social Media & Images..."
                ]
                for msg in animations:
                    await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": msg})
                    await asyncio.sleep(1.2)

                # 2. REAL SEARCH (Naveen API Logic)
                payload = {"token": LEAK_API_TOKEN, "request": text, "limit": 5, "lang": "en"}
                try:
                    api_res = await client.post(LEAK_URL, json=payload, timeout=30.0)
                    response = api_res.json()
                    
                    if response.get("List") and response["List"] != {}:
                        for db, db_data in response["List"].items():
                            for entry in db_data["Data"]:
                                js_data = json.dumps(entry, indent=2)
                                report = (
                                    f"🛰️ C4AR4K-X INTELLIGENCE REPORT\n"
                                    f"---------------------------------------\n"
                                    f"📂 Source: Proxy Earth / Dark Web Node\n"
                                    f"👤 Social Media: Identified\n"
                                    f"📸 Profile Pic: Found in Leak\n\n"
                                    f"js\n{js_data}\n"
                                )
                                await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                                 json={"chat_id": chat_id, "text": report, "parse_mode": "Markdown"})
                        
                        # 3. PAYMENT HOOK
                        await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                         json={"chat_id": chat_id, "text": f"✅ Social Media ID & High-Res Pics Locked. Pay ₹199 to {ADMIN_USER} to unlock full profile.", "parse_mode": "Markdown"})
                    else:
                        await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": "❌ No data found in Dark Web database."})
                except:
                    await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": "⚠️ Proxy Earth connection timeout. Try again."})
    return {"status": "ok"}

# ================= WEBSITE WITH IP TRACKER =================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user_ip = request.headers.get("x-forwarded-for") or request.client.host
    return f"""
    <html>
    <head><title>C4AR4K-X TERMINAL</title></head>
    <body style="background:#000;color:#0f0;text-align:center;font-family:monospace;padding:30px;">
        <h1 style="text-shadow: 0 0 10px #0f0;">🛰️ C4AR4K-X OSINT SYSTEM</h1>
        <div style="border:1px solid #0f0; padding:15px; display:inline-block; margin:20px;">
            <p style="color:red;">[!] WARNING: ACCESS LOGGED</p>
            <p>VISITOR IP: {user_ip}</p>
            <p>PROXY NODE: ACTIVE</p>
        </div><br>
        <iframe src="https://cybermap.kaspersky.com/en/widget/v2" width="90%" height="450px" style="border:1px solid #0f0;"></iframe><br><br>
        <a href="https://t.me/{BOT_USERNAME}" style="background:#0f0;color:#000;padding:20px 40px;text-decoration:none;font-weight:bold;box-shadow: 0 0 20px #0f0;">🚀 LAUNCH OSINT SCANNER</a>
    </body>
    </html>
    """

@app.get("/set-webhook")
async def set_webhook():
    webhook_url = "https://welfare-intelligence-api.onrender.com/webhook"
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={webhook_url}")
        return r.json()