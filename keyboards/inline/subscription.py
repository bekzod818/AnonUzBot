from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


check_button_uz = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✔️ Obunani tekshirish", callback_data="check_subs_uz")
    ]]
)

check_button_ru = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✔️ Проверить подписку", callback_data="check_subs_ru")
    ]]
)

check_button_en = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✔️ Check subscription", callback_data="check_subs_en")
    ]]
)