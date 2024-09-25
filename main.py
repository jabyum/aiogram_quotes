from aiogram import Bot, Dispatcher
import asyncio
from bot import bot_router
bot = Bot(token="6849219345:AAFcDrJ-NC1FxsfoKqat672eAltYQe9RMpc")
dp = Dispatcher()
async def main():
    dp.include_router(bot_router)
    await dp.start_polling(bot)

asyncio.run(main())

