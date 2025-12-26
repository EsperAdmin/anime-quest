import discord 
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

# Starting the bot
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"{self.user} has started!")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('BOT_TOKEN'))

# Commands

@commands.command()
async def stats(ctx):
    await ctx.send("Here are the bot stats!")

# Add commands
async def setup(bot):
    bot.add_command(stats)
    await bot.load_extension('stats')
    