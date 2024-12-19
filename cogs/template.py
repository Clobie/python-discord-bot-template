# cogs/template.py

from discord.ext import commands
from core.core import core

class TemplateCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

async def setup(bot: commands.Bot):
    await bot.add_cog(TemplateCog(bot))