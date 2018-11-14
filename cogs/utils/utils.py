from settings import LOG_CHANNEL
import discord


def get_log_channel(guild) -> discord.TextChannel:
    channel = guild.get_channel(int(LOG_CHANNEL))
    return channel
