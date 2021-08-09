from aiogram import types
from loader import dp, bot, db
from keyboards.default.menuKeyboard import menu
from keyboards.default.stopKeyboard import stop
from keyboards.inline.users_age import inline_markup


@dp.message_handler(content_types=['text'])
async def do_bot(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Erkak 👨':
            if db.set_gender(message.chat.id, 'male'):
                await bot.send_message(message.chat.id, '✅ Sizning jinsingiz muvaffaqiyatli qo\'shildi!\n\n🤫 Yoshingiz oralig\'ini tanlang\n',
                                 reply_markup=inline_markup)
            else:
                await bot.send_message(message.chat.id,
                                 f'✅ Sizning jinsingiz muvaffaqiyatli qo\'shildi!\n\n🤫 Yoshingiz oralig\'ini tanlang\n', reply_markup=inline_markup)

        elif message.text == 'Ayol 👩‍🦱':
            if db.set_gender(message.chat.id, 'female'):
                await bot.send_message(message.chat.id, '✅ Sizning jinsingiz muvaffaqiyatli qo\'shildi!\n\n🤫 Yoshingiz oralig\'ini tanlang\n',
                                 reply_markup=inline_markup)
            else:
                await bot.send_message(message.chat.id,
                                 f'✅ Sizning jinsingiz muvaffaqiyatli qo\'shildi!\n\n🤫 Yoshingiz oralig\'ini tanlang\n', reply_markup=inline_markup)

        elif message.text == '👤 Suhbatdosh qidirish':
            user_info = db.get_chat()
            chat_two = user_info[0]

            if db.create_chat(message.chat.id, chat_two) == False:
                db.add_queue(message.chat.id, db.get_gender(message.chat.id))
                await message.answer("👻 Suhbatdosh qidirilmoqda", reply_markup=stop)
            else:
                msg = '👤 Suhbatdosh topildi\n\n/next - yangi suhbatdosh qidirish\n/stop - suhbatni to\'xtatish'
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.row('❌ Bekor qilish')
                await bot.send_message(message.chat.id, msg, reply_markup=markup)
                await bot.send_message(chat_two, msg, reply_markup=markup)
        
        elif message.text == '❌ Bekor qilish':
            chat_info = db.get_active_chat(message.chat.id)
            if chat_info != False:
                db.delete_chat(chat_info[0])
                await bot.send_message(chat_info[1], '❌ Suhbatdosh suhbatni tark etdi\n\n/search - Yangi suhbatdosh qidirish', reply_markup=menu)
                await bot.send_message(message.chat.id, '❌ Siz suhbatni tark etdingiz\n\n/search - Yangi suhbatdosh qidirish', reply_markup=menu)
            else:
                await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!\n\n/search - Yangi suhbatdosh qidirish')


        elif message.text == "❌ Qidirishni to'xtatish":
            db.delete_queue(message.chat.id)
            await bot.send_message(message.chat.id, '❌ Qidiruv to\'xtatildi', reply_markup=menu)
        
        else:
            if db.get_active_chat(message.chat.id) != False:
                chat_info = db.get_active_chat(message.chat.id)
                await  bot.send_message(chat_info[1], message.text)
            else:
                await bot.send_message(message.chat.id, '❌ Siz suhbatni boshlamadingiz!')