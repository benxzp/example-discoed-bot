import discord
from discord.ext import commands
from discord.ext import tasks
import random
from itertools import cycle
import youtube_dl
import ffmpeg
from discord.voice_client import VoiceClient
import asyncio


@client.event
async def on_ready():
	change_status.start()
	await client.change_presence(status=discord.Status.idle)
	print('Bot is ready LETS GO')

client.run('ODYzNTIwODQyMDc1ODY1MTI5.YOoGdA.kHOdf2hQ8PFMQV47VzGH23wJDao')