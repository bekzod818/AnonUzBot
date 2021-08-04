from aiogram import types
from loader import dp, bot, db


@dp.message_handler(content_types=['sticker'])
async def sendsticker(message: types.Message):
    if message.chat.type == 'private':
        chat_info = db.get_active_chat(message.chat.id)
        if chat_info != False:
            await bot.send_sticker(chat_info[1], message.sticker.file_id)
        else:
            await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!')
