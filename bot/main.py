import os
import discord
from discord.ext import commands
from config import settings as cfg
from bot.utils.logger import log

intents = discord.Intents.all()
bot = Bot(
    command_prefix=cfg.BOT_PREFIX, 
    intents=intents
)

# move this to the help cog after it's made
#bot.remove_command("help")

async def loadcogs():
    for filename in os.listdir(cfg.DIR_COGS):
        if filename.endswith('.py') and not filename.startswith('_'):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f'cogs.{cog_name}')
            except Exception as e:
                log.log(f"Failed to load cog '{cog_name}': {str(e)}", logging.ERROR)

@bot.event
async def on_message(message):
    if message.author is bot.user:
        return
    await bot.process_commands(message)

async def main():
    token = os.getenv('BOT_SECRETS_TOKEN')
    if not token:
        log("Environment variable BOT_SECRETS_TOKEN not set. Exiting.", level=logging.ERROR)
        exit()
    log("Starting bot", level=logging.INFO)
    async with bot:
        await loadcogs()
        log.log("Waiting for the bot to be ready...")
        await bot.start(token.BOT_SECRETS_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())