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

# Все инлайн-кнопки с колбэками (колбэк это значение, которое триггерит в конце callback_theory)

buttonsTheory = [
    [types.InlineKeyboardButton(text='1', callback_data='1'),
     types.InlineKeyboardButton(text='2', callback_data='2')],
    [types.InlineKeyboardButton(text='3', callback_data='3'),
     types.InlineKeyboardButton(text='4', callback_data='4')],
    [types.InlineKeyboardButton(text='5', callback_data='5'),
     types.InlineKeyboardButton(text='6', callback_data='6')],
    [types.InlineKeyboardButton(text='7', callback_data='7'),
     types.InlineKeyboardButton(text='8', callback_data='8')],
    [types.InlineKeyboardButton(text='9', callback_data='9'),
     types.InlineKeyboardButton(text='10', callback_data='10')],
    [types.InlineKeyboardButton(text='Назад...', callback_data='back')]
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
keyboardTheory = types.InlineKeyboardMarkup(inline_keyboard=buttonsTheory, resize_keyboard = True)
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
            await message.answer('Теория', reply_markup=keyboardTheory)
        case 'Справка📃':
            await message.answer('temp', reply_markup=keyboardRef)
        case 'Статистика📊':
            await message.answer("temp", reply_markup=keyboardStatistic)
        case 'Назад...':
            await message.answer("Меню", reply_markup=keyboardStart)
        case _:
            await message.answer("temp")




# Задается хэндлер и список колбэков которые его вызывают
@dp.callback_query_handler(text=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'back'])
async def callback_theory(query: types.CallbackQuery):
    # Получаем текст кнопки, чтобы по ней потом подбирать файл
    button_text = query.data

    if query.data == 'back':
        await bot.send_message(query.from_user.id, reply_markup=keyboardStart)
    else:
        await bot.answer_callback_query(query.id)
        # Отправляем файл с соответствующим названием
        with open(f'src/theory/pdf/{button_text}.pdf', 'rb') as file:
            await bot.send_document(query.from_user.id, file, caption=f"Теория {button_text}")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
