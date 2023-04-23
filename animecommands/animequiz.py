from discord.ext import commands, tasks
import discord
from random import choice, randint
from random import shuffle
from modules.myanimelist import charactersList, characterData
from PIL import Image, ImageFilter
import time
import requests
import asyncio
import difflib
import json
import os
with open('database/used.txt', 'r') as f:
  usedAnimes = f.readlines()


class AnimeQuiz(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def anime(self, ctx, number=None):

    if number == None:
      limitAnimes = randint(1, 4) * 50
    else:
      limitAnimes = int(number) * 50

    try:
      randomCharacter = characterData(choice(
        charactersList(limit=limitAnimes)))
      print(randomCharacter)
    except Exception as e:
      print(e)

    characterName = randomCharacter[0][0] + '\n'
    if characterName in usedAnimes:

      used = True
      notUsedCharacter = randomCharacter

    else:
      used = False
      notUsedCharacter = randomCharacter

    while used == True:
      notUsedCharacter = characterData(
        choice(charactersList(limit=limitAnimes)))
      await ctx.send(notUsedCharacter)

      newCharactername = notUsedCharacter[0] + '\n'

      if newCharactername in usedAnimes:
        used = True

      else:
        used = False

    characterNames = notUsedCharacter[0]

    characterPicture = notUsedCharacter[1][0]

    OriImage = Image.open(requests.get(characterPicture, stream=True).raw)
    OriImage.show()

    boxImage = OriImage.filter(ImageFilter.BoxBlur(int(2)))
    boxImage.show()

    boxImage.save('boxblur.png')
    embed = discord.Embed(title="Guess The Anime ! ",
                          description="You have 20s To Guess The Anime ! ",
                          color=0x00EE48)
    file = discord.File("boxblur.png", filename="boxblur.png")
    embed.set_image(url="attachment://boxblur.png")
    embed.set_footer(text='Bot By Hadjaymen Baroud | DZO#5994',
                     icon_url=self.bot.user.avatar)
    await ctx.send(file=file, embed=embed)
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

        checkList = map(check_true, characterNames)
        if True in checkList:
          return True
        return False

    except Exception as e:
      print(e)
    try:
      msg = await self.bot.wait_for('message', check=check, timeout=20)
      await ctx.send(f'Congrats ,{msg.author.mention}  answered right  ')
      with open("database/pointa.json") as f:

        players = json.load(f)
      id = str(msg.author.name)
      players.setdefault("players", {})
      ids = players["players"].keys()
      if id in ids:
        players["players"][id] += 1
      else:

        players["players"][id] = 1

      with open('database/pointa.json', 'w') as f:
        json.dump(players, f, ensure_ascii=False, indent=4)

    except asyncio.TimeoutError:
      embod = discord.Embed(title="No one answered ! ",
                            description='The answers are :  **{}** '.format(
                              ' / '.join(i for i in characterNames)),
                            color=0x00EE48)
      embod.set_image(url=characterPicture)

      embod.set_footer(text='Bot By Hadjaymen Baroud | DZO#5994',
                       icon_url=self.bot.user.avatar)
      await ctx.send(embed=embod)

    with open('database/used.txt', 'a+') as f:
      f.write(notUsedCharacter[0][0] + '\n')
    os.remove('boxblur.png')


async def setup(bot):
  await bot.add_cog(AnimeQuiz(bot))
