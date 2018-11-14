import discord
from discord.ext import commands
from .utils.utils import get_log_channel

class LogCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_message_delete(self, message):
        log_channel = get_log_channel(message.guild)
        if message.author.bot:
            return
        if message.content.startswith('!'):
            return
        for att in message.attachments:
            await log_channel.send(f'{message.author.display_name} deleted attachment {att.proxy_url}')
        await log_channel.send(f'{message.author.display_name} deleted message `\'{message.content}\'`')

    async def on_member_update(self, before: discord.Member, after: discord.Member):
        log_channel = get_log_channel(before.guild)
        if before.name != after.name:
            await log_channel.send(f'Name {after.display_name}: {before.name}, {after.name}')
        if before.discriminator != after.discriminator:
            await log_channel.send(f'Discriminator: {after.display_name}: {before.discriminator}, {after.discriminator}')
        if before.status != after.status:
            await log_channel.send(f'Status: {after.display_name}: {before.status}, {after.status}')
        if before.nick != after.nick:
            await log_channel.send(f'Nick: {after.display_name}: {before.nick or before.name}, {after.nick or after.name}')
        if before.avatar != after.avatar:
            await log_channel.send(f'Avatar: {after.display_name}: {before.avatar_url}, {after.avatar_url}')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def debug(self, ctx, member: discord.Member):
        try:
            await ctx.send(f'{super(member.activity.__class__, member.activity)}')
            await ctx.send(f'{isinstance(member.activity, discord.Streaming)}')
        except Exception as e:
            await ctx.send(e)

def setup(bot):
    bot.add_cog(LogCog(bot))


