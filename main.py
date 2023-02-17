import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)
API_TOKEN = "6059259592:AAHZGLUzC7DijF6XCAnHbU1bGz4akGETYdA"
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

buttonsBilets = [
    [types.KeyboardButton(text='Билеты АВ'),
     types.KeyboardButton(text='Экзамен')],
    [types.KeyboardButton(text='Темы'),
     types.KeyboardButton(text='Назад...')]
]

buttonsStartKB = [
    [types.KeyboardButton(text='Билеты'),
     types.KeyboardButton(text='Квиз')],
    [types.KeyboardButton(text='Теория'),
     types.KeyboardButton(text='Справка'),
     types.KeyboardButton(text='Статистика')]
]
keyboardStart = types.ReplyKeyboardMarkup(keyboard=buttonsStartKB, resize_keyboard=True)
keyboardBilets = types.ReplyKeyboardMarkup(keyboard=buttonsBilets, resize_keyboard=True)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет!\nЯ бот DriveMeNuts!\nЕбал твою мамашу", reply_markup=keyboardStart)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
