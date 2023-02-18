import logging
import random

from aiogram import Bot, Dispatcher, executor, types
import asyncio
import time
# Configure logging
import boards
import strings
import tickets

logging.basicConfig(level=logging.INFO)
API_TOKEN = "6059259592:AAHZGLUzC7DijF6XCAnHbU1bGz4akGETYdA"
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Все инлайн-кнопки с колбэками (колбэк это значение, которое триггерит в конце callback_theory)
theoryCallbacksArray = ['0'] * 26
for i in range(0, 26):
    theoryCallbacksArray[i] = 'theoryChapter' + str(i)

with open("src/theory/theoryPickedIntro.txt") as file:
    theoryPickedIntro = file.read()

keyboardStart = types.ReplyKeyboardMarkup(keyboard=boards.buttonsStartKB, resize_keyboard=True)
keyboardBilets = types.ReplyKeyboardMarkup(keyboard=boards.buttonsBilets, resize_keyboard=True)
keyboardQuiz = types.ReplyKeyboardMarkup(keyboard=boards.buttonsQuiz, resize_keyboard=True)
keyboardTheory = types.InlineKeyboardMarkup(inline_keyboard=boards.buttonsTheory, resize_keyboard=True)
keyboardStatistic = types.ReplyKeyboardMarkup(keyboard=boards.buttonsStatistic, resize_keyboard=True)
keyboardRef = types.ReplyKeyboardMarkup(keyboard=boards.buttonsRef, resize_keyboard=True)
keyboardAB = types.InlineKeyboardMarkup(inline_keyboard=boards.buttonsBiletAB, resize_keyboard=True)
keyboardAnswers = types.InlineKeyboardMarkup(inline_keyboard=boards.buttonsAnswers, resize_keyboard=True)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет!\nЯ бот DriveMeNuts!", reply_markup=keyboardStart)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_message(message: types.Message):
    match message.text:
        case 'Билеты🚗':
            await message.answer("Выберите вариант тестирования", reply_markup=keyboardBilets)
        case 'Билеты АВ':
            await message.answer("Билеты АВ", reply_markup=keyboardAB)
        case 'Квиз🚦':
            await message.answer("temp", reply_markup=keyboardQuiz)
        case 'Теория📚':
            await message.answer(theoryPickedIntro, reply_markup=keyboardTheory, parse_mode="html")
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
    with open(f'src/theory/pdf/{strings.theoryFilesDict[button_text][0]}.pdf', 'rb') as file:
        await bot.send_document(query.from_user.id, file, caption=f"Теория. Выбранный раздел:"
                                                                  f" \"{strings.theoryFilesDict[button_text][1]}\"")


currentAsk = 0
list = []
listMistake = []

@dp.callback_query_handler(lambda c: c.data.startswith('biletAB'))
async def process_callback_button(callback_query: types.CallbackQuery):
    button_number = callback_query.data.split('AB')[1]
    global list
    global listMistake
    global currentAsk
    list = tickets.getBilet(button_number)
    currentAsk = 0
    if button_number == '0':
        button_number = random.randrange(1, 21)
    await bot.send_message(chat_id=callback_query.message.chat.id, text=f'Билет №{button_number}')
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=f'{list[currentAsk].num}\n{list[currentAsk].text}', reply_markup=keyboardAnswers)


@dp.callback_query_handler(lambda c: c.data in ['ans1', 'ans2', 'ans3', 'ans4', 'ans5'])
async def process_callback_button(callback_query: types.CallbackQuery):
    global list
    global listMistake
    global currentAsk
    currentAsk = currentAsk + 1
    print(currentAsk)
    await bot.send_message(chat_id=callback_query.message.chat.id, text=f'Ваш ответ {callback_query.data}')
    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=None)
    if(currentAsk < list.__len__()):
        await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=f'{list[currentAsk].num}\n{list[currentAsk].text}', reply_markup=keyboardAnswers)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
