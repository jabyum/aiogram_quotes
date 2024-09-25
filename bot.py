from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message
from buttons import *
bot_router = Router()

@bot_router.message(CommandStart())
async def start(message:Message):
    user_id = message.from_user.id
    await message.bot.send_message(user_id,
                                   "Привет", reply_markup=await button1())

