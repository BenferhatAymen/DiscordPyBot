import discord
from discord.ext import commands, tasks
import glob
from discord.ext.commands import cooldown, BucketType
import os
import asyncio
import random
#------------------------------------------------
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="#",
                      case_insensitive=True,
                      intents=intents)

#------------------------------------------------


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,
                               activity=discord.Game("Hi !"))
  print("\nLogged in as", client.user, ': ', client.user.id, "\n")


@client.command()
async def ping(ctx):
  await ctx.send("Pong ! ")


#------------------------------------------------
dirs = ["cogs", "fun","events","animecommands"]


async def load_extensions(dir):
  for filename in os.listdir(f"./{dir}"):
    if filename.endswith(".py"):

      await client.load_extension(f"{dir}.{filename[:-3]}")


async def main():
  async with client:
    for i in dirs:
      await load_extensions(i)
    await client.start(os.getenv('TOKEN'))


asyncio.run(main())
