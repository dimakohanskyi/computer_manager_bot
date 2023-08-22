import os
from dotenv import load_dotenv
import pyautogui as pg
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from try_ose import (open_chrome, open_edge,
                     open_discord, open_telegram, open_steam, home_page,
                     open_binance, open_spotify, open_trello)

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

home_page_b = KeyboardButton('Desktop💻')
open_chrome_b = KeyboardButton('Chrome🌐')
open_edge_b = KeyboardButton('Edge🌐')
open_discord_b = KeyboardButton('Discord📞')
open_telegram_b = KeyboardButton('Telegram📱')
open_steam_b = KeyboardButton('Steam🎮')
open_trello_b = KeyboardButton('Trello📌')
open_binance_b = KeyboardButton('Binance📈')
open_spotify_b = KeyboardButton('Spotify🎧')
make_screen_b = KeyboardButton('ScreenShot📺')

reply_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(open_chrome_b, open_edge_b, open_discord_b,
                                                             open_telegram_b, open_steam_b, make_screen_b,
                                                             open_trello_b, open_spotify_b, open_binance_b,
                                                             home_page_b)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Choose an option:", reply_markup=reply_markup)


@dp.message_handler(lambda message: message.text == 'Desktop')
async def open_chrome_handler(message: types.Message):
    await message.answer("Opening desktop...")
    home_page()


@dp.message_handler(lambda message: message.text == 'Chrome')
async def open_chrome_handler(message: types.Message):
    await message.answer("Opening Chrome...")
    open_chrome()


@dp.message_handler(lambda message: message.text == 'Edge')
async def open_chrome_handler(message: types.Message):
    await message.answer("Opening Edge browser...")
    open_edge()


@dp.message_handler(lambda message: message.text == 'Discord')
async def open_chrome_handler(message: types.Message):
    await message.answer("Opening Discord...")
    open_discord()


@dp.message_handler(lambda message: message.text == 'Telegram')
async def open_chrome_handler(message: types.Message):
    await message.answer("Opening Telegram...")
    open_telegram()


@dp.message_handler(lambda message: message.text == 'Steam')
async def open_chrome_handler(message: types.Message):
    await message.answer("Opening Steam...")
    open_steam()


@dp.message_handler(lambda message: message.text == 'Binance')
async def open_chrome_handler(message: types.Message):
    await message.answer("Opening Binance...")
    open_binance()


@dp.message_handler(lambda message: message.text == 'Trello')
async def open_chrome_handler(message: types.Message):
    await message.answer("Opening Trello...")
    open_trello()


@dp.message_handler(lambda message: message.text == 'Spotify')
async def open_chrome_handler(message: types.Message):
    await message.answer("Opening Spotify...")
    open_spotify()


async def take_screenshot_and_send(chat_id):
    screenshot = pg.screenshot()
    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)

    with open(screenshot_path, 'rb') as photo:
        await bot.send_photo(chat_id, photo)

    os.remove(screenshot_path)


@dp.message_handler(lambda message: message.text == 'ScreenShot')
async def screenshot_handler(message: types.Message):
    await take_screenshot_and_send(message.chat.id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
