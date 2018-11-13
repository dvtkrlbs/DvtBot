import discord
from discord.ext import commands


class DebugCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.guild_only()
    async def get_channel(self, ctx, channel: discord.TextChannel):
        await ctx.send(type(channel.id))


def setup(bot):
    bot.add_cog(DebugCog(bot))