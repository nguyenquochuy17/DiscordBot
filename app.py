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

# Map of user ID to their entrance audio file
USER_ENTRANCE_AUDIO = {
    688659963052425357: "join_sound.mp3",  # You
    688386424612847618: "ht2.mp3"          # Your friend
}

@bot.event
async def on_voice_state_update(member, before, after):
    # Only act if the user is in our dictionary and they joined/moved voice channels
    if member.id in USER_ENTRANCE_AUDIO and before.channel != after.channel and after.channel is not None:
        audio_file = USER_ENTRANCE_AUDIO[member.id]

        try:
            vc = await after.channel.connect()
        except discord.ClientException:
            # Already connected to a channel
            return

        vc.play(discord.FFmpegPCMAudio(audio_file))

        while vc.is_playing():
            await asyncio.sleep(1)

        await vc.disconnect()

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
