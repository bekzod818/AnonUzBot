from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.inline.set_lang import inline_markup


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer('🇺🇿 Tillardan birini tanlang\n🇷🇺 Выберите один из языков\n🏴󠁧󠁢󠁥󠁮󠁧󠁿 Choose one of the languages\n', reply_markup=inline_markup)
