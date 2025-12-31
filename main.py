import asyncio, json, httpx, random, string
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# ================= [1. CONFIGURATION BLOCK] =================
TOKEN_A = "8488837085:AAGD9g2k_rT_i046HD3q3vBaKWguR18QFiM" # Finance Bot
TOKEN_B = "8369647120:AAE0S7oP9s2hhqMh4b3bGFvKtJaRfIzdgJE" # Scanner Bot
ADMIN_USER_ID = "7856837434"
UPI_ID = "charak777@ybl"

# Social Links
LINK_CHANNLE = "https://t.me/wolf_welfare_77"
LINK_INSTA = "https://www.instagram.com/teamwelfare77?igsh=d21ia3h6eWJ5Z2lu"
LINK_INSTA_BACKUP = "https://www.instagram.com/agyat.vyuh?igsh=emFrY21vM3hzeW9m"
LINK_X = "https://x.com/TeamWelfar62682"

# Helpers
def generate_key():
    return "CHX-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

async def send_msg(token, chat_id, text, markup=None):
    async with httpx.AsyncClient() as client:
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        if markup: payload["reply_markup"] = markup
        await client.post(f"https://api.telegram.org/bot{token}/sendMessage", json=payload)

# ================= [2. BOT B: SCANNER & GATEKEEPER] =================
@app.post("/webhook_b")
async def scanner_bot(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_name = data["message"]["from"].get("first_name", "Unknown")
        text = data["message"].get("text", "")

        if text == "/start":
            # Admin Logger
            await send_msg(TOKEN_A, ADMIN_USER_ID, f"🔔 *New User Alert!*\nName: {user_name}\nID: {chat_id}\nAction: Started Scanner")
            
            msg = "🛡️ *CHARAK-X OSINT INTERFACE*\n\nStatus: [ENCRYPTED]\n\nSystem access ke liye official channel join karna anivarya hai."
            markup = {"inline_keyboard": [
                [{"text": "📢 Join Official Channel", "url": LINK_CHANNLE}],
                [{"text": "✅ Verify & Enter Terminal", "callback_data": "menu"}]
            ]}
            await send_msg(TOKEN_B, chat_id, msg, markup)

    elif "callback_query" in data:
        chat_id = data["callback_query"]["message"]["chat"]["id"]
        cb_data = data["callback_query"]["data"]
        
        if cb_data == "menu":
            msg = "💻 *CHARAK-X TERMINAL CONSOLE*\n\nModules Loaded:\n1. OSINT Scanner (Active)\n2. Social Links (Connected)\n3. Database (Standby)"
            markup = {"inline_keyboard": [
                [{"text": "🔍 Launch OSINT Tool", "url": "https://t.me/C4ar4k2_Bot"}],
                [{"text": "📱 System Socials", "callback_data": "socials"}]
            ]}
            await send_msg(TOKEN_B, chat_id, msg, markup)
            
        elif cb_data == "socials":
            msg = "🔗 *OFFICIAL INTEL NETWORK:*"
            markup = {"inline_keyboard": [
                [{"text": "📸 Main Insta", "url": LINK_INSTA}],
                [{"text": "🔄 Backup Insta", "url": LINK_INSTA_BACKUP}],
                [{"text": "🐦 Twitter (X)", "url": LINK_X}],
                [{"text": "🔙 Back", "callback_data": "menu"}]
            ]}
            await send_msg(TOKEN_B, chat_id, msg, markup)
    return {"ok": True}

# ================= [3. BOT A: FINANCE & AUTO-APPROVAL] =================
@app.post("/webhook_a")
async def finance_bot(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_text = data["message"].get("text", "")

        if user_text == "/start":
            pay_msg = f"⚡ *CHARAK-X PREMIUM ACCESS\n\nPlan: ₹19 / Lifetime\nUPI ID: {UPI_ID}\n\nPayment ke baad **12-digit UTR ID* yahan likh kar bhein."
            await send_msg(TOKEN_A, chat_id, pay_msg)
            
        elif len(user_text) == 12 and user_text.isdigit():
            # User confirmation
            await send_msg(TOKEN_A, chat_id, "⏳ *UTR RECEIVED.*\nAdmin verification ke baad aapki Key bhej di jayegi.")
            # Admin Approval Shortcut
            admin_btn = {"inline_keyboard": [[{"text": "✅ APPROVE & SEND KEY", "callback_data": f"app_{chat_id}"}]]}
            await send_msg(TOKEN_A, ADMIN_USER_ID, f"💰 *Payment Claim!*\nUser: {chat_id}\nUTR: {user_text}", admin_btn)
            
        elif user_text.startswith("/approve") and str(chat_id) == ADMIN_USER_ID:
            try:
                target = user_text.split(" ")[1]
                key = generate_key()
                await send_msg(TOKEN_A, target, f"✅ *VERIFIED!*\n\nYour Access Key: {key}\nSystem: ACTIVE")
            except: pass
        else:
            if str(chat_id) != ADMIN_USER_ID:
                await send_msg(TOKEN_A, ADMIN_USER_ID, f"📩 *Message from {chat_id}:*\n{user_text}")

    elif "callback_query" in data:
        cb_data = data["callback_query"]["data"]
        if cb_data.startswith("app_"):
            target_id = cb_data.split("_")[1]
            key = generate_key()
            await send_msg(TOKEN_A, target_id, f"✅ *PAYMENT VERIFIED!*\n\nWelcome. Your Key: {key}")
            await send_msg(TOKEN_A, ADMIN_USER_ID, f"Success! Key sent to {target_id}")
    return {"ok": True}

# ================= [4. WEBPAGE: INTEL DASHBOARD] =================
@app.get("/", response_class=HTMLResponse)
async def home():
    return f"""
    <html>
    <head>
        <title>CHARAK-X | INTELLIGENCE DASHBOARD</title>
        <style>
            body {{ background: #000; color: #0f0; font-family: 'Courier New', monospace; margin: 0; }}
            .header {{ border-bottom: 2px solid #0f0; padding: 25px; text-align: center; background: #050505; }}
            .access-btn {{ display: block; width: 250px; margin: 20px auto; padding: 15px; border: 2px solid #0f0; color: #0f0; text-decoration: none; font-weight: bold; animation: glow 1.5s infinite; }}
            @keyframes glow {{ 0% {{ box-shadow: 0 0 5px #0f0; }} 50% {{ box-shadow: 0 0 25px #0f0; }} 100% {{ box-shadow: 0 0 5px #0f0; }} }}
            .grid {{ display: grid; grid-template-columns: 2fr 1fr; gap: 20px; padding: 20px; }}
            .box {{ border: 1px solid #333; padding: 15px; background: #080808; overflow: hidden; }}
            .news {{ font-size: 12px; color: #aaa; margin-bottom: 10px; border-left: 2px solid #f00; padding-left: 10px; }}
            iframe {{ width: 100%; height: 400px; border: 1px solid #111; }}
            .links a {{ color: #0f0; font-size: 13px; text-decoration: none; border: 1px solid #333; padding: 5px; margin-right: 5px; }}
            .links a:hover {{ background: #0f0; color: #000; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>CHARAK-X INTEL NETWORK</h1>
            <p>[ NATIONAL SECURITY & OSINT DASHBOARD - INDIA ]</p>
            <a href="https://t.me/C4ar4kX_Bot" class="access-btn">▶ ACCESS SYSTEM TERMINAL</a>
        </div>
        <div class="grid">
            <div class="left">
                <div class="box">
                    <h3>📊 LIVE CYBER THREAT RADAR</h3>
                    <iframe src="https://cybermap.kaspersky.com/en/widget/dynamic/dark"></iframe>
                </div>
                <br>
                <div class="box links">
                    <h3>🇮🇳 GOVERNMENT RESOURCES</h3>
                    <a href="https://cybercrime.gov.in">🚨 REPORT CRIME</a>
                    <a href="https://www.cert-in.org.in">🛡️ CERT-In ALERTS</a>
                    <a href="https://www.nia.gov.in">🗞️ NIA UPDATES</a>
                </div>
            </div>
            <div class="right">
                <div class="box">
                    <h3>🗞️ R&AW / NIA INTELLIGENCE FEEDS</h3>
                    <div class="news"><b>[NIA]</b> Special cell monitoring encrypted financial channels.</div>
                    <div class="news"><b>[R&AW]</b> Intelligence alert: High-risk phishing in defense sector.</div>
                    <div class="news"><b>[CERT-In]</b> New security advisory for Indian Android users.</div>
                    <div class="news"><b>[INFO]</b> Charak-X OSINT System v2.1 Active.</div>
                </div>
                <br>
                <div class="box">
                    <h3>📱 CONNECT SOCIALS</h3>
                    <p>Insta: <a href="{LINK_INSTA}" style="color:#0f0;">@teamwelfare77</a></p>
                    <p>Twitter: <a href="{LINK_X}" style="color:#0f0;">@TeamWelfar62682</a></p>
                    <p>Admin ID: <a href="https://t.me/Charak_777" style="color:#0f0;">@Charak_777</a></p>
                </div>
            </div>
        </div>
        <footer style="text-align:center; padding:15px; color:#444; font-size:10px;">&copy; CHARAK-X PROJECT | UNRESTRICTED INTELLIGENCE ACCESS</footer>
    </body>
    </html>
    """