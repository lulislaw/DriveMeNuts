import logging
import random
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputMediaPhoto
from aiogram.dispatcher import FSMContext
import datetime
import boards
import strings
import tickets
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from fun.config import Config
import statdb

config = Config()

logging.basicConfig(level=logging.INFO)
API_TOKEN = config.token

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
statdb.create_user_table()
theoryCallbacksArray = ['0'] * 26
for i in range(0, 26):
    theoryCallbacksArray[i] = 'theoryChapter' + str(i)

with open("src/theory/theoryPickedIntro.txt", encoding='utf-8') as file:
    theoryPickedIntro = file.read()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message.from_user.full_name)
    statdb.new_user(message.chat.id)
    await message.answer(strings.hello_message, reply_markup=boards.keyboard_start)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_message(message: types.Message, state: FSMContext):
    if 'В ' in message.text:
        data = await state.get_data()
        id_chat = message.chat.id
        id_message = data.get(f'{id_chat.__str__()}message')
        cur_quest = int(message.text.split(' ')[1]) - 1
        await state.update_data({f'{id_chat.__str__()}quest': cur_quest})
        print(cur_quest)
        list_quests = data.get(f'{message.chat.id.__str__()}list')
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        if os.path.exists(list_quests[cur_quest].image):
            with open(list_quests[cur_quest].image, 'rb') as photo:
                new_photo = InputMediaPhoto(media=photo)
                await bot.edit_message_media(chat_id=id_chat, message_id=id_message, media=new_photo)
        else:
            with open('src/bilets/img/other/noImage.jpg', 'rb') as photo:
                new_photo = InputMediaPhoto(media=photo)
                await bot.edit_message_media(chat_id=id_chat, message_id=id_message, media=new_photo)
        if (list_quests[cur_quest].ready):
            new_text = f'{list_quests[cur_quest].num}\n{list_quests[cur_quest].text}\n{list_quests[cur_quest].a1}\n{list_quests[cur_quest].a2}\n{list_quests[cur_quest].a3}\n{list_quests[cur_quest].a4}\n{list_quests[cur_quest].a5}\n{list_quests[cur_quest].descript}'
            new_text = new_text[:1023]
            await bot.edit_message_caption(chat_id=id_chat, message_id=id_message, caption=new_text)
            await bot.edit_message_reply_markup(chat_id=id_chat, message_id=id_message,
                                                reply_markup=boards.keyboard_next_prev)
        else:
            new_text = f'{list_quests[cur_quest].num}\n{list_quests[cur_quest].text}\n{list_quests[cur_quest].a1}\n{list_quests[cur_quest].a2}\n{list_quests[cur_quest].a3}\n{list_quests[cur_quest].a4}\n{list_quests[cur_quest].a5}'
            await bot.edit_message_caption(chat_id=id_chat, message_id=id_message, caption=new_text)
            await bot.edit_message_reply_markup(chat_id=id_chat, message_id=id_message,
                                                reply_markup=boards.getAnsKeyBoard(list_quests, cur_quest))



    else:
        match message.text:
            case 'Билеты🚗':
                await message.answer(strings.bilets_message, reply_markup=boards.keyboard_bilets)
            case 'Билеты АВ':
                with open('src/bilets/img/other/BiletsAB.jpg', 'rb') as photo:
                    caption = 'Билеты AB'
                    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=caption,
                                         reply_markup=boards.keyboard_ab)
            case 'Квиз🚦':
                await message.answer("temp", reply_markup=boards.keyboard_quiz)
            case 'Теория📚':
                await message.answer(theoryPickedIntro, reply_markup=boards.keyboard_theory, parse_mode="html")
            case 'Справка📃':
                await message.answer('temp', reply_markup=boards.keyboard_ref)
            case 'Экзамен':
                list_quests = tickets.get_bilet_by_exam()
                cur_quest = 0
                new_text = f'{list_quests[cur_quest].text}\n{list_quests[cur_quest].a1}\n{list_quests[cur_quest].a2}\n{list_quests[cur_quest].a3}\n{list_quests[cur_quest].a4}\n{list_quests[cur_quest].a5}'
                current_time = datetime.datetime.now()
                await bot.send_message(chat_id=message.chat.id,
                                       text=current_time.strftime('Начало %H:%M:%S\nЭкзамен'),
                                       reply_markup=boards.create_reply_keyboard(len(list_quests)))
                await bot.delete_message(chat_id=message.chat.id,
                                         message_id=message.message_id)
                if os.path.exists(list_quests[cur_quest].image):
                    with open(list_quests[cur_quest].image, 'rb') as photo:
                        quest_message = await bot.send_photo(chat_id=message.chat.id, photo=photo,
                                                             caption=new_text,
                                                             reply_markup=boards.getAnsKeyBoard(list_quests, 0))
                else:
                    with open('src/bilets/img/other/noImage.jpg', 'rb') as photo:
                        quest_message = await bot.send_photo(chat_id=message.chat.id, photo=photo,
                                                             caption=new_text,
                                                             reply_markup=boards.getAnsKeyBoard(list_quests, 0))

                await state.update_data({
                    f'{message.chat.id.__str__()}quest': 0,
                    f'{message.chat.id.__str__()}message': quest_message.message_id,
                    f'{message.chat.id.__str__()}list': list_quests})
            case 'Статистика📊':
                lst_stat = statdb.get_stat_results(message.chat.id)
                lst_theme = statdb.get_stat_stattheme(message.chat.id)
                temp_str = ''
                count_ready_bilets = 0
                for i, stat in enumerate(lst_stat):
                    if sum(stat) == 20:
                        count_ready_bilets += 1
                    temp_str = f'{temp_str}Билет №{i + 1} {sum(stat)}/40\t'
                temp_str = f'{temp_str}\n\n'
                for theme in lst_theme:
                    temp_str = f'{temp_str}\n{theme[0]} : {theme[1]}/{theme[2]}'
                await message.answer(f'Выполненно : {count_ready_bilets}/40\n{temp_str}')
            case 'Назад...':
                await message.answer("Меню", reply_markup=boards.keyboard_start)
            case 'Закончить':
                await message.answer("Вы не ответили на все вопросы\nТочно ли вы хотите закончить?",
                                     reply_markup=boards.keyboard_yes_or_no)
            case 'Темы':
                await message.answer(f'Темы:\n{strings.theme}', reply_markup=boards.keyboard_theme)
            case _:
                await message.answer("temp")


