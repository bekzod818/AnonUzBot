from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("📝 Men quyidagilarni qila olaman:",
            "",
            "/start - Botni ishga tushirish",
            "/search - Suhbatdosh qidirish",
            "/next - Yangi suhbatdosh",
            "/stop - Suhbatni to'xtatish",
            "/send_account - Profilingizni yuborish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
