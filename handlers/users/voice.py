from aiogram import types
from loader import dp, bot, db


@dp.message_handler(content_types=['voice'])
async def sendsticker(message: types.Message):
    if message.chat.type == 'private':
        chat_info = db.get_active_chat(message.chat.id)
        if chat_info != False:
            await bot.send_voice(chat_info[1], message.voice.file_id)
        else:
            await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!')
