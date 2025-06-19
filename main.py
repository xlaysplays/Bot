import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Important for message commands to work

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')

# Add your token here
bot.run("YOUR_BOT_TOKEN")
  
