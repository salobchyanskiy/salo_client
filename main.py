import discord
from discord.ext import commands
from config import token

client = discord.Client(command_prefix = '$', intents=intents)

bot.command()
async def on_ready(ctx):
  print('Bot is now ready!')

  
  
client.run(token)
