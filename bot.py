from discord.ext import commands
from settings import DISCORD_TOKEN
import sys
import traceback
import logging


initial_extensions = ['cogs.mod',
                      'cogs.log',
                      'cogs.admin',
                      'cogs.fun']


class DvtBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('!'))
        self.add_command(self.ping)
        for ext in initial_extensions:
            try:
                self.load_extension(ext)
            except Exception as e:
                print(f'Failed to load {ext}', file=sys.stderr)
                traceback.print_exc()
    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.send('Pong!')


# logging.basicConfig(level=logging.DEBUG)
bot = DvtBot()
bot.run(DISCORD_TOKEN)
