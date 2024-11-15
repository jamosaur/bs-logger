import os
import discord
from formatter import format_for_csv
from loot import extract_loot, create_coins_drop
from dotenv import load_dotenv
import re

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

    coin_drops = []
    loots = []

    if message.attachments:
        await message.add_reaction('\N{STOPWATCH}')
        total = len(message.attachments)
        for idx, attachment in enumerate(message.attachments):
            loot = await extract_loot(attachment)
            loots.append(format_for_csv(message.author.global_name, loot))
        await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

    if message.content.startswith('!coins'):
        amount = message.content.replace('!coins', '')
        amount = amount.strip()
        split = amount.split(' ')
        inputs = list(map(lambda i: re.sub('[^0-9]', '', i), split))
        inputs = list(filter(bool, inputs))

        if len(inputs):
            for input in inputs:
                loot = create_coins_drop(input)
                coin_drops.append(format_for_csv(message.author.global_name, loot))

    joinedList = loots + coin_drops
    formattedList = "\n".join(joinedList)
    if len(formattedList):
        await message.channel.send(f"<@{message.author.id}> ```{formattedList}```")


client.run(os.getenv('TOKEN'))