# Задается хэндлер и список колбэков которые его вызывают
@dp.callback_query_handler(text=theoryCallbacksArray)
async def callback_theory(query: types.CallbackQuery):
    # Получаем текст кнопки, чтобы по ней потом подбирать файл
    buttonText = query.data
    await bot.answer_callback_query(query.id)
    # Отправляем файл через парный элемент колбэка в словаре theoryFilesDict
    with open(f'src/theory/pdf/{strings.theoryFilesDict[buttonText][0]}.pdf', 'rb') as file:
        await bot.send_document(query.from_user.id, file, caption=f"Теория. Выбранный раздел:"
                                                                  f" \"{strings.theoryFilesDict[buttonText][1]}\"")


@dp.callback_query_handler(lambda c: c.data.startswith('theme'))
async def process_callback_button_theme(callback_query: types.CallbackQuery, state: FSMContext):
    bilet_number = int(callback_query.data.split('heme_')[1])
    list_quests = tickets.get_bilet_by_theme(strings.theme_list[bilet_number - 1])
    cur_quest = 0
    new_text = f'{list_quests[cur_quest].text}\n{list_quests[cur_quest].a1}\n{list_quests[cur_quest].a2}\n{list_quests[cur_quest].a3}\n{list_quests[cur_quest].a4}\n{list_quests[cur_quest].a5}'
    current_time = datetime.datetime.now()
    await bot.send_message(chat_id=callback_query.message.chat.id, text=current_time.strftime('Начало %H:%M:%S'),
                           reply_markup=boards.create_reply_keyboard(len(list_quests)))
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    if os.path.exists(list_quests[cur_quest].image):
        with open(list_quests[cur_quest].image, 'rb') as photo:
            quest_message = await bot.send_photo(chat_id=callback_query.message.chat.id, photo=photo, caption=new_text,
                                                 reply_markup=boards.getAnsKeyBoard(list_quests, 0))
    else:
        with open('src/bilets/img/other/noImage.jpg', 'rb') as photo:
            quest_message = await bot.send_photo(chat_id=callback_query.message.chat.id, photo=photo, caption=new_text,
                                                 reply_markup=boards.getAnsKeyBoard(list_quests, 0))

    await state.update_data({
        f'{callback_query.message.chat.id.__str__()}quest': 0,
        f'{callback_query.message.chat.id.__str__()}message': quest_message.message_id,
        f'{callback_query.message.chat.id.__str__()}list': list_quests})


