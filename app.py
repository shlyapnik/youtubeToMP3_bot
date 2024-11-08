import asyncio
import logging
from loader import bot, dp
from handlers import user

async def main():
    logging.basicConfig(level=logging.INFO)
    
    dp.include_router(user.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 