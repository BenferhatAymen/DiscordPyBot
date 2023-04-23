from discord.ext import commands, tasks
import discord
import requests
from os import remove
from random import choice
import time
import json
from PIL import Image, ImageDraw, ImageFont


class FastTyper(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def first(self, ctx):
    embid = discord.Embed(
      title='Fast Typer Game !!! ',
      description=
      f'In This game you need to be the first one who type the word appears every 2 seconds'
    )
    embid.set_image(
      url=
      'https://media.discordapp.net/attachments/851792852753186818/851840177571233842/unknown.png?width=322&height=184'
    )
    misg = await ctx.send(embed=embid)

    time.sleep(1)

    if 5 > 1:
      embed2 = discord.Embed(
        title='Be Ready !',
        description=f'Please Choose The number of rounds you want to play !')
      embed2.set_image(
        url=
        'https://media.discordapp.net/attachments/851792852753186818/851840177571233842/unknown.png?width=322&height=184'
      )
      await misg.edit(embed=embed2)
      time.sleep(1)

      def check(m):
        return m.author == ctx.author

      msg = await self.bot.wait_for('message', check=check)
      try:
        if int(msg.content) >= 8 or int(msg.content) <= 0:
          await misg.delete()
          await ctx.send('**Please set a  number between 1 and 8 !**')

        elif isinstance(int(msg.content), int):
          rounds = int(msg.content)
      except:
        await ctx.send('**Please set a valid number!**')

    await misg.delete()

    for i in range(0, rounds):
      f = open('database/wordlist.txt', 'r')
      wordlist = f.read().splitlines()

      randomstr = choice(wordlist)
      fontsize = 0
      imgW, imgH = ((0, 0))
      if len(randomstr) <= 2:
        fontsize = 120
        imgW, imgH = ((114, 84))
      elif len(randomstr) == 3:
        fontsize = 120
        imgW, imgH = ((102, 90))

      elif len(randomstr) < 5:
        fontsize = 120
        imgW, imgH = ((95, 90))
      elif len(randomstr) >= 5 and len(randomstr) <= 9:
        fontsize = 70
        imgW, imgH = ((102, 110))
      else:
        fontsize = 50
        imgW, imgH = ((70, 112))

      font = ImageFont.truetype('pillow/kungfumastersemital.ttf', fontsize)
      image = Image.open('pillow/background.png')
      d = ImageDraw.Draw(image)
      d.text((imgW, imgH), randomstr, font=font, fill=(255, 255, 0))
      image.save(f'pic{i}.png')
      file = discord.File(f'pic{i}.png')
      emb = discord.Embed(title="Type it FAST !", color=0xffdf00)
      emb.set_image(url=f'attachment://pic{i}.png')
      await ctx.send(embed=emb, file=file)
      remove(f'pic{i}.png')

      def check(m):
        return m.content.lower() == randomstr.lower(
        ) and m.channel == ctx.channel

      msg = await self.bot.wait_for('message', check=check)
      midz = await ctx.send(
        "**Correct answer !** {.author.mention}".format(msg))
      time.sleep(2)
      with open("database/points.json") as f:
        players = json.load(f)
      id = str(msg.author.name)
      players.setdefault("players", {})
      ids = players["players"].keys()
      if id in ids:
        players["players"][id] += 1
      else:

        players["players"][id] = 1

      with open('database/points.json', 'w') as f:
        json.dump(players, f, ensure_ascii=False, indent=4)
    with open('database/points.json') as f:
      players = json.load(f)
    try:
      embod = discord.Embed(title='Leaderboard')
      sort_leader = sorted(players["players"].items(),
                           key=lambda x: x[1],
                           reverse=True)
      print(sort_leader)
      index = 1
      for i in sort_leader:

        embod.add_field(name=f'{index}) {i[0]}', value=f'Points: {i[1]}')

        index += 1
      embod.set_footer(text='SYC#7287', icon_url = self.bot.user.avatar)
      embod.set_image(
        url=
        'https://media.discordapp.net/attachments/851792852753186818/851840177571233842/unknown.png?width=322&height=184'
      )
    except Exception as e:
      print(e)
    try:
      await ctx.send(embed=embod)
    except Exception as e:
      print(e)

    del players["players"]

    with open('database/points.json', 'w') as f:
      json.dump(players, f, ensure_ascii=False, indent=4)


async def setup(bot):
  await bot.add_cog(FastTyper(bot))
