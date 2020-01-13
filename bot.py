import os
import discord

token = os.environ.get("DISCORD_TOKEN")
print(token)
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

client.run(token)