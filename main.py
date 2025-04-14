import os
import requests
import time

DISCORD_TOKEN = os.getenv("MTM2MDIyODA1ODQ1NTYwNTM5Mg.G6rZ_u.eML2JrW4OWM4TUI4zj6TPi68AZZeI59SQhnbL0")
WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1360181990397050950/Gjk6bzD_UOhjtn2iwCwNs6Nl50BpSpzYPxIyudSmfvs0h_lf9rY15OLB_PYeA8QSbeAc")

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
