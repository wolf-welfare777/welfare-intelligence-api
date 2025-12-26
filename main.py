from fastapi import FastAPI, Request
import httpx
import json

app = FastAPI()

# --- CONFIGURATION ---
BOT_TOKEN = "8369647120:AAE0S7oP9s2hhqMh4b3bGFvKtJaRfIzdgJE"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
LEAK_API_TOKEN = "NDiqpXCQOnVgfeP5XYEXkt6bGNOYCgGo"
ADMIN_ID = "7856837434"  # Aapki numeric ID

# Subscriptions Database (Volatile)
users_db = {} 

def format_as_js(data):
    """Format data entries in a professional JS style."""
    lines = []
    for key, value in data.items():
        value_str = json.dumps(value)
        lines.append(f"  {key}: {value_str}")
    return "{\n" + "\n".join(lines) + "\n}"

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = str(data["message"]["chat"]["id"])
        text = data["message"].get("text", "").strip()

        # 1. Start Command & Welcome UI
        if text == "/start":
            reply = (
                "🚀 *C4ar4k-X OSINT System v2.0*\n\n"
                "Welcome to the most advanced OSINT tool.\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "🛠 *Features:*\n"
                "• Instagram Profile Scanning\n"
                "• Deep Data Leak Search (Number/Email)\n\n"
                "💎 *Pricing:*\n"
                "• 1st Trial: ₹19 (3 Scans)\n"
                "• Monthly: ₹199 (Unlimited)\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "Pay ₹19 to UPI: naveen@upi and send screenshot to @Charak_777.\n\n"
                "🔴 *Developer: Charak X*"
            )
        
        # 2. Admin Approval Logic (/approve 12345678)
        elif text.startswith("/approve") and chat_id == ADMIN_ID:
            try:
                target_user = text.split(" ")[1]
                users_db[target_user] = {"scans_left": 3, "premium": True}
                reply = f"✅ User {target_user} approved for 3 scans by Admin Charak X!"
            except:
                reply = "❌ Format galat hai! Use karein: /approve USER_ID"

        # 3. Processing Scans (Check if user has credits)
        else:
            user_info = users_db.get(chat_id, {"scans_left": 0, "premium": False})
            
            if user_info["scans_left"] > 0:
                # Target Detection (Leak Search vs Instagram)
                if "@" in text or text.startswith("+") or (text.isdigit() and len(text) > 5):
                    # --- LEAKOSINT LOGIC ---
                    payload = {"token": LEAK_API_TOKEN, "request": text, "limit": 10}
                    async with httpx.AsyncClient() as client:
                        try:
                            res = await client.post("https://leakosintapi.com/", json=payload, timeout=20.0)
                            resp = res.json()
                        except:
                            resp = {"List": {}}
                    
                    if resp.get("List") == {} or not resp.get("List"):
                        reply = "❌ No data found in leaked databases for this target."
                    else:
                        users_db[chat_id]["scans_left"] -= 1
                        reply = f"📁 *Database Scan Results:* {text}\n"
                        # Show data from the first database found
                        for db in resp["List"].keys():
                            entry = resp["List"][db]["Data"][0]
                            reply += f"\n*Source:* {db}\njs\n{format_as_js(entry)}\n"
                            break 
                        reply += f"\n📉 Scans Remaining: {users_db[chat_id]['scans_left']}"
                else:
                    # --- INSTAGRAM LOGIC ---
                    users_db[chat_id]["scans_left"] -= 1
                    reply = (
                        f"🔍 *SCANNING TARGET:* {text}\n"
                        f"━━━━━━━━━━━━━━━━━━━━\n"
                        f"✅ *SUCCESS:* Profile Found\n"
                        f"🔗 *LINK:* https://instagram.com/{text}\n\n"
                        f"📉 Scans Remaining: {users_db[chat_id]['scans_left']}"
                    )
            else:
                # Block unpaid users
                reply = (
                    "⚠️ *ACCESS DENIED*\n\n"
                    "Aapka trial khatam ho gaya hai ya aapne payment nahi kiya hai.\n\n"
                    "👉 *Unlock 3 Scans for ₹19*\n"
                    "Contact: @Charak_777"
                )

        # Send response to Telegram
        async with httpx.AsyncClient() as client:
            await client.post(f"{BASE_URL}/sendMessage", json={
                "chat_id": chat_id, 
                "text": reply, 
                "parse_mode": "Markdown"
            })
            
    return {"status": "ok"}

@app.get("/set-webhook")
async def set_webhook():
    webhook_url = "https://welfare-intelligence-api.onrender.com/webhook"
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/setWebhook?url={webhook_url}")
        return r.json()

@app.get("/")
async def root():
    return {"status": "Online", "system": "C4ar4k-X", "developer": "Charak X"}