@dp.callback_query_handler(lambda c: c.data.startswith('biletAB'))
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    bilet_number = callback_query.data.split('AB')[1]
    if bilet_number == '0':
        bilet_number = random.randrange(1, 21)
    list_quests = tickets.get_bilet_by_id(bilet_number)
    cur_quest = 0
    new_text = f'{list_quests[cur_quest].num}\n{list_quests[cur_quest].text}\n{list_quests[cur_quest].a1}\n{list_quests[cur_quest].a2}\n{list_quests[cur_quest].a3}\n{list_quests[cur_quest].a4}\n{list_quests[cur_quest].a5}'
    current_time = datetime.datetime.now()
    await bot.send_message(chat_id=callback_query.message.chat.id, text=current_time.strftime('Начало %H:%M:%S'),
                           reply_markup=boards.create_reply_keyboard(len(list_quests)))
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    if os.path.exists(list_quests[cur_quest].image):
        with open(list_quests[cur_quest].image, 'rb') as photo:
            quest_message = await bot.send_photo(chat_id=callback_query.message.chat.id, photo=photo, caption=new_text,
                                                 reply_markup=boards.getAnsKeyBoard(list_quests, 0))
    else:
        with open('src/bilets/img/other/noImage.jpg', 'rb') as photo:
            quest_message = await bot.send_photo(chat_id=callback_query.message.chat.id, photo=photo, caption=new_text,
                                                 reply_markup=boards.getAnsKeyBoard(list_quests, 0))
    await state.update_data({
        f'{callback_query.message.chat.id.__str__()}quest': 0,
        f'{callback_query.message.chat.id.__str__()}message': quest_message.message_id,
        f'{callback_query.message.chat.id.__str__()}list': list_quests})


