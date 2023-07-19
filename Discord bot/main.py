token = 'MTEzMTI2MDQzODY2ODEyNDM0NA.Gw2prV.KDL9f0IoOBPyA_JruoXBgppOds0mo7ufL4zFZ8'
prefix = "!"
from progress.bar import Bar
import discord
from discord.ext import commands
import random
import asyncio

imports = [
    'from progress.bar import Bar',
    'import discord',
    'from discord.ext import commands',
    'import random'
]

print("Loading...")
bar = Bar('loading', max=len(imports))
for i in range(0, len(imports)):
    exec(str(imports[i]))
    bar.next()
bar.finish()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"ready to bring joy to the universe. {bot.user.display_name}, {bot.user.id}")

ch_channel = ""
@bot.command()
async def set_channel(ctx):
    ch_channel = ctx.channel
    await ctx.send(f"set channel to {ch_channel}")

@bot.command()
async def start(ctx):
    urls = open('urls.txt', "r")
    clist = []
    for i in urls:
        clist.append(i.replace("\n", ""))
    while True:
        x = random.choice(clist)
        embed = discord.Embed(
            title="Cute ChinChilla!!!"
        )
        embed.set_image(url=x)
        await ctx.send(embed=embed)
        await ctx.ch_channel.send(embed=embed)
        bar = Bar('loading', max=60)
        for i in range(0, 60):
            exec(str(i))
            bar.next()
        bar.finish()



try:
    bot.run(token)
except discord.LoginFailure:
    print('Invalid Token Passed')