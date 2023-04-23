from discord.ext import commands, tasks
import discord

#----------------------------


class Test(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def cogtest(self, ctx):
    await ctx.send("Test test !")


async def setup(bot):
  await bot.add_cog(Test(bot))
