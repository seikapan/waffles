import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Ensure this is enabled
bot = commands.Bot(command_prefix='!', intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def deal(ctx, *, game_name):
    """Fetches the best game deal for the specified game."""
    base_url = "https://www.cheapshark.com/api/1.0/deals?title="
    response = requests.get(f"{base_url}{game_name}")
    deals = response.json()
    
    if not deals:
        await ctx.send("No deals found for this game. Try another title!")
        return
    
    best_deal = deals[0]  # Assuming the first deal is the best
    deal_message = f"**{game_name}** is currently on sale for ${best_deal['salePrice']}! You can buy it from {best_deal['storeID']}. Here's the link: https://www.cheapshark.com/redirect?dealID={best_deal['dealID']}"
    
    await ctx.send(deal_message)

# Replace 'your_token_here' with your actual bot token
bot.run('INSERT TOKEN HERE')
