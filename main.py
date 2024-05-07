import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

crafting_ideas = [
    "Plastik Şişelerden Bitki Saksısı Yapımı",
    "Plastik Kaşıklardan Süs Eşyası Yapımı",
    "Plastik Şişelerden Kalemlik Yapımı",
    "Plastik Tabaklardan Duvar Dekoru Yapımı",
    "Plastik Kaplardan Takı Kutusu Yapımı",
    "Plastik Şişelerden Lamba Yapımı"
]

@bot.command()
async def elisi(ctx):
    '''Rastgele bir el işi fikri alın.'''
    crafting_idea = random.choice(crafting_ideas)
    await ctx.send(f"İşte bir el yapımı plastik işi fikri: {crafting_idea}")

bot.run("Buaya Token ekleyin")
