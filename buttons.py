
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

async def button1():
    buttons = [[KeyboardButton(text="Hello")],
               [KeyboardButton(text="Bye")]]
    kb = ReplyKeyboardMarkup(resize_keyboard=True,
                             keyboard=buttons)
    return kb

