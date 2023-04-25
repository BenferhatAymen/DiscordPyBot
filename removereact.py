from discord.ext import commands, tasks
import discord

#----------------------------


class RemoveReact(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_reaction_add(self, reaction, user):
    try:
      if str(reaction.emoji) == '💀':
        message = reaction.message
        
        await message.clear_reaction(reaction)
        
        
    except Exception as e:
      print(e)


async def setup(bot):
  await bot.add_cog(RemoveReact(bot))
