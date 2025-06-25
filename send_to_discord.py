import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_signal_if_any():
    try:
        with open("latest_signal.json", "r") as f:
            signal = json.load(f)
    except Exception:
        print("⚠️ No signal file found.")
        return

    if not signal or signal.get("sent"):
        print("ℹ️ No new signal to send.")
        return

    # Format message
    message = f"""📡 **Project X Signal – BTCUSDT (15m)**

**Direction:** {signal['direction']}
**Entry:** {signal['entry']}
**Stoploss:** {signal['sl']}
**Take Profit:** {signal['tp']}
**Vote Count:** {signal['votes']}

🧠 **AI Votes:**
• ChatGPT:   {signal['ai_votes']['chatgpt']}
• Grok:      {signal['ai_votes']['grok']}
• Deepshik:  {signal['ai_votes']['deepshik']}
"""

    data = {
        "content": message
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("✅ Signal sent to Discord.")

        # Mark as sent
        signal["sent"] = True
        with open("latest_signal.json", "w") as f:
            json.dump(signal, f, indent=4)
    else:
        print(f"❌ Failed to send message: {response.status_code}")
