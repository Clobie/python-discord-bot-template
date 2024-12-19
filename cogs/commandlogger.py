# cogs/commandlogger.py

from discord.ext import commands
from core.core import core

class CommandLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            core.logger.info(f'Command not found: {ctx.message.content}')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing required argument.')
            core.logger.info(f'Missing required argument in command: {ctx.message.content}')
        else:
            await ctx.send(f'{str(error)}')
            core.logger.error(f'An error occurred: {str(error)}')
            raise error

    @commands.Cog.listener()
    async def on_command(self, ctx):
        server_name = getattr(ctx.guild, 'name', 'DM')
        channel_name = getattr(ctx.channel, 'name', 'Direct Message')
        command_content = ctx.message.content.encode('unicode_escape').decode('utf-8')
        channel_id = ctx.channel.id
        user_info = f"{ctx.author.name} (ID: {ctx.author.id})" if ctx.guild else f"{ctx.author.name} (ID: {ctx.author.id})"
        core.logger.info(f"Command '{command_content}' entered by {user_info} in {server_name} ({channel_name}) [channel id: {channel_id}]")

async def setup(bot):
    await bot.add_cog(CommandLogger(bot))