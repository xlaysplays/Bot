import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')


@bot.tree.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)  # Convert to milliseconds
    await interaction.response.send_message(f"Pong! Latency: {latency}ms")


@bot.tree.command(name="hello", description="Says hello to you!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.name}!")


# Get token from environment variables
token = os.getenv('DISCORD_BOT_TOKEN')
if not token:
    print("Error: DISCORD_BOT_TOKEN environment variable not set!")
    print("Using hardcoded token for now - please add to Secrets!")
    token = "MTM4NTI4OTAwOTg0ODI1NDYwNg.GdyXNd.OI3dwYSbk-mYKwFXXVET0KjmZUCMdeshEQKklw"

bot.run(token)
