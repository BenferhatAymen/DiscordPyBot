from discord.ext import commands, tasks
import discord


class BrodCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def brod(self, ctx, *, message):

    members = ctx.guild.members
    successfulCounter = 0
    badCounter = 0
    for member in members:

      try:

        await member.send(f'**{message}**')
        await ctx.reply('sent to {}'.format(member.mention))
        successfulCounter += 1
      except Exception as e:
        print(e)
        badCounter += 1
    await ctx.reply(f'**sent to {successfulCounter} Members ** ')
    await ctx.reply(f'** not sent to {badCounter} Members ** ')


async def setup(bot):
  await bot.add_cog(BrodCommands(bot))
