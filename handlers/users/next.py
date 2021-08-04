from aiogram import types
from loader import dp, bot, db
from keyboards.default.stopKeyboard import stop


@dp.message_handler(commands=['next'])
async def stop_chat(message: types.Message):
    chat_info = db.get_active_chat(message.chat.id)
    
    if chat_info != False:
        db.delete_chat(chat_info[0])
        await bot.send_message(chat_info[1], '❌ Suhbatdosh suhbatni tark etdi\n\n/search - Yangi suhbatdosh qidirish', reply_markup=types.ReplyKeyboardRemove())
    else:
        await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!\n\n/search - Yangi suhbatdosh qidirish', reply_markup=types.ReplyKeyboardRemove())

    
    user_info = db.get_chat()
    chat_two = user_info[0]

    if db.create_chat(message.chat.id, chat_two) == False:
        db.add_queue(message.chat.id, db.get_gender(message.chat.id))
        await message.answer("👻 Suhbatdosh qidirilmoqda", reply_markup=stop)
    else:
        msg = '👤 Suhbatdosh topildi\n\n/next - yangi suhbatdosh qidirish\n/stop - suhbatni to\'xtatish'
        await bot.send_message(message.chat.id, msg, reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(chat_two, msg, reply_markup=types.ReplyKeyboardRemove())