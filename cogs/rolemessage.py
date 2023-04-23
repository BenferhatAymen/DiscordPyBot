from discord.ext import commands, tasks
import discord
from discord.utils import get
import asyncio


#==========================================
class roleMessageCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def rmessage(self, ctx, role: discord.Role, *, message):

    sentCounter = 0
    notSentCounter = 0

    role = get(ctx.guild.roles, id=role.id)

    for user in ctx.guild.members:
      try:
        if role in user.roles:
          if user.dm_channel is None:
            await user.create_dm()
          await user.dm_channel.send(message)
          print(f"sent to {user.name}")
          await asyncio.sleep(1)
          sentCounter += 1
      except Exception as e:
        print(e)
        notSentCounter += 1
    await ctx.send(
      f"Message sent to **{str(sentCounter)}** members and not sent to **{str(notSentCounter)}** members"
    )


async def setup(bot):
  await bot.add_cog(roleMessageCommands(bot))
