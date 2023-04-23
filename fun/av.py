from discord.ext import commands, tasks
import discord
import random
import asyncio
#==========================


class TruthorDare(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def av(self, ctx):
    try:

      emb = discord.Embed(
        title='Truth or Dare !',
        description=f'React with ⭕ to join \nyou have 10s to join ✅',
        color=0x00EE48)
      emb.add_field(name=f"Remaining Time : ", value=f"**10s**", inline=False)
      ok = '⭕'
      msg = await ctx.send(embed=emb)
      await msg.add_reaction(ok)

      for i in range(2, 11, 2):
        emb2 = discord.Embed(
          title='Truth or Dare !',
          description=f'React with  ⭕ to join \nyou have 10s to join ✅',
          color=0x00EE48)
        emb2.add_field(name=f"Remaining Time : ",
                       value=f"**{str(10-i)}s**",
                       inline=False)

        await asyncio.sleep(2)
        await msg.edit(embed=emb2)

      getmsg = await ctx.fetch_message(msg.id)
      users = [
        user async for user in getmsg.reactions[0].users()
        if user != self.bot.user
      ]

      team = []
      random.shuffle(team)
      try:
        for user in users:
          team.append(user.id)

        c = random.choice(team)
        team.remove(c)
        c2 = random.choice(team)

        emb3 = discord.Embed(title='Truth or Dare !',
                             description=f'Participants are : ',
                             color=0x00EE48)
        emb3.add_field(name=f"Who asks :", value=f"<@{c}>", inline=False)
        emb3.add_field(name=f"Who answers :", value=f"<@{c2}>", inline=False)
        await msg.edit(embed=emb3)

      except:
        emb = discord.Embed(
          title='Sorry !',
          description=f'The number of participants should be more than 1 ! ',
          color=0x00EE48)
        await msg.edit(embed=emb)

    except Exception as e:
      print(e)


async def setup(bot):
  await bot.add_cog(TruthorDare(bot))
