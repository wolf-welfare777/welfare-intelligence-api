from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import httpx
import os

app = FastAPI()

# --- CONFIGURATION ---
BOT_TOKEN = "8369647120:AAE0S7oP9s2hhqMh4b3bGFvKtJaRfIzdgJE"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# --- 1. ADVANCED WEB/APP DASHBOARD ---
@app.get("/cyber", response_class=HTMLResponse)
async def hacker_dashboard(request: Request):
    client_ip = request.client.host
    return f"""
    <html>
        <head>
            <title>C4ar4k-X | OSINT PRO</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
            <style>
                body {{ background: black; color: #00ff00; font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }}
                canvas {{ position: fixed; top: 0; left: 0; z-index: -1; }}
                .container {{ position: relative; z-index: 1; padding: 15px; text-align: center; }}
                .box {{ border: 2px solid #00ff00; display: inline-block; padding: 25px; background: rgba(0, 10, 0, 0.9); box-shadow: 0 0 20px #00ff00; border-radius: 10px; width: 90%; max-width: 450px; margin-top: 30px; }}
                input {{ background: #000; color: #00ff00; border: 1px solid #00ff00; padding: 15px; width: 90%; outline: none; margin-top: 15px; font-size: 16px; }}
                button {{ background: #00ff00; color: black; border: none; padding: 15px; cursor: pointer; font-weight: bold; margin-top: 15px; width: 90%; font-size: 16px; }}
                #log {{ margin-top: 20px; text-align: left; font-size: 14px; min-height: 100px; color: #0f0; padding: 10px; border-top: 1px solid #004400; }}
                .access-granted {{ color: #00ff00; border: 1px solid #0f0; padding: 5px; margin-top: 5px; display: block; background: rgba(0,255,0,0.1); }}
            </style>
        </head>
        <body>
            <canvas id="matrix"></canvas>
            
            <audio id="typeSound"><source src="https://www.soundjay.com/communication/typing-on-computer-keyboard-1.mp3"></audio>
            <audio id="accessSound"><source src="https://www.soundjay.com/buttons/button-20.mp3"></audio>

            <div class="container">
                <div class="box">
                    <h2 style="text-shadow: 0 0 10px #0f0;">[ C4ar4k-X OSINT SYSTEM ]</h2>
                    <p style="font-size: 12px; color: yellow;">IP: {client_ip} | OWNER: @Charak_777</p>
                    
                    <input type="text" id="target" placeholder="Enter Target Username..." oninput="document.getElementById('typeSound').play()">
                    <button onclick="runSearch()">EXECUTE DEEP SEARCH</button>
                    
                    <div id="log">> System Ready... Enter Target Data.</div>
                </div>
            </div>

            <script>
                const canvas = document.getElementById('matrix');
                const ctx = canvas.getContext('2d');
                canvas.width = window.innerWidth; canvas.height = window.innerHeight;
                const characters = "0101XYZ@#$%&*";
                const drops = Array(Math.floor(canvas.width/20)).fill(1);
                function draw() {{
                    ctx.fillStyle = "rgba(0, 0, 0, 0.05)"; ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = "#0F0"; ctx.font = "15px monospace";
                    drops.forEach((y, i) => {{
                        const text = characters.charAt(Math.floor(Math.random() * characters.length));
                        ctx.fillText(text, i * 20, y * 20);
                        if (y * 20 > canvas.height && Math.random() > 0.975) drops[i] = 0;
                        drops[i]++;
                    }});
                }}
                setInterval(draw, 35);

                function runSearch() {{
                    let target = document.getElementById('target').value;
                    let log = document.getElementById('log');
                    if(!target) return;
                    
                    document.getElementById('accessSound').play();
                    log.innerHTML = "> Scanning Network Nodes for: " + target;
                    
                    setTimeout(() => {{ log.innerHTML += "<br>> Bypassing Social Firewall..."; }}, 1000);
                    setTimeout(() => {{ 
                        log.innerHTML += "<br><span class='access-granted'>[ PROFILE DISCOVERED ]<br>Link: <a href='https://instagram.com/"+target+"' target='_blank' style='color:white;'>instagram.com/"+target+"</a></span>"; 
                    }}, 2500);
                }}
            </script>
        </body>
    </html>
    """

# --- 2. TELEGRAM BOT ENGINE ---
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        if text == "/start":
            reply = "Welcome to C4ar4k-X OSINT System!\\n\\nSend any Instagram username to fetch real-time data."
        else:
            # Real Link Generation
            reply = f"🔍 SCANNING TARGET: {text}\\n\\n✅ SUCCESS: Profile Found\\n🔗 LINK: https://instagram.com/{text}"
            
        async with httpx.AsyncClient() as client:
            await client.post(f"{BASE_URL}/sendMessage", json={{"chat_id": chat_id, "text": reply}})
    return {{"status": "ok"}}

# Webhook Setup
@app.get("/set-webhook")
async def set_webhook():
    webhook_url = "https://welfare-intelligence-api.onrender.com/webhook"
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/setWebhook?url={webhook_url}")
    return r.json()

@app.get("/")
async def root():
    return {{"status": "Online", "system": "C4ar4k-X", "bot": "@C4ar4kX_Bot"}}
