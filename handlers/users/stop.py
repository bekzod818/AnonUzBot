from aiogram import types
from loader import dp, bot, db
from keyboards.default.menuKeyboard import menu


@dp.message_handler(commands=['stop'])
async def stop_chat(message: types.Message):
    chat_info = db.get_active_chat(message.chat.id)
    if chat_info != False:
        db.delete_chat(chat_info[0])
        await bot.send_message(chat_info[1], '❌ Suhbatdosh suhbatni tark etdi\n\n/search - Yangi suhbatdosh qidirish', reply_markup=menu)
        await bot.send_message(message.chat.id, '❌ Siz suhbatni tark etdingiz\n\n/search - Yangi suhbatdosh qidirish', reply_markup=menu)
    else:
        await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!\n\n/search - Yangi suhbatdosh qidirish', reply_markup=menu)
