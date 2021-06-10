import asyncio

import discord
from discord.ext import commands

TOKEN = ''  # Dein Token hier

bot = commands.Bot(command_prefix='')  # Dein Prefix hier


@bot.event
async def on_ready():
    print('--------------------------------------')
    print('Bot is ready.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------------------------')
    bot.loop.create_task(status_task())

########################################################################################################################


async def status_task():
    while True:
        # Online
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name='Dein Text', status=discord.Status.online))
        await asyncio.sleep(10)

        # Abwesend
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name='Dein Text', status=discord.Status.idle))
        await asyncio.sleep(10)

        # Nicht stören
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name='Dein Text', status=discord.Status.dnd))
        await asyncio.sleep(10)

        # Streaming
        await bot.change_presence(activity=discord.Streaming(name='Dein Text', url="https://www.twitch.tv/"))
        await asyncio.sleep(10)

        # Spielt
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Dein Text'))
        await asyncio.sleep(10)

        # Hört zu
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Dein Text"))
        await asyncio.sleep(10)

        # Schaut
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Dein Text"))
        await asyncio.sleep(10)


bot.run(TOKEN)
