import psutil
import platform
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/cyber", response_class=HTMLResponse)
def advanced_hacker_dashboard():
    # Laptop ki asli details nikalna
    cpu_usage = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    os_name = platform.system() + " " + platform.release()

    return f"""
    <html>
        <head>
            <title>C4ar4k-X | Intelligence System</title>
            <style>
                body {{ margin: 0; background: black; overflow: hidden; font-family: 'Courier New'; color: #0f0; }}
                canvas {{ position: absolute; top: 0; left: 0; z-index: -1; }}
                .main-box {{
                    position: relative; border: 3px solid #0f0; background: rgba(0,0,0,0.8);
                    width: 80%; margin: 50px auto; padding: 20px; box-shadow: 0 0 30px #0f0; text-align: center;
                }}
                h1 {{ color: #f00; font-size: 40px; text-shadow: 0 0 10px #f00; margin: 5px; }}
                .stat {{ color: #0ff; font-size: 18px; margin: 10px 0; }}
                .dev-tag {{ background: #0f0; color: #000; padding: 5px 20px; font-weight: bold; font-size: 20px; }}
                .blink {{ animation: b 1s infinite; color: #fff; }}
                @keyframes b {{ 50% {{ opacity: 0; }} }}
            </style>
        </head>
        <body>
            <canvas id="matrix"></canvas>
            <div class="main-box">
                <div class="blink">>>> DECRYPTING SYSTEM DATA <<<</div>
                <h1>WELFARE INTELLIGENCE</h1>
                <div class="dev-tag">OPERATOR: C4ar4k-X</div>
                <div class="stat">
                    <p>OS: {os_name}</p>
                    <p>CPU USAGE: {cpu_usage}%</p>
                    <p>RAM STATUS: {ram}%</p>
                </div>
            </div>

            <audio id="hackerSound">
                <source src="https://www.soundjay.com/buttons/sounds/beep-01a.mp3" type="audio/mpeg">
            </audio>

            <script>
                const canvas = document.getElementById('matrix');
                const ctx = canvas.getContext('2d');
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                const letters = "01010101WELFAREINTELLIGENCEC4AR4KX";
                const fontSize = 16;
                const columns = canvas.width / fontSize;
                const drops = Array(Math.floor(columns)).fill(1);

                function draw() {{
                    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = "#0f0";
                    ctx.font = fontSize + "px arial";
                    for (let i = 0; i < drops.length; i++) {{
                        const text = letters.charAt(Math.floor(Math.random() * letters.length));
                        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                        drops[i]++;
                    }}
                }}
                setInterval(draw, 33);
                
                // Sound activate karne ke liye mobile screen pe click karein
                document.body.addEventListener('click', () => {{
                    const audio = document.getElementById('hackerSound');
                    audio.play();
                }});
            </script>
        </body>
    </html>
    """
    import httpx
from fastapi import FastAPI

app = FastAPI()

# OSINT Function: Check Username
async def check_username(username: str):
    social_media = {
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
    }
    results = {}
    async with httpx.AsyncClient() as client:
        for platform, url in social_media.items():
            try:
                response = await client.get(url)
                if response.status_code == 200:
                    results[platform] = "FOUND ✅"
                else:
                    results[platform] = "Not Found ❌"
            except:
                results[platform] = "Error ⚠️"
    return results

@app.get("/osint/{username}")
async def osint_tool(username: str):
    data = await check_username(username)
    return {"target": username, "results": data}
