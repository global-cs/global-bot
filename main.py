import discord
import random
from discord.ext import commands 

client = commands.Bot(command_prefix=".",intents=discord.Intents.all())

@client.event
async def on_ready(): 
    print("Initialised")
    print("----------------------------")


@client.event
async def on_member_join(member):
    channel = client.get_channel(1251593647972159681)
    embed=discord.Embed(title="Welcome!",description=f"{member.mention} Just Joined")
    await channel.send(embed=embed)

client.run("bot_id")
