from settings import LOG_CHANNEL


def get_log_channel(guild):
    channel = guild.get_channel(int(LOG_CHANNEL))
    return channel
