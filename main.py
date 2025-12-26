import os
import json
import asyncio
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# === CONFIG (SAB KUCH VERIFIED HAI) ===
TOKEN = "8369647120:AAE0S7oP9s2hhqMh4b3bGFvKtJaRfIzdgJE"
BOT_USERNAME = "C4ar4kX_Bot"
ADMIN_USER = "Charak_777" 
UPI_ID = "charak777@ybl"
LEAK_API_TOKEN = "NDiqpXCQOnVgfeP5XYEXkt6bGNOYCgGo" # Naveen's Power API
LEAK_URL = "https://leakosintapi.com/"

# === BUTTONS SYSTEM (PROFESSIONAL LOOK) ===
def get_combined_buttons():
    return {
        "inline_keyboard": [
            [{"text": "💳 Pay for Trial (₹19 Only)", "url": f"https://upilinks.in/payment-button?upi={UPI_ID}&amt=19"}],
            [{"text": "📞 Contact Admin / Send SS", "url": f"https://t.me/{ADMIN_USER}"}],
            [{"text": "🔑 Request Activation Key", "url": f"https://t.me/{ADMIN_USER}"}],
            [
                {"text": "📢 Telegram", "url": "https://t.me/C4AR4K_X"},
                {"text": "📸 Instagram", "url": f"https://instagram.com/{ADMIN_USER}"}
            ]
        ]
    }

@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data.get("message", {}).get("text", "").strip()
        
        async with httpx.AsyncClient() as client:
            if text == "/start":
                welcome = (
                    f"🛰️ C4AR4K-X GLOBAL OSINT TERMINAL\n"
                    f"------------------------------------------\n"
                    f"🌐 FOLLOW US: [Telegram](https://t.me/C4AR4K_X) | [Instagram](https://instagram.com/{ADMIN_USER})\n"
                    f"🛡️ ENCRYPTION: AES-256 (Proxy Earth Active)\n"
                    f"------------------------------------------\n\n"
                    f"⚡ INVESTIGATION PLANS:\n"
                    f"🔹 TRIAL: ₹19 (2 Real Scans)\n"
                    f"🔹 MONTHLY: ₹199 (Unlimited)\n"
                    f"🔹 LIFETIME: ₹699 (Permanent Access)\n\n"
                    f"Target ka Phone Number ya Email bhejien scan karne ke liye."
                )
                await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                 json={"chat_id": chat_id, "text": welcome, "parse_mode": "Markdown", "disable_web_page_preview": True, "reply_markup": get_combined_buttons()})
            
            elif text.isdigit() or "@" in text:
                # Scary Animation Sequence (Dark Web Simulation)
                for s in ["🛰️ Connecting to Proxy Earth Node-01...", "⛓️ Scraping Dark-Web SQL Layers...", "🎯 Target Identified! Fetching Data..."]:
                    await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": s})
                    await asyncio.sleep(1.2)

                # NAVEEN'S REAL API CALL
                payload = {"token": LEAK_API_TOKEN, "request": text, "limit": 5, "lang": "en"}
                try:
                    api_res = await client.post(LEAK_URL, json=payload, timeout=30.0)
                    res = api_res.json()
                    
                    if res.get("List") and res["List"] != {}:
                        for db, db_data in res["List"].items():
                            for entry in db_data["Data"]:
                                report = f"🛰️ DATA FOUND IN: {db}\n---\njs\n{json.dumps(entry, indent=2)}\n"
                                await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": report, "parse_mode": "Markdown"})
                        
                        await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                         json={"chat_id": chat_id, "text": "✅ Social Media IDs & Full Report Locked.\nPay ₹199 to unlock all sensitive data and high-res pics.", "reply_markup": get_combined_buttons()})
                    else:
                        await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": "❌ No data found in our 2025 Deep-Web records."})
                except Exception:
                    await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": "⚠️ Proxy Node timeout. Try again later."})

    return {"status": "ok"}

# === WEB TERMINAL (MATRIX EFFECT + IP TRACKER) ===
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    ip = request.headers.get("x-forwarded-for") or request.client.host
    return f"""
    <html><body style="background:#000;color:#0f0;text-align:center;font-family:monospace;overflow:hidden;margin:0;">
        <canvas id="m"></canvas>
        <div style="position:absolute;width:100%;top:20%;z-index:1;">
            <h1 style="text-shadow:0 0 10px #0f0;font-size:3em;">🛰️ C4AR4K-X OSINT</h1>
            <div style="border:1px solid #0f0;padding:20px;display:inline-block;background:rgba(0,0,0,0.85);">
                <p style="color:red; font-weight:bold;">[!] YOUR IP: {ip}</p>
                <p>STATUS: SYSTEM LOGGING ACTIVE | ACCESS: LOGGED</p>
            </div><br><br>
            <a href="https://t.me/{BOT_USERNAME}" style="background:#0f0;color:#000;padding:20px 40px;text-decoration:none;font-weight:bold;box-shadow:0 0 20px #0f0;border-radius:5px;">🚀 LAUNCH OSINT SCANNER</a>
        </div>
        <script>
            const c=document.getElementById('m');const x=c.getContext('2d');
            c.width=window.innerWidth;c.height=window.innerHeight;
            const d=Array(Math.floor(c.width/16)).fill(1);
            setInterval(()=>{{
                x.fillStyle="rgba(0,0,0,0.05)";x.fillRect(0,0,c.width,c.height);
                x.fillStyle="#0f0";d.forEach((y,i)=>{{
                    x.fillText(String.fromCharCode(48+Math.random()*70),i*16,y*16);
                    if(y*16>c.height&&Math.random()>0.95)d[i]=0;d[i]++;
                }});
            }},35);
        </script>
    </body></html>
    """

@app.get("/set-webhook")
async def set_webhook():
    webhook_url = "https://welfare-intelligence-api.onrender.com/webhook"
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={webhook_url}")
        return r.json()