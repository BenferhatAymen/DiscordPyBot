from discord.ext import commands, tasks
import discord
import requests
import os
import datetime


class RoleinfoCommand(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def roleinfo(self, ctx, *, role: discord.Role = None):
    if role == None:
      await ctx.send('Please Speciefy a role ! ')
      return
    roleid = str(role.id)
    rolecreation = role.created_at.__format__('%A, %d. %B %Y')
    roleposition = str(role.position)
    rolecolor = str(role.color)
    ifmentionable = str(role.mentionable)
    membercount = len(role.members)
    members = []
    for i in role.members:
      members.append(i.mention)

    embed = discord.Embed(title=f'{role.name}\'s Informations',
                          description='',
                          color=0xffdf00,
                          timestamp=datetime.datetime.utcnow())
    embed.set_author(name="INFO", icon_url=self.bot.user.avatar)
    embed.add_field(name="RoleID: ", value=roleid, inline=True)
    embed.add_field(name="Created at: ", value=rolecreation, inline=True)
    embed.add_field(name="Role Color: ", value=rolecolor, inline=True)
    embed.add_field(name="Mentionable: ", value=ifmentionable, inline=True)
    embed.add_field(name="Role Position: ", value=roleposition, inline=True)
    embed.add_field(name="Member Count",
                    value=f'''{membercount}''',
                    inline=True)
    embed.add_field(name="Members",
                    value=', '.join(f'<@{str(member.id)}>'
                                    for member in role.members),
                    inline=True)

    embed.set_footer(text=f'Requested by {ctx.author.name}',
                     icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)


async def setup(bot):
  await bot.add_cog(RoleinfoCommand(bot))
