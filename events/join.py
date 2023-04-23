import discord
from discord.ext import commands, tasks
from discord.utils import get


class onMemberJoin(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = discord.utils.get(member.guild.channels, id=1045364894628859955)
    if channel is not None:
      emb = discord.Embed(
        title='Welcome   to   ...',
        description=
        f"**Hi there {member.mention}, Welcome to the ... server !** \n Don't forget to read the rules here  <@rulesroomid> and Thanks !",
        color=0x00EE48)

      await channel.send(embed=emb)


async def setup(bot):
  await bot.add_cog(onMemberJoin(bot))
