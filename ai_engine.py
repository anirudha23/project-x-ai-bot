import json
import random
from datetime import datetime

# This function generates a new dummy signal using AI logic (for now it simulates logic)
def generate_ai_signal():
    direction = random.choice(["BUY", "SELL"])
    base_price = random.randint(65000, 66000)
    entry = base_price
    sl = base_price - 400 if direction == "BUY" else base_price + 400
    tp = base_price + 800 if direction == "BUY" else base_price - 800

    signal = {
        "symbol": "BTCUSDT",
        "timeframe": random.choice(["5m", "15m"]),
        "direction": direction,
        "entry": str(entry),
        "sl": str(sl),
        "tp": str(tp),
        "votes": "2 YES / 1 NO",
        "chatgpt": f"YES → Entry: {entry} | SL: {sl} | TP: {tp}",
        "grok": f"YES → Entry: {entry-10} | SL: {sl-100} | TP: {tp-100}",
        "deepshik": "NO → Entry: — | SL: — | TP: —",
        "timestamp": datetime.utcnow().isoformat()
    }

    return signal

# Save to last_signal.json
def save_signal(signal):
    with open("last_signal.json", "w") as f:
        json.dump(signal, f, indent=2)
    print("✅ New AI signal written to last_signal.json")

if __name__ == "__main__":
    signal = generate_ai_signal()
    save_signal(signal)
