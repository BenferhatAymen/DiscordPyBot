import discord
from discord.ext import commands
import datetime


class ServerinfoCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        try:

            name = str(ctx.guild.name)

            owner = ctx.guild.owner.mention
            id = str(ctx.guild.id)

            memberCount = str(ctx.guild.member_count)

            icon = str(ctx.guild.icon)
            list_of_bots = [
                bot.mention for bot in ctx.guild.members if bot.bot]

            roleCount = len(ctx.guild.roles)

            verification_level = str(ctx.guild.verification_level)

            textChannels = len(ctx.guild.text_channels)

            voiceChannels = len(ctx.guild.voice_channels)

            categories = len(ctx.guild.categories)

            totalChannels = textChannels + voiceChannels

            createdAt = ctx.guild.created_at.__format__('%A, %d. %B %Y')

            highestRole = ctx.guild.roles[-1].mention
            # ---------------------
            embed = discord.Embed(title="INFOS",
                                  color=0xffdf00,
                                  timestamp=datetime.datetime.utcnow())

            embed.add_field(name="Owner", value=owner, inline=True)
            embed.add_field(name="Server ID", value=id, inline=True)
            embed.add_field(name="Verification Level",
                            value=verification_level,
                            inline=True)

            embed.add_field(name="Member Count",
                            value=memberCount, inline=True)
            embed.add_field(name="Role Count", value=roleCount, inline=True)
            embed.add_field(name="Bots", value=len(list_of_bots), inline=True)
            embed.add_field(name="textChannels",
                            value=textChannels, inline=True)
            embed.add_field(name="VoiceChannels",
                            value=voiceChannels, inline=True)

            embed.add_field(name="Total Channels",
                            value=totalChannels, inline=True)

            embed.add_field(name="Categories", value=categories, inline=True)

            embed.add_field(name="Guild Created at: ",
                            value=createdAt, inline=True)

            embed.add_field(name="Highest Role ",
                            value=highestRole, inline=True)

            embed.set_footer(text=f'Requested by {ctx.author.name}',
                             icon_url=ctx.author.avatar)

            embed.set_author(name=name + " Server Informations",
                             icon_url=self.bot.user.avatar)

            if icon not in [None, "None", "none"]:
                embed.set_image(url=icon)

            await ctx.send(embed=embed)
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(ServerinfoCommand(bot))
