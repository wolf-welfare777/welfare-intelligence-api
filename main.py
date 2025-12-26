from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import httpx
import json

app = FastAPI()

# --- 🛠 CONFIGURATION (SAB KUCH FIX HAI) ---
BOT_TOKEN = "8369647120:AAE0S7oP9s2hhqMh4b3bGFvKtJaRfIzdgJE"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
LEAK_API_TOKEN = "NDiqpXCQOnVgfeP5XYEXkt6bGNOYCgGo"
ADMIN_ID = "7856837434"

# Payment Details
QR_URL = "https://files.catbox.moe/p88m0j.png" 
UPI_ID = "charak777@ybl"

# Temporary Database
users_db = {}

# --- 🎭 THE HACKER UI (MATRIX + CYBER SOUND) ---
HACKER_UI = """
<!DOCTYPE html>
<html>
<head>
    <title>C4ar4k-X OSINT SYSTEM</title>
    <style>
        body { background: black; color: #0f0; font-family: 'Courier New', monospace; margin: 0; overflow: hidden; display: flex; align-items: center; justify-content: center; height: 100vh; }
        .box { border: 2px solid #0f0; padding: 50px; background: rgba(0, 20, 0, 0.95); text-align: center; box-shadow: 0 0 50px #0f0; z-index: 10; border-radius: 20px; }
        h1 { font-size: 3.5rem; letter-spacing: 5px; text-shadow: 0 0 20px #0f0; margin: 0; }
        .status { color: #f00; font-weight: bold; animation: pulse 1s infinite; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
        canvas { position: fixed; top: 0; left: 0; opacity: 0.4; }
    </style>
</head>
<body>
    <canvas id="m"></canvas>
    <div class="box">
        <h1>C4AR4K-X OSINT</h1>
        <p class="status">POLICE & INVESTIGATION MODE: ACTIVE</p>
        <p style="color:white">Global Database & Social Media Link: OK</p>
        <hr style="border-color:#0f0">
        <p style="color:#888">Secure Connection: Encrypted</p>
    </div>
    <audio autoplay loop><source src="https://www.soundjay.com/mechanical/sounds/computer-processing-1.mp3" type="audio/mpeg"></audio>
    <script>
        const c = document.getElementById('m'), q = c.getContext('2d');
        c.width = window.innerWidth; c.height = window.innerHeight;
        const s = Array(256).join(1).split('');
        setInterval(() => {
            q.fillStyle = 'rgba(0,0,0,0.05)'; q.fillRect(0,0,c.width,c.height);
            q.fillStyle = '#0f0'; s.forEach((y, i) => {
                q.fillText(String.fromCharCode(33+Math.random()*94), i*10, y);
                s[i] = y > 758 + Math.random()*1e4 ? 0 : y + 10;
            });
        }, 33);
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home(): return HACKER_UI

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = str(data["message"]["chat"]["id"])
        text = data["message"].get("text", "").strip()
        user_info = data["message"].get("from", {})
        first_name = user_info.get("first_name", "Unknown")

        # 1. 📢 START & NOTIFICATION
        if text == "/start":
            # Admin Alert (Aapko message aayega)
            alert = f"🚨 *New Target Spotted!*\n👤 Name: {first_name}\n🆔 ID: {chat_id}\n🚀 Usne system start kiya hai."
            async with httpx.AsyncClient() as client:
                await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": ADMIN_ID, "text": alert, "parse_mode": "Markdown"})
            
            welcome = (
                f"🛡️ *C4ar4k-X OSINT Intelligence v5.0*\n\n"
                "Welcome Agent. This system is optimized for Scammer Identification.\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "🔍 *Investigation Powers:*\n"
                "• Full Name, Father Name & Address\n"
                "• Deep Data Leak History\n"
                "• All Social Media Linked Accounts\n"
                "• Alternative Number Detection\n\n"
                f"💳 *Activation Fee:* ₹19 ({UPI_ID})\n"
                "👉 *Admin:* @Charak_777"
            )
            async with httpx.AsyncClient() as client:
                await client.post(f"{BASE_URL}/sendPhoto", json={"chat_id": chat_id, "photo": QR_URL, "caption": "Scan to Pay ₹19"})
                await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": welcome, "parse_mode": "Markdown"})

        # 2. ✅ ADMIN APPROVAL (Sirf aap kar paoge)
        elif text.startswith("/approve") and chat_id == ADMIN_ID:
            try:
                target_id = text.split(" ")[1]
                users_db[target_id] = {"scans": 10} 
                msg = f"✅ Agent {target_id} authorized for 10 God-Level Scans."
            except: msg = "❌ Format: /approve USER_ID"
            async with httpx.AsyncClient() as client:
                await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": msg})

        # 3. 🔍 ULTRA DEEP SEARCH (Leak + Social)
        else:
            user = users_db.get(chat_id, {"scans": 0})
            if user["scans"] > 0:
                async with httpx.AsyncClient() as client:
                    # Leak API Call
                    p = {"token": LEAK_API_TOKEN, "request": text, "limit": 15}
                    r = await client.post("https://leakosintapi.com/", json=p, timeout=25.0)
                    res = r.json()
                
                users_db[chat_id]["scans"] -= 1
                reply = f"📑 *Investigation Report for: {text}*\n"
                
                # Leaks Data
                if res.get("List") and res["List"] != {}:
                    for db_name, content in list(res["List"].items())[:4]:
                        reply += f"\n📂 *Source:* {db_name}\njs\n{json.dumps(content['Data'][0], indent=2)}\n"
                else:
                    reply += "\n❌ *Database:* No direct leak found. Switching to Social Mapping...\n"

                # Social Media Accounts Tracking
                clean_num = text.replace("+", "").replace(" ", "")
                reply += f"\n🕵️‍♂️ *Social Identification Links:*\n"
                reply += f"📱 [WhatsApp Status](https://wa.me/{clean_num})\n"
                reply += f"📸 [Instagram Profile Search](https://www.instagram.com/explore/tags/{clean_num})\n"
                reply += f"👥 [Facebook Profile Search](https://www.facebook.com/search/top/?q={clean_num})\n"
                reply += f"✉️ [TrueCaller Identity](https://www.truecaller.com/search/in/{clean_num})\n"
                reply += f"🌍 [Global Web Search](https://www.google.com/search?q=%22{clean_num}%22)\n"
                
                reply += f"\n📉 Remaining Scans: {users_db[chat_id]['scans']}"
                
                async with httpx.AsyncClient() as client:
                    await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": reply, "parse_mode": "Markdown", "disable_web_page_preview": True})
            else:
                deny = "⚠️ *ACCESS DENIED!*\nSystem is locked. Pay ₹19 to @Charak_777 to unlock investigation power."
                async with httpx.AsyncClient() as client:
                    await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": deny})

    return {"status": "ok"}

@app.get("/set-webhook")
async def set_webhook():
    async with httpx.AsyncClient() as client:
        await client.get(f"{BASE_URL}/setWebhook?url=https://welfare-intelligence-api.onrender.com/webhook")
    return {"status": "Ultra Webhook Activated Successfully"}