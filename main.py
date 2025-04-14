import os
import requests

def send_alert():
    webhook_url = os.getenv("webhook_url")
    message = {
        "content": "**[SMC Alert]** EUR/USD vừa xuất hiện CHoCH + OB Buy zone. Winrate 82%. 📈",
    }
    requests.post(webhook_url, json=message)

if __name__ == "__main__":
    send_alert()
