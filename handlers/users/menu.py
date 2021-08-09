from typing import Text
from aiogram.types import CallbackQuery
from loader import dp
from keyboards.default.genderKeyboard import markupuz, markupru, markupen

@dp.callback_query_handler(text='uz')
async def lang_uz(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Anonim suhbatga xush kelibsiz, 👤 <b>{call.from_user.full_name}</b>!\nIltimos, jinsingizni tanlang 🔽", reply_markup=markupuz, parse_mode='html')   
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='ru')
async def lang_uz(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Добро пожаловать в анонимный чат, 👤 <b>{call.from_user.full_name}</b>!\nПожалуйста, выберите ваш пол 🔽", reply_markup=markupru, parse_mode='html')   
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='en')
async def lang_uz(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Welcome to Anonymous Chat, 👤 <b>{call.from_user.full_name}</b>!\nPlease choose your gender 🔽", reply_markup=markupen, parse_mode='html')   
    await call.answer(cache_time=60)