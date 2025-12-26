

import random
import string
import json
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# --- ⚙️ CONFIGURATION ---
BOT_TOKEN = "8369647120:AAE0S7oP9s2hhqMh4b3bGFvKtJaRfIzdgJE"
BOT_USERNAME = "C4ar4kX_OSINT_bot"
ADMIN_ID = "7856837434"
LEAK_API_TOKEN = "NDiqpXCQOnVgfeP5XYEXkt6bGNOYCgGo"
QR_URL = "https://files.catbox.moe/p88m0j.png" 
UPI_ID = "charak777@ybl"

TG_CHANNEL = "https://t.me/wolf_welfare_77"
INSTA_LINK = "https://www.instagram.com/teamwelfare77?igsh=d21ia3h6eWJ5Z2lu"
X_LINK = "https://x.com/TeamWelfar62682"
MASTER_KEY = "TEAM_WELFARE_ADMIN_777"

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
users_db = {} 
keys_db = {}  

# --- 🖥️ WEB INTERFACE (MAP + NEWS + SOCIALS) ---
HACKER_UI = f"""
<!DOCTYPE html>
<html>
<head>
    <title>C4ar4k-X Intelligence Terminal</title>
    <style>
        body {{ background: #000; color: #0f0; font-family: 'Courier New', monospace; margin: 0; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }}
        .header {{ width: 100%; padding: 15px; text-align: center; border-bottom: 2px solid #0f0; background: rgba(0, 20, 0, 0.9); }}
        #clock {{ font-size: 1.2rem; color: #fff; margin-top: 5px; }}
        .main-container {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 20px; width: 95%; }}
        .map-box {{ flex: 2; min-width: 500px; height: 450px; border: 2px solid #0f0; border-radius: 10px; box-shadow: 0 0 20px #0f0; overflow: hidden; }}
        .side-panel {{ flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 15px; }}
        .info-box {{ border: 1px solid #0f0; padding: 15px; background: rgba(0, 30, 0, 0.8); border-radius: 8px; }}
        .social-btn {{ display: block; margin: 10px 0; padding: 10px; text-align: center; text-decoration: none; font-weight: bold; border-radius: 4px; color: white; }}
        .tg {{ background: #24A1DE; }} .insta {{ background: #E1306C; }} .x-btn {{ background: #333; }}
        .news-box {{ font-size: 0.85rem; height: 180px; overflow-y: hidden; border: 1px solid #f00; color: #ff0; }}
        .btn-main {{ padding: 20px 40px; background: #0f0; color: #000; text-decoration: none; font-weight: bold; border-radius: 8px; font-size: 1.4rem; box-shadow: 0 0 30px #0f0; margin: 20px; }}
    </style>
</head>
<body onload="startTime()">
    <div class="header">
        <h1>C4AR4K-X GLOBAL INTELLIGENCE</h1>
        <div id="clock"></div>
        <p style="color:red; font-weight:bold; letter-spacing: 2px;">[ CHARAK INVESTIGATION MODE: ACTIVE ]</p>
    </div>
    <div class="main-container">
        <div class="map-box"><iframe src="https://cybermap.kaspersky.com/en/widget/v2" width="100%" height="100%" frameborder="0"></iframe></div>
        <div class="side-panel">
            <div class="info-box">
                <h3 style="color:#0f0; text-align:center;">TEAM WELFARE HUB</h3>
                <a href="{TG_CHANNEL}" target="_blank" class="social-btn tg">Join Telegram</a>
                <a href="{INSTA_LINK}" target="_blank" class="social-btn insta">Follow Instagram</a>
                <a href="{X_LINK}" target="_blank" class="social-btn x-btn">Follow X Account</a>
            </div>
            <div class="info-box news-box">
                <h3 style="color:#f00; text-align:center;">📡 LIVE INTELLIGENCE</h3>
                <div id="news-content"></div>
            </div>
        </div>
    </div>
    <a href="https://t.me/{BOT_USERNAME}" class="btn-main">🚀 ACCESS INVESTIGATION BOT</a>
    <script>
        function startTime() {{
            const today = new Date();
            document.getElementById('clock').innerHTML = today.toDateString() + " | " + today.toLocaleTimeString();
            setTimeout(startTime, 1000);
        }}
        const newsList = [
            "⚠️ [INDIA] New phishing node detected in Delhi-NCR.",
            "🔒 [SYSTEM] AES-256 Military Encryption active.",
            "📡 [INFO] Scammer database linked successfully.",
            "🇮🇳 [CERT-In] Advisory: New malware targeting Android users.",
            "🛰️ [TRACKER] Team Welfare monitoring 400+ scam nodes."
        ];
        setInterval(() => {{
            let n = newsList[Math.floor(Math.random()*newsList.length)];
            const box = document.getElementById('news-content');
            box.innerHTML = "<p style='margin:5px 0'>> " + n + "</p>" + box.innerHTML;
        }}, 4000);
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home(): return HACKER_UI

# --- 🤖 TELEGRAM BOT LOGIC ---
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = str(data["message"]["chat"]["id"])
        text = data["message"].get("text", "").strip()
        f_name = data["message"]["from"].get("first_name", "Agent")

        if text == "/start":
            alert = f"🚨 *New User Spotted!*\n👤 Name: {f_name}\n🆔 ID: {chat_id}\n\nTo send key: /sendkey {chat_id}"
            async with httpx.AsyncClient() as client:
                await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": ADMIN_ID, "text": alert, "parse_mode": "Markdown"})
            
            welcome = (
                f"🛰️ *C4ar4k-X OSINT Terminal v10.0*\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"👤 *Operator:* {f_name}\n"
                "🛡️ *Status:* LOCKED (Auth Required)\n"
                f"━━━━━━━━━━━━━━━━━━━━\n\n"
                "System unlock karne ke liye ₹19 pay karein aur @Charak_777 ko screenshot bhejien."
            )
            keyboard = {"inline_keyboard": [[{"text": "💳 Pay & Activate (₹19)", "url": "https://t.me/Charak_777"}],[{"text": "📢 Team Welfare", "url": TG_CHANNEL}]]}
            async with httpx.AsyncClient() as client:
                await client.post(f"{BASE_URL}/sendPhoto", json={"chat_id": chat_id, "photo": QR_URL, "caption": "Official Team Welfare QR"})
                await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": welcome, "parse_mode": "Markdown", "reply_markup": keyboard})

        elif text.startswith("/sendkey") and chat_id == ADMIN_ID:
            try:
                target_id = text.split(" ")[1]
                new_key = "CX-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                keys_db[new_key] = 30
                msg = f"🎁 *ACCESS KEY GENERATED!*\nAapki Key: {new_key}\nIse copy karke yahan paste karein!"
                async with httpx.AsyncClient() as client:
                    await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": target_id, "text": msg, "parse_mode": "Markdown"})
                    await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": ADMIN_ID, "text": f"✅ Key {new_key} sent to {target_id}"})
            except: pass

        elif text.startswith("CX-") or text == MASTER_KEY:
            if text == MASTER_KEY:
                users_db[chat_id] = {"active": True, "scans": 9999}
                res = "🔥 *Admin Master Key Accepted!*"
            elif text in keys_db:
                users_db[chat_id] = {"active": True, "scans": keys_db[text]}
                del keys_db[text]
                res = "✅ *System Unlocked!* Search chalu karein."
            else: res = "❌ Invalid Key!"
            async with httpx.AsyncClient() as client:
                await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": res})

        else:
            user = users_db.get(chat_id, {"active": False, "scans": 0})
            if user["active"] and user["scans"] > 0:
                async with httpx.AsyncClient() as client:
                    load = await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": "🔍 *Scanning Archives...*"})
                    l_id = load.json()["result"]["message_id"]
                    p = {"token": LEAK_API_TOKEN, "request": text, "limit": 10}
                    r = await client.post("https://leakosintapi.com/", json=p, timeout=35.0)
                    res = r.json()
                
                users_db[chat_id]["scans"] -= 1
                rep = f"📊 *C4AR4K-X REPORT\n━━━━━━━━━━━━━━━━━━━━\n🎯 **Target:* {text}\n"
                if res.get("List") and res["List"] != {}:
                    for db, content in list(res["List"].items())[:3]:
                        rep += f"\n📂 *Source:* {db}\njs\n{json.dumps(content['Data'][0], indent=2)}\n"
                else: rep += "\n❌ Database mein koi record nahi mila."
                num = text.replace("+", "").replace(" ", "")
                rep += f"\n━━━━━━━━━━━━━━━━━━━━\n🌐 [WhatsApp](https://wa.me/{num}) | [Insta](https://instagram.com/explore/tags/{num})\n📉 Scans Left: {users_db[chat_id]['scans']}"
                async with httpx.AsyncClient() as client:
                    await client.post(f"{BASE_URL}/deleteMessage", json={"chat_id": chat_id, "message_id": l_id})
                    await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": rep, "parse_mode": "Markdown", "disable_web_page_preview": True})
            else:
                async with httpx.AsyncClient() as client:
                    await client.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": "⚠️ *Access Denied!* Pehle Premium Key enter karein."})

    return {"status": "ok"}

@app.get("/set-webhook")
async def set_webhook():
    async with httpx.AsyncClient() as client:
        await client.get(f"{BASE_URL}/setWebhook?url=https://welfare-intelligence-api.onrender.com/webhook")
    return {"status": "God Mode System Active"}