import discord
from discord.ext import commands
import asyncio


class FunCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def combine(self, ctx, left: discord.Emoji, middle: discord.Emoji, right: discord.Emoji):
        await ctx.message.delete()
        msg = await ctx.send(f'{left}                                             {right}')
        await asyncio.sleep(0.3)
        await msg.edit(content=f'{left}                           {right}')
        await msg.edit(content=f'{left}                  {right}')
        await msg.edit(content=f'{left}         {right}')
        await msg.edit(content=f'{left}{right}')
        await msg.edit(content=f'{middle}')
        await asyncio.sleep(1.5)
        await msg.delete()


def setup(bot):
    bot.add_cog(FunCog(bot))
