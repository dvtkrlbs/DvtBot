import discord
from typing import Union
import datetime

async def message_delete_embed(cog, message: discord.Message) -> discord.Embed:
    embed = discord.Embed(title=f'{message.author.name}', colour=message.author.color, description=f'{message.content}', timestamp=message.created_at)

    embed.set_author(name="Message Delete", icon_url="https://cdn1.iconfinder.com/data/icons/round-ui/123/47-512.png")
    embed.set_footer(text=f'{message.id}', icon_url=f'{message.author.avatar_url}')

    return embed

async def member_update_embed(cog, before: discord.Member, after: discord.Member) -> discord.Embed:
    pass

async def reaction_remove_embed(cog, payload: discord.RawReactionActionEvent) -> discord.Embed:
    reactor = cog.bot.get_user(payload.user_id)
    message = await cog.bot.get_channel(payload.channel_id).get_message(payload.message_id)
    embed = discord.Embed(title=f'{payload.emoji.name}', color=reactor.color, description=f'**{reactor.name}** ```{message.content}```')
    embed.set_author(name="Reaction Remove", icon_url="https://cdn1.iconfinder.com/data/icons/round-ui/123/47-512.png")
    embed.set_footer(text=f'{reactor.id}', icon_url=f'{reactor.avatar_url}')

    return embed

async def member_ban_unban_embed(cog, guild: discord.Guild, user: Union[discord.User, discord.Member], is_ban: bool) -> discord.Embed:
    pass

async def member_join_remove_embed(cog, member: discord.Member, is_join: bool) -> discord.Embed:
    pass
