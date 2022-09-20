import os
import configparser
import discord
from yt_dlp import YoutubeDL

config = configparser.ConfigParser()
config.read(os.path.abspath("config.ini"))

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
    if str(message.channel) in config['PROD']['CHANNELS'].split(","):
        if 'https://vm.tiktok.com/' in message.content:
            url = [url for url in message.content.split(" ") if "https://vm.tiktok.com/" in url][0]
            print(url)
            ydl_opts = {'outtmpl': "videos\\"+(url.split("https://vm.tiktok.com/")[1].split("/")[0])+'.mp4', 'format': 'download_addr-0'}
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            file = discord.File(os.path.abspath(str(ydl_opts['outtmpl']['default'])), filename=str(ydl_opts['outtmpl']['default']))
            await message.channel.send(file=file)
        elif 'https://www.tiktok.com/' in message.content:
            url = [url for url in message.content.split(" ") if "https://www.tiktok.com/" in url][0]
            print(url)
            ydl_opts = {'outtmpl': "videos\\"+(url.split("video/")[1].split("?")[0])+'.mp4', 'format': 'download_addr-0'}
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            file = discord.File(os.path.abspath(str(ydl_opts['outtmpl']['default'])), filename=str(ydl_opts['outtmpl']['default']))
            await message.channel.send(file=file)

client.run(config['PROD']['DISCORDBOT_TOKEN'])