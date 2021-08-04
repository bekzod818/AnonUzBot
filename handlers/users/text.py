from aiogram import types
from loader import dp, bot, db

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('👤 Suhbatdosh qidirish')
    markup.add(item1)
    return markup

def stop_chat():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("❌ Qidirishni to'xtatish")
    markup.add(item1)
    return markup

def stop_search():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("❌ Qidirishni to'xtatish")
    markup.add(item1)
    return markup

def stop():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("👤 Suhbatdosh qidirish")
    markup.add(item1)
    return markup


@dp.message_handler(content_types=['text'])
async def do_bot(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Erkak 👨':
            if db.set_gender(message.chat.id, 'male'):
                await bot.send_message(message.chat.id, '✅ Sizning jinsingiz muvaffaqiyatli qo\'shildi!',
                                 reply_markup=main_menu())
            else:
                await bot.send_message(message.chat.id,
                                 f'❌ Siz allaqachon jinsingizni ko\'rsatgansiz. \n🔄 Ma\'lumotlarni o\'zgartirish - /settings', reply_markup=main_menu())

        elif message.text == 'Ayol 👩‍🦱':
            if db.set_gender(message.chat.id, 'female'):
                await bot.send_message(message.chat.id, '✅ Sizning jinsingiz muvaffaqiyatli qo\'shildi!',
                                 reply_markup=main_menu())
            else:
                await bot.send_message(message.chat.id,
                                 f'❌ Siz allaqachon jinsingizni ko\'rsatgansiz. \n🔄 Ma\'lumotlarni o\'zgartirish - /settings', reply_markup=main_menu())

        elif message.text == '👤 Suhbatdosh qidirish':
            user_info = db.get_chat()
            chat_two = user_info[0]

            if db.create_chat(message.chat.id, chat_two) == False:
                db.add_queue(message.chat.id, db.get_gender(message.chat.id))
                await message.answer("👻 Suhbatdosh qidirilmoqda", reply_markup=stop_search())
            else:
                msg = '👤 Suhbatdosh topildi\n\n/next - yangi suhbatdosh qidirish\n/stop - suhbatni to\'xtatish'
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                markup.row('❌ Bekor qilish')
                await bot.send_message(message.chat.id, msg, reply_markup=markup)
                await bot.send_message(chat_two, msg, reply_markup=markup)
        
        elif message.text == '❌ Bekor qilish':
            chat_info = db.get_active_chat(message.chat.id)
            if chat_info != False:
                db.delete_chat(chat_info[0])
                await bot.send_message(chat_info[1], '❌ Suhbatdosh suhbatni tark etdi\n\n👤 Yangi suhbatdosh qidirish: /search', reply_markup=stop())
                await bot.send_message(message.chat.id, '❌ Siz suhbatni tark etdingiz\n\n👤 Yangi suhbatdosh qidirish: /search', reply_markup=stop())
            else:
                await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!\n\n👤 Yangi suhbatdosh qidirish: /search')


        elif message.text == "❌ Qidirishni to'xtatish":
            db.delete_queue(message.chat.id)
            await bot.send_message(message.chat.id, '❌ Qidiruv to\'xtatildi', reply_markup=main_menu())
        
        else:
            if db.get_active_chat(message.chat.id) != False:
                chat_info = db.get_active_chat(message.chat.id)
                await  bot.send_message(chat_info[1], message.text)
            else:
                await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!')