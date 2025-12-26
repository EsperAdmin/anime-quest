import discord 
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

# Set command prefix and require intents
bot = commands.Bot(command_prefix='$', intents=intents)

# Starting the bot
@bot.event
async def on_ready():
    print(f"{bot.user} has started!")


# Watch if message is from self
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

# Commands
@bot.command()
async def stats(ctx):
    await ctx.send(
    f"**{bot.user.display_name}** stats!"
    f"\nServers: {len(bot.guilds)}"
    f"\nLatency: {format(round(bot.latency * 1000))}ms")

# Run the bot and pass ENV Token
bot.run(os.getenv('BOT_TOKEN'))

    