@dp.callback_query_handler(lambda c: c.data in ['realnoFinish', 'otmenaFinisha'])
async def process_callback_finish(callback_query: types.CallbackQuery, state: FSMContext):
    if ('realno' in callback_query.data):
        data = await state.get_data()
        id_message = data.get(f'{callback_query.message.chat.id.__str__()}message')
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=id_message)
        await bot.send_message(chat_id=callback_query.message.chat.id, text='Меню', reply_markup=boards.keyboard_start)
        statdb.set_cell_stat(callback_query.message.chat.id,
                             data.get(f'{callback_query.message.chat.id.__str__()}list'))

    else:
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(lambda c: c.data in ['nextQuest', 'prevQuest'])
async def process_callback_nextprev(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    id_chat = callback_query.message.chat.id
    id_message = data.get(f'{callback_query.message.chat.id.__str__()}message')
    cur_quest = data.get(f'{callback_query.message.chat.id.__str__()}quest')
    list_quests = data.get(f'{callback_query.message.chat.id.__str__()}list')
    quest_id = f'{callback_query.message.chat.id.__str__()}quest'
    print(cur_quest)

    if ('next' in callback_query.data and cur_quest != 19):
        await state.update_data({quest_id: cur_quest + 1})
        cur_quest += 1
    elif ('prev' in callback_query.data and cur_quest != 0):
        await state.update_data({quest_id: cur_quest - 1})
        cur_quest -= 1
    if (cur_quest != -1 and cur_quest != 20):  # -1 и 20 ?????

        if os.path.exists(list_quests[cur_quest].image):
            with open(list_quests[cur_quest].image, 'rb') as photo:
                new_photo = InputMediaPhoto(media=photo)
                await bot.edit_message_media(chat_id=id_chat, message_id=id_message, media=new_photo)

        else:
            with open('src/bilets/img/other/noImage.jpg', 'rb') as photo:
                new_photo = InputMediaPhoto(media=photo)
                await bot.edit_message_media(chat_id=id_chat, message_id=id_message, media=new_photo)

        if (list_quests[cur_quest].ready):
            new_text = f'{list_quests[cur_quest].num}\n{list_quests[cur_quest].text}\n{list_quests[cur_quest].a1}\n{list_quests[cur_quest].a2}\n{list_quests[cur_quest].a3}\n{list_quests[cur_quest].a4}\n{list_quests[cur_quest].a5}\n{list_quests[cur_quest].descript}'
            new_text = new_text[:1023]
            await bot.edit_message_caption(chat_id=id_chat, message_id=id_message, caption=new_text)
            await bot.edit_message_reply_markup(chat_id=id_chat, message_id=id_message,
                                                reply_markup=boards.keyboard_next_prev)
        else:
            new_text = f'{list_quests[cur_quest].num}\n{list_quests[cur_quest].text}\n{list_quests[cur_quest].a1}\n{list_quests[cur_quest].a2}\n{list_quests[cur_quest].a3}\n{list_quests[cur_quest].a4}\n{list_quests[cur_quest].a5}'
            await bot.edit_message_caption(chat_id=id_chat, message_id=id_message, caption=new_text)
            await bot.edit_message_reply_markup(chat_id=id_chat, message_id=id_message,
                                                reply_markup=boards.getAnsKeyBoard(list_quests, cur_quest))


@dp.callback_query_handler(lambda c: c.data in ['ans1', 'ans2', 'ans3', 'ans4', 'ans5'])
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    bilet_id = f'{callback_query.message.chat.id.__str__()}bilet'
    quest_id = f'{callback_query.message.chat.id.__str__()}quest'
    cur_quest = data.get(quest_id)
    list_quests = data.get(f'{callback_query.message.chat.id.__str__()}list')
    idAns = callback_query.data.split('ans')[1]
    answers = [list_quests[cur_quest].a1, list_quests[cur_quest].a2, list_quests[cur_quest].a3,
               list_quests[cur_quest].a4,
               list_quests[cur_quest].a5]
    if list_quests[cur_quest].suc in answers[(int(idAns) - 1)]:
        list_quests[cur_quest].a5 = list_quests[cur_quest].a5 + '\nВерно✅'
        list_quests[cur_quest].ready = True
    else:
        list_quests[cur_quest].a5 = list_quests[cur_quest].a5 + '\nНеверно❌'

    new_text = f'{list_quests[cur_quest].num}\n{list_quests[cur_quest].text}\n{list_quests[cur_quest].a1}\n{list_quests[cur_quest].a2}\n{list_quests[cur_quest].a3}\n{list_quests[cur_quest].a4}\n{list_quests[cur_quest].a5}\n{list_quests[cur_quest].descript}'
    new_text = new_text[:1023]

    await state.update_data({f'{callback_query.message.chat.id.__str__()}list': list_quests})
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                                   caption=new_text)

    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=boards.keyboard_next_prev)
    if all(item.ready for item in list_quests):
        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text="Вы ответили на все вопросы\nХотите ли вы закончить?",
                               reply_markup=boards.keyboard_yes_or_no)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
