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
theoryCallbacksArray = ['0']*25
for i in range(0, 25):
    theoryCallbacksArray[i] = 'theoryChapter' + str(i)

theoryFilesDict = {
    "theoryChapter1": "Общие положения",
    "theoryChapter2": "Общие обязанности водителей",
    "theoryChapter3": "Применение специальных сигналов",
    "theoryChapter4": "Обязанности пешеходов",
    "theoryChapter5": "Обязанности пассажиров",
    "theoryChapter6": "Сигналы светофора и регулировщика",
    "theoryChapter7": "Применение аварийной сигнализации и знака аварийной остановки",
    "theoryChapter8": "Начало движения, маневрирование",
    "theoryChapter9": "Расположение транспортных средств на проезжей части",
    "theoryChapter10": "Скорость движения",
    "theoryChapter11": "Обгон, опережение, встречный разъезд",
    "theoryChapter12": "Остановка и стоянка",
    "theoryChapter13": "Проезд перекрестков",
    "theoryChapter14": "Пешеходные переходы и места остановок маршрутных транспортных средств",
    "theoryChapter15": "Движение через железнодорожные пути",
    "theoryChapter16": "Движение по автомагистралям",
    "theoryChapter17": "Движение в жилых зонах",
    "theoryChapter18": "Приоритет маршрутных транспортных средств",
    "theoryChapter19": "Пользование внешними световыми приборами и звуковыми сигналами",
    "theoryChapter20": "Буксировка механических транспортных средств",
    "theoryChapter21": "Учебная езда",
    "theoryChapter22": "Перевозка людей",
    "theoryChapter23": "Перевозка грузов",
    "theoryChapter24": "Дополнительные требования к движению велосипедистов и водителей мопедов",
    "theoryChapter25": "Дополнительные требования к движению гужевых повозок, а также к прогону животных"
}

buttonsTheory = [
    [types.InlineKeyboardButton(text='Вся теория', callback_data='allTheoryFile')],
    [types.InlineKeyboardButton(text='1', callback_data='theoryChapter1'),
     types.InlineKeyboardButton(text='2', callback_data='theoryChapter2'),
     types.InlineKeyboardButton(text='3', callback_data='theoryChapter3'),
     types.InlineKeyboardButton(text='4', callback_data='theoryChapter4')],
    [types.InlineKeyboardButton(text='5', callback_data='theoryChapter5'),
     types.InlineKeyboardButton(text='6', callback_data='theoryChapter6'),
     types.InlineKeyboardButton(text='7', callback_data='theoryChapter7'),
     types.InlineKeyboardButton(text='8', callback_data='theoryChapter8')],
    [types.InlineKeyboardButton(text='9', callback_data='theoryChapter9'),
     types.InlineKeyboardButton(text='10', callback_data='theoryChapter10'),
     types.InlineKeyboardButton(text='11', callback_data='theoryChapter11'),
     types.InlineKeyboardButton(text='12', callback_data='theoryChapter12')],
    [types.InlineKeyboardButton(text='13', callback_data='theoryChapter13'),
     types.InlineKeyboardButton(text='14', callback_data='theoryChapter14'),
     types.InlineKeyboardButton(text='15', callback_data='theoryChapter15'),
     types.InlineKeyboardButton(text='16', callback_data='theoryChapter16')],
    [types.InlineKeyboardButton(text='17', callback_data='theoryChapter17'),
     types.InlineKeyboardButton(text='18', callback_data='theoryChapter18'),
     types.InlineKeyboardButton(text='19', callback_data='theoryChapter19'),
     types.InlineKeyboardButton(text='20', callback_data='theoryChapter20')],
    [types.InlineKeyboardButton(text='21', callback_data='theoryChapter21'),
     types.InlineKeyboardButton(text='22', callback_data='theoryChapter22'),
     types.InlineKeyboardButton(text='23', callback_data='theoryChapter23')],
    [types.InlineKeyboardButton(text='24', callback_data='theoryChapter24'),
     types.InlineKeyboardButton(text='25', callback_data='theoryChapter25')]

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
keyboardTheory = types.InlineKeyboardMarkup(inline_keyboard=buttonsTheory, resize_keyboard=True)
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
@dp.callback_query_handler(text=theoryCallbacksArray)
async def callback_theory(query: types.CallbackQuery):
    # Получаем текст кнопки, чтобы по ней потом подбирать файл
    button_text = query.data
    await bot.answer_callback_query(query.id)
    # Отправляем файл через парный элемент колбэка в словаре theoryFilesDict
    with open(f'src/theory/pdf/{theoryFilesDict[button_text]}.pdf', 'rb') as file:
        await bot.send_document(query.from_user.id, file, caption=f"Теория {button_text}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
