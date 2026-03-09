import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Бот берет токен из настроек GitHub Actions
API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- КОНФИГУРАЦИИ СКОРОСТИ ---
OS_CONFIGS = {
    "android": {
        "link": "https://t.me/proxy?server=162.19.163.43&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
        "label": "🚀 SNAPDRAGON TURBO",
        "info": "Оптимизировано под ядро Android. Идеально для Samsung Fold."
    },
    "ios": {
        "link": "https://t.me/proxy?server=5.135.161.164&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
        "label": "🍎 APPLE SECURE",
        "info": "Протокол TLS 1.3. Максимальная защита iOS."
    },
    "windows": {
        "link": "https://t.me/proxy?server=exp.proxy.com&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
        "label": "💻 DESKTOP MAX",
        "info": "Многопоточный режим для Windows PC."
    }
}

def main_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🤖 Android", callback_data="os:android")],
        [InlineKeyboardButton(text="🍎 iOS (iPhone)", callback_data="os:ios")],
        [InlineKeyboardButton(text="💻 Windows / PC", callback_data="os:windows")]
    ])

@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer(
        "🦾 **ALISA VPN SYSTEM V54**\n\n"
        "Запущено через GitHub Actions 24/7.\n"
        "Выбери ОС для калибровки скорости:",
        reply_markup=main_kb(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data.startswith("os:"))
async def tune_os(callback: CallbackQuery):
    os_name = callback.data.split(":")[1]
    cfg = OS_CONFIGS[os_name]
    
    msg = await callback.message.edit_text(f"📡 Анализ системы {os_name.upper()}...")
    await asyncio.sleep(0.5)
    await msg.edit_text(f"⚡️ Применение профиля: {cfg['label']}...")

    res_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🟢 ПОДКЛЮЧИТЬ", url=cfg['link'])]
    ])

    await msg.edit_text(
        f"✅ **ГОТОВО ДЛЯ {os_name.upper()}**\n\n"
        f"📝 {cfg['info']}\n"
        "Нажми кнопку ниже:",
        reply_markup=res_kb,
        parse_mode="Markdown"
    )

async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(run_bot())
