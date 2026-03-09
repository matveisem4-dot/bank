import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Берем токен из Secret
API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Кнопки выбора ОС
def get_os_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🤖 Android", callback_data="os:android")],
        [InlineKeyboardButton(text="🍎 iOS / iPhone", callback_data="os:ios")],
        [InlineKeyboardButton(text="💻 Windows PC", callback_data="os:windows")]
    ])

@dp.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer(
        "💎 **ALISA PRIVATE NETWORK V56**\n"
        "Статус: **Dedicated Server (Germany) — Online**\n\n"
        "Выберите платформу для мгновенной настройки:",
        reply_markup=get_os_kb(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data.startswith("os:"))
async def tune_os(callback: CallbackQuery):
    os_name = callback.data.split(":")[1]
    # Прямая ссылка на прокси (без лишних переходов)
    links = {
        "android": "https://t.me/proxy?server=162.19.163.43&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
        "ios": "https://t.me/proxy?server=5.135.161.164&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
        "windows": "https://t.me/proxy?server=exp.proxy.com&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d"
    }
    
    res_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🟢 ПОДКЛЮЧИТЬ", url=links[os_name])]
    ])
    
    await callback.message.edit_text(
        f"✅ **ПРОФИЛЬ {os_name.upper()} СКОНФИГУРИРОВАН**\n"
        "Скорость: 1 Гбит/с\n\n"
        "Нажмите кнопку ниже:",
        reply_markup=res_kb,
        parse_mode="Markdown"
    )

async def main():
    # ГЛАВНОЕ: очищаем все зависшие запросы
    await bot.delete_webhook(drop_pending_updates=True)
    print(">>> ALISA VPN: Бот успешно запущен и очередь очищена.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
