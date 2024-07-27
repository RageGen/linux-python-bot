import asyncio
from aiogram import Bot, Dispatcher
from bot_parts.handlers import router
from os import getenv
bot=Bot(getenv('TOKEN'))
dp=Dispatcher()
    
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())