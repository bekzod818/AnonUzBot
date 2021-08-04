from aiogram import types
from loader import dp, bot, db


def stop():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("👤 Suhbatdosh qidirish")
    markup.add(item1)
    return markup


@dp.message_handler(commands=['stop'])
async def stop_chat(message: types.Message):
    chat_info = db.get_active_chat(message.chat.id)
    if chat_info != False:
        db.delete_chat(chat_info[0])
        await bot.send_message(chat_info[1], '❌ Suhbatdosh suhbatni tark etdi\n\n👤 Yangi suhbatdosh qidirish: /search', reply_markup=stop())
        await bot.send_message(message.chat.id, '❌ Siz suhbatni tark etdingiz\n\n👤 Yangi suhbatdosh qidirish: /search', reply_markup=stop())
    else:
        await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!\n\n👤 Yangi suhbatdosh qidirish: /search')
