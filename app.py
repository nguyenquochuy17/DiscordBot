import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

YOUR_USER_ID = 688659963052425357 # Replace with your Discord user ID
ENTRANCE_AUDIO = "join_sound.mp3"

@bot.event
async def on_voice_state_update(member, before, after):
    if member.id == YOUR_USER_ID and after.channel is not None:
        vc = await after.channel.connect()
        vc.play(discord.FFmpegPCMAudio(ENTRANCE_AUDIO))

        while vc.is_playing():
            await asyncio.sleep(1)

        await vc.disconnect()


bot.run(os.getenv("DISCORD_BOT_TOKEN"))
