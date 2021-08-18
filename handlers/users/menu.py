from typing import Text
from aiogram.types import CallbackQuery
from loader import dp, bot
from data.config import CHANNELS
from keyboards.inline.subscription import check_button_uz, check_button_ru, check_button_en


@dp.callback_query_handler(text='uz')
async def lang_uz(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"

    await call.message.answer(f"Quyidagi kanallarga obuna bo'ling: \n\n"
                         f"{channels_format}",
                         reply_markup=check_button_uz,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text='ru')
async def lang_uz(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"

    await call.message.answer(f"Подпишитесь на следующие каналы: \n\n"
                         f"{channels_format}",
                         reply_markup=check_button_ru,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text='en')
async def lang_uz(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=60)
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"

    await call.message.answer(f"Subscribe to the following channels: \n\n"
                         f"{channels_format}",
                         reply_markup=check_button_en,
                         disable_web_page_preview=True)