import os

import discord

from formatter import format_for_csv
from loot import extract_loot
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.attachments:
        await message.add_reaction('\N{STOPWATCH}')
        total = len(message.attachments)
        loots = []
        for idx, attachment in enumerate(message.attachments):
            loot = await extract_loot(attachment)
            loots.append(format_for_csv(message.author.global_name, loot))
        await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
        joinedList = "\n".join(loots)
        await message.channel.send(f"<@{message.author.id}> ```{joinedList}```")



client.run(os.getenv('TOKEN'))
