from loader import dp, bot
from data.config import CHANNELS
from utils.misc import subscription
from aiogram import types
from keyboards.inline.subscription import check_button_uz, check_button_ru, check_button_en
from keyboards.default.genderKeyboard import markupuz, markupru, markupen


@dp.callback_query_handler(text="check_subs_uz")
async def checker(call: types.CallbackQuery):
    await call.answer()
    final_status = True
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            final_status *= status
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        
        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f"❌ <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lmagansiz.\n\n")
    
    if final_status:
        await call.message.delete()
        msg = f"Anonim suhbatga xush kelibsiz\n👤 <b>{call.from_user.full_name}</b>!\nIltimos, jinsingizni tanlang 🔽" 
        await call.message.answer(msg, reply_markup=markupuz)
    else:
        await call.message.delete()
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=check_button_uz)
    


@dp.callback_query_handler(text="check_subs_ru")
async def checker(call: types.CallbackQuery):
    await call.answer()
    final_status = True
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            final_status *= status
            result += f"✅ <b>{channel.title},</b> вы подписались на канал!\n\n"
        
        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f"❌ <a href='{invite_link}'><b>{channel.title},</b></a> вы не подписались на канал.\n\n")
    
    if final_status:
        await call.message.delete()
        msg = f"Добро пожаловать в анонимный чат\n👤 <b>{call.from_user.full_name}</b>!\nПожалуйста, выберите ваш пол 🔽"   
        await call.message.answer(msg, reply_markup=markupru)
    else:
        await call.message.delete()
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=check_button_ru)
    


@dp.callback_query_handler(text="check_subs_en")
async def checker(call: types.CallbackQuery):
    await call.answer()
    final_status = True
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            final_status *= status
            result += f"✅ <b>{channel.title},</b> you have subscribed to the channel!\n\n"
        
        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f"❌ <a href='{invite_link}'><b>{channel.title},</b></a> you have not subscribed to the channel.\n\n")
    
    if final_status:
        await call.message.delete()
        msg = f"Welcome to Anonymous Chat\n👤 <b>{call.from_user.full_name}</b>!\nPlease choose your gender 🔽"
        await call.message.answer(msg, reply_markup=markupen)
    else:
        await call.message.delete()
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=check_button_en)
    