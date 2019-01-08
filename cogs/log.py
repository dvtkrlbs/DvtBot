import discord
from discord.ext import commands
from .utils.utils import get_log_channel
from typing import Union
from .utils import embeds


class LogCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_message_delete(self, message: discord.Message):
        log_channel = get_log_channel(message.guild)
        if message.author.bot:
            return
        if message.content.startswith('!'):
            return
        for att in message.attachments:
            await log_channel.send(f'{message.author.display_name} deleted attachment {att.proxy_url}')
        # await log_channel.send(f'{message.author.display_name} deleted message `\'{message.content}\'`')
        embed = await embeds.message_delete_embed(self, message)
        await log_channel.send(embed=embed)

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

    # async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
    #     log_channel = get_log_channel(self.bot.get_guild(payload.guild_id))
    #     # message = await self.bot.get_channel(payload.channel_id).get_message(payload.message_id)
    #     # await log_channel.send(f'Reaction removed: {self.bot.get_user(payload.user_id)} removed `{payload.emoji.name}` from message: `{message.content}` from {message.author}')
    #     embed = await embeds.reaction_remove_embed(self, payload)
    #     await log_channel.send(embed=embed)

    async def on_member_ban(self, guild: discord.Guild, user: Union[discord.User, discord.Member]):
        log_channel = get_log_channel(guild)
        await log_channel.send(f'User banned: {user.name}')

    async def on_member_unban(self, guild: discord.Guild, user: Union[discord.User, discord.Member]):
        log_channel = get_log_channel(guild)
        await log_channel.send(f'User unbanned: {user.name}')

    async def on_member_join(self, member):
        log_channel = get_log_channel(member.guild)
        await log_channel.send(f'Member joined: {member.name}')

    async def on_member_remove(self, member):
        log_channel = get_log_channel(member.guild)
        await log_channel.send(f'Member left (or kicked): {member.name}')

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
