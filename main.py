# main.py

import asyncio
from core.core import core

async def main():
    await core.run()

asyncio.run(main())