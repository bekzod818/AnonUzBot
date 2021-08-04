from aiogram import types
from loader import dp, bot, db


@dp.message_handler(commands=['send_account'])
async def send_your_account(message: types.Message):
    chat_info = db.get_active_chat(message.chat.id)
    if chat_info != False:
        if message.from_user.username:
            await bot.send_message(chat_info[1], '@' + message.from_user.username)
            await bot.send_message(message.chat.id, '✅ Sizning profil suhbatdoshga yuborildi')
        else:
            await bot.send_message(message.chat.id,
                             '❌ Telegram profilingizni username yo\'q, oldin username kiriting.')
    else:
        await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!')