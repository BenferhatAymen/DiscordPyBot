from discord.ext import commands, tasks
import discord
from random import choice, randint
from random import shuffle
from modules.blkom import animeList, animeData
from PIL import Image, ImageFilter
import time
import requests
import asyncio
import difflib
import json
import os
with open('database/blkomused.txt', 'r') as f:
  usedAnimes = f.readlines()


class StoryQuiz(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  
  async def story(self, ctx, number=None):

    if number == None:
      page = randint(0, 4)
    else:
      page = int(number)

    try:
      randomAnime = animeData(choice(animeList(page=page)))
    except Exception as e:
      print(e)

    AnimeName = randomAnime[0][0] + '\n'
    if AnimeName in usedAnimes:

      used = True
      notUsedAnime = randomAnime

    else:
      used = False
      notUsedAnime = randomAnime

    while used == True:
      notUsedAnime = animeData(choice(animeList(page=page)))
      await ctx.send(notUsedAnime)

      newAnimename = notUsedAnime[0] + '\n'

      if newAnimename in usedAnimes:
        used = True

      else:
        used = False

    AnimeNames = notUsedAnime[0]

    AnimeStory = notUsedAnime[1][0]

    embed = discord.Embed(title="Guess The Anime ! ",
                          description="You have 20s To Guess The Anime ! ",
                          color=0x00EE48)
    embed.add_field(name="The Story", value=f"**{AnimeStory}**", inline=True)

    embed.set_footer(text='Bot By Hadjaymen Baroud | DZO#5994',
                     icon_url=self.bot.user.avatar)
    await ctx.send(embed=embed)
    try:
      boolList = []
      similarityList = []

      def check(msg):
        if msg.author.id == self.bot.user.id or msg.channel.id != ctx.channel.id:
          return False
        if True:

          def check_true(answerText):

            similarity = difflib.SequenceMatcher(
              None, msg.content.lower(),
              answerText.lower().rstrip().lstrip()).ratio()
            ratio = 0
            if len(answerText) <= 10:
              ratio = 0.80
            elif len(answerText) > 10 and len(answerText) < 20:
              ratio = 0.60

            elif len(answerText) >= 20 and len(answerText) < 30:
              ratio = 0.45

            elif len(answerText) >= 30:
              ratio = 0.35
            if similarity >= ratio:
              boolList.append(True)
              similarityList.append(similarity)
              return True
            return False

        checkList = map(check_true, AnimeNames)
        if True in checkList:
          return True
        return False

    except Exception as e:
      print(e)
    try:
      msg = await self.bot.wait_for('message', check=check, timeout=20)
      await ctx.send(f'Congrats ,{msg.author.mention}  answered right  ')
      with open("database/storypoints.json") as f:

        players = json.load(f)
      id = str(msg.author.name)
      players.setdefault("players", {})
      ids = players["players"].keys()
      if id in ids:
        players["players"][id] += 1
      else:

        players["players"][id] = 1

      with open('database/storypoints.json', 'w') as f:
        json.dump(players, f, ensure_ascii=False, indent=4)

    except asyncio.TimeoutError:
      embod = discord.Embed(title="No one answered ! ",
                            description='The answers are :  **{}** '.format(
                              ' / '.join(i for i in AnimeNames)),
                            color=0x00EE48)

      embod.set_footer(text='Bot By Hadjaymen Baroud | DZO#5994',
                       icon_url=self.bot.user.avatar)
      await ctx.send(embed=embod)

    with open('database/blkomused.txt', 'a+') as f:
      f.write(notUsedAnime[0][0] + '\n')


async def setup(bot):
  await bot.add_cog(StoryQuiz(bot))
