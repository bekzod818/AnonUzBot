from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Erkak 👨', 'Ayol 👩‍🦱')
    await message.answer(
        f"Anonim suhbatga xush kelibsiz, <b>{message.from_user.full_name}</b>!\nIltimos, jinsingizni tanlang 🔽",
        reply_markup=markup, parse_mode='html')
