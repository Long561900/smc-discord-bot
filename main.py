
import discord
import json
import asyncio
import requests

with open("config.json") as f:
    config = json.load(f)

TOKEN = config["discord_token"]
WEBHOOK_URL = config["webhook_url"]

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    while True:
        data = {
            "content": "**[SMC ALERT]** EUR/USD xuất hiện CHoCH + OB Buy zone. Winrate 82%. ✅"
        }
        requests.post(WEBHOOK_URL, json=data)
        await asyncio.sleep(3600)

bot.run(TOKEN)
