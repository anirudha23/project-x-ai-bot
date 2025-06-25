import os, json, requests

# 1) Check that .env is being read
print("ENV  ➜ DISCORD_WEBHOOK_URL =", os.getenv("DISCORD_WEBHOOK_URL"))

# 2) Build a minimal test payload
payload = {
    "content": "🚨 DEBUG TEST – If you see this in Discord, webhook works."
}

# 3) Send to Discord
url = os.getenv("DISCORD_WEBHOOK_URL")
if not url:
    print("❌  No webhook URL found in environment variables.")
    exit()

r = requests.post(url, data=json.dumps(payload),
                  headers={"Content-Type": "application/json"})

print("HTTP status   ➜", r.status_code)
print("Discord reply ➜", r.text if r.text else "(empty)")
