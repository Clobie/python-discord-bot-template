# core/core.py

import discord
from discord.ext import commands
from utils.config import cfg
from utils.log import logger
from utils.embed import embed
from utils.cog import cog

class Core:
    def __init__(self):
        self.bot = commands.Bot(command_prefix=cfg.COMMAND_PREFIX, intents=discord.Intents.all())
        self.cfg = cfg
        self.logger = logger
        self.embed = embed
        self.cog = cog

    async def run(self):
        logger.info('Starting bot...')
        self.bot.remove_command("help")
        async with self.bot:
            await cog.load_cogs(self.bot)
            await self.bot.start(cfg.BOT_TOKEN)

core = Core()