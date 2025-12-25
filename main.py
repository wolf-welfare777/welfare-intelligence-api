from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/cyber", response_class=HTMLResponse)
async def hacker_dashboard(request: Request):
    client_ip = request.client.host
    return f"""
    <html>
        <head>
            <title>C4ar4k-X | OSINT SYSTEM</title>
            <style>
                body {{ background: black; color: #00ff00; font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }}
                canvas {{ position: fixed; top: 0; left: 0; z-index: -1; }}
                .container {{ position: relative; z-index: 1; padding: 20px; text-align: center; }}
                .box {{ border: 2px solid #00ff00; display: inline-block; padding: 25px; background: rgba(0, 15, 0, 0.9); box-shadow: 0 0 20px #00ff00; border-radius: 8px; max-width: 500px; width: 90%; margin-top: 40px; }}
                .tab-btn {{ background: none; border: 1px solid #00ff00; color: #00ff00; padding: 10px 15px; cursor: pointer; margin: 5px; font-family: monospace; }}
                .active-tab {{ background: #00ff00; color: black; font-weight: bold; }}
                input {{ background: #000; color: #00ff00; border: 1px solid #00ff00; padding: 12px; width: 85%; outline: none; margin-top: 15px; }}
                button {{ background: #00ff00; color: black; border: none; padding: 12px 25px; cursor: pointer; font-weight: bold; margin-top: 15px; }}
                .footer {{ margin-top: 20px; font-size: 12px; }}
                .footer a {{ color: #00ff00; text-decoration: none; border-bottom: 1px solid #00ff00; }}
                #status-log {{ text-align: left; background: rgba(0,0,0,0.5); padding: 10px; margin-top: 15px; border-radius: 5px; font-size: 13px; min-height: 50px; color: cyan; }}
            </style>
        </head>
        <body>
            <canvas id="matrix"></canvas>
            
            <audio id="typeSound"><source src="https://www.soundjay.com/communication/typing-on-computer-keyboard-1.mp3" type="audio/mpeg"></audio>
            <audio id="clickSound"><source src="https://www.soundjay.com/buttons/button-20.mp3" type="audio/mpeg"></audio>

            <div class="container">
                <div class="box">
                    <h1 style="text-shadow: 0 0 10px #0F0;">[ C4ar4k-X OSINT SYSTEM ]</h1>
                    <p style="color: yellow; font-size: 14px;">TARGET IP: {client_ip} | OWNER: @Charak_777</p>
                    <hr color="#00ff00">

                    <div id="lock-screen">
                        <p style="color:red; font-weight:bold;">! ACCESS DENIED: UNLOCK REQUIRED !</p>
                        <button onclick="unlockSystem()">FOLLOW @teamwelfare77 TO UNLOCK</button>
                    </div>

                    <div id="main-interface" style="display:none;">
                        <button class="tab-btn active-tab" onclick="showTab('osint', this)">OSINT SEARCH</button>
                        <button class="tab-btn" onclick="showTab('network', this)">NETWORK TOOLS</button>
                        <div id="osint-content">
                            <h3 style="color: white;">SOCIAL RECONNAISSANCE</h3>
                            <input type="text" id="targetInput" placeholder="Enter Instagram Username..." onkeydown="playType()">
                            <br><button onclick="executeAction('Scanning Instagram...')">START INTRUSION</button>
                        </div>
                        <div id="network-content" style="display:none;">
                            <h3 style="color: white;">NETWORK SCANNER</h3>
                            <input type="text" placeholder="Enter IP Address..." onkeydown="playType()">
                            <br><button onclick="executeAction('Scanning Network...')">EXECUTE SCAN</button>
                        </div>
                        <div id="status-log"></div>
                    </div>
                    <div class="footer"><a href="https://t.me/Charak_777" target="_blank">DEVELOPED BY C4ar4k-X</a></div>
                </div>
            </div>

            <script>
                const canvas = document.getElementById('matrix');
                const ctx = canvas.getContext('2d');
                canvas.width = window.innerWidth; canvas.height = window.innerHeight;
                const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*";
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

                function playType() {{ document.getElementById('typeSound').play(); }}
                function playClick() {{ document.getElementById('clickSound').play(); }}

                function unlockSystem() {{
                    playClick();
                    window.open("https://www.instagram.com/teamwelfare77?igsh=d21ia3h6eWJ5Z2lu", "_blank");
                    document.getElementById('lock-screen').style.display = 'none';
                    document.getElementById('main-interface').style.display = 'block';
                }}

                function showTab(tab, btn) {{
                    playClick();
                    document.getElementById('osint-content').style.display = (tab === 'osint') ? 'block' : 'none';
                    document.getElementById('network-content').style.display = (tab === 'network') ? 'block' : 'none';
                    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active-tab'));
                    btn.classList.add('active-tab');
                }}

                function executeAction(msg) {{
                    playClick();
                    let log = document.getElementById('status-log');
                    log.innerHTML = "> " + msg;
                    setTimeout(() => {{ log.innerHTML += "<br>> Accessing Private Clusters..."; }}, 1500);
                    setTimeout(() => {{ log.innerHTML += "<br><span style='color:red'>> ERROR: DATABASE CONNECTION FAILED.</span>"; }}, 3000);
                }}
            </script>
        </body>
    </html>
    """