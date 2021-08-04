from aiogram import types
from loader import dp, bot, db


def stop_search():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("❌ Qidirishni to'xtatish")
    markup.add(item1)
    return markup


@dp.message_handler(commands=['search'])
async def search_user(message: types.Message):
    user_info = db.get_chat()
    chat_two = user_info[0]

    if db.create_chat(message.chat.id, chat_two) == False:
        db.add_queue(message.chat.id, db.get_gender(message.chat.id))
        await message.answer("👻 Suhbatdosh qidirilmoqda", reply_markup=stop_search())
    else:
        msg = '👤 Suhbatdosh topildi\n\n/next - yangi suhbatdosh qidirish\n/stop - suhbatni to\'xtatish'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('❌ Bekor qilish')
        await bot.send_message(message.chat.id, msg, reply_markup=markup)
        await bot.send_message(chat_two, msg, reply_markup=markup)
