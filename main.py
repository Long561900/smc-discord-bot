import os
import requests
import time

DISCORD_TOKEN = os.getenv("")
WEBHOOK_URL = os.getenv("")
def send_alert(msg):
    payload = {"content": msg}
    requests.post(WEBHOOK_URL, json=payload)

def main_loop():
    while True:
        # Giả lập tín hiệu SMC mẫu
        signal = "[SMC Alert] EUR/USD vừa xuất hiện CHoCH + OB Buy zone. Winrate 82% 🔵"
        send_alert(signal)
        time.sleep(3600)  # gửi mỗi 1 tiếng

if __name__ == "__main__":
    main_loop()
