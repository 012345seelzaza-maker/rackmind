
import discord, os
# pip install discord.py openai

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user in message.mentions or message.content.startswith("!rack"):
        # TODO: fetch metrics and call LLM
        await message.channel.send("**RackMind:** PUE 1.72 | Temp 26.8°C | All systems normal. Wasted $12.3 yesterday. Recommendation: Clean air filter.")

client.run(os.getenv("DISCORD_BOT_TOKEN"))
