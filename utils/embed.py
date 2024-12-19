# utils/common.py

import discord
from datetime import datetime
from utils.config import cfg

class Embed:
    def __init__(self):
        self.url = cfg.EMBED_URL
        self.icon_url = cfg.EMBED_ICON_URL
        self.name = cfg.BOT_NAME
        self.author = cfg.BOT_AUTHOR

    def create_embed_generic(self, title, description, color):
        embed = discord.Embed(
            title=title,
            description=description,
            colour=color,
            timestamp=datetime.now()
        )
        embed.set_author(name=self.author,url=self.url,icon_url=self.icon_url)
        embed.set_thumbnail(url=self.icon_url)
        embed.set_footer(text=self.author,icon_url=self.icon_url)
        return embed

    def create_embed_error(self, title, description):
        return self.create_embed_generic(f"Error: {title}", description, cfg.ERRORCOLOR)
    
    def create_embed_info(self, title, description):
        return self.create_embed_generic(f"Info: {title}", description, cfg.INFOCOLOR)

    def create_embed(self, title, description):
        return self.create_embed_generic(title, description, cfg.PRIMARYCOLOR)
    
embed = Embed()