from loader import dp
from aiogram.types import CallbackQuery
from keyboards.default.menuKeyboard import menu

@dp.callback_query_handler(text='age1')
async def lang_uz(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"👤 <b>{call.from_user.full_name}</b> muvvafaqiyatli ro'yhatdan o'tdingiz!", reply_markup=menu, parse_mode='html')   
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='age2')
async def lang_uz(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"👤 <b>{call.from_user.full_name}</b> muvvafaqiyatli ro'yhatdan o'tdingiz!", reply_markup=menu, parse_mode='html')   
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='age3')
async def lang_uz(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"👤 <b>{call.from_user.full_name}</b> muvvafaqiyatli ro'yhatdan o'tdingiz!", reply_markup=menu, parse_mode='html')   
    await call.answer(cache_time=60)