import logging

from aiogram import Bot, Dispatcher, executor, types


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
    [types.KeyboardButton(text='Теория📚'),
     types.KeyboardButton(text='Билеты🚗')],
    [types.KeyboardButton(text='Квиз🚦'),
     types.KeyboardButton(text='Справка📃'),
     types.KeyboardButton(text='Статистика📊')]
]
buttonsQuiz = [
    [types.KeyboardButton(text='quiz1'),
     types.KeyboardButton(text='quiz2')],
    [types.KeyboardButton(text='quiz3'),
     types.KeyboardButton(text='Назад...')]
]

buttonsTheory = [
    [types.KeyboardButton(text='Theory1'),
     types.KeyboardButton(text='Theory2')],
    [types.KeyboardButton(text='Theory3'),
     types.KeyboardButton(text='Назад...')]
]

buttonsStatistic = [
    [types.KeyboardButton(text='Statistic1'),
     types.KeyboardButton(text='Statistic2')],
    [types.KeyboardButton(text='Statistic3'),
     types.KeyboardButton(text='Назад...')]
]

buttonsRef = [
    [types.KeyboardButton(text='Ref1'),
     types.KeyboardButton(text='Ref2')],
    [types.KeyboardButton(text='Ref3'),
     types.KeyboardButton(text='Назад...')]
]

keyboardStart = types.ReplyKeyboardMarkup(keyboard=buttonsStartKB, resize_keyboard=True)
keyboardBilets = types.ReplyKeyboardMarkup(keyboard=buttonsBilets, resize_keyboard=True)
keyboardQuiz = types.ReplyKeyboardMarkup(keyboard=buttonsQuiz, resize_keyboard=True)
keyboardTheory = types.ReplyKeyboardMarkup(keyboard=buttonsTheory, resize_keyboard=True)
keyboardStatistic = types.ReplyKeyboardMarkup(keyboard=buttonsStatistic, resize_keyboard=True)
keyboardRef = types.ReplyKeyboardMarkup(keyboard=buttonsRef, resize_keyboard=True)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет!\nЯ бот DriveMeNuts!", reply_markup=keyboardStart)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_message(message: types.Message):
    match message.text:
        case 'Билеты🚗':
            await message.answer("temp", reply_markup=keyboardBilets)
        case 'Квиз🚦':
            await message.answer("temp", reply_markup=keyboardQuiz)
        case 'Теория📚':
            await message.answer('temp', reply_markup=keyboardTheory)
        case 'Справка📃':
            await message.answer('temp', reply_markup=keyboardRef)
        case 'Статистика📊':
            await message.answer("temp", reply_markup=keyboardStatistic)
        case 'Назад...':
            await message.answer("Меню", reply_markup=keyboardStart)
        case _:
            await message.answer("temp")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
