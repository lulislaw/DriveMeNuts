from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from typing import Optional


def getPartOfButtons(startInt, endInt, name, callback):
    list = []
    for i in range(startInt, endInt + 1):
        list.append(types.KeyboardButton(text=f'{name}{i}', callback_data=f'{callback}{i}'))
    return list


def create_reply_keyboard(num_buttons):
    MAX_BUTTONS_PER_ROW = 4
    num_cols = min(num_buttons, MAX_BUTTONS_PER_ROW)
    num_rows = (num_buttons + num_cols - 1) // num_cols

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Закончить"))

    for i in range(num_rows):
        row_buttons = []
        for j in range(num_cols):
            button_index = i * num_cols + j
            if button_index >= num_buttons:
                break
            button_text = f"В {button_index + 1}"
            row_buttons.append(KeyboardButton(button_text))
        keyboard.row(*row_buttons)

    return keyboard


buttons_theme = [
    [types.InlineKeyboardButton(text='1', callback_data='theme_1'),
     types.InlineKeyboardButton(text='2', callback_data='theme_2'),
     types.InlineKeyboardButton(text='3', callback_data='theme_3'),
     types.InlineKeyboardButton(text='4', callback_data='theme_4')],
    [types.InlineKeyboardButton(text='5', callback_data='theme_5'),
     types.InlineKeyboardButton(text='6', callback_data='theme_6'),
     types.InlineKeyboardButton(text='7', callback_data='theme_7'),
     types.InlineKeyboardButton(text='8', callback_data='theme_8')],
    [types.InlineKeyboardButton(text='9', callback_data='theme_9'),
     types.InlineKeyboardButton(text='10', callback_data='theme_10'),
     types.InlineKeyboardButton(text='11', callback_data='theme_11'),
     types.InlineKeyboardButton(text='12', callback_data='theme_12')],
    [types.InlineKeyboardButton(text='13', callback_data='theme_13'),
     types.InlineKeyboardButton(text='14', callback_data='theme_14'),
     types.InlineKeyboardButton(text='15', callback_data='theme_15'),
     types.InlineKeyboardButton(text='16', callback_data='theme_16')],
    [types.InlineKeyboardButton(text='17', callback_data='theme_17'),
     types.InlineKeyboardButton(text='18', callback_data='theme_18'),
     types.InlineKeyboardButton(text='19', callback_data='theme_19'),
     types.InlineKeyboardButton(text='20', callback_data='theme_20')],
    [types.InlineKeyboardButton(text='21', callback_data='theme_21'),
     types.InlineKeyboardButton(text='22', callback_data='theme_22'),
     types.InlineKeyboardButton(text='23', callback_data='theme_23'),
     types.InlineKeyboardButton(text='24', callback_data='theme_24')],
    [types.InlineKeyboardButton(text='25', callback_data='theme_25'),
     types.InlineKeyboardButton(text='26', callback_data='theme_26')]

]

buttons_theory = [
    [types.InlineKeyboardButton(text='Вся теория', callback_data='theoryChapter0')],
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

buttons_bilet_ab = [
    [types.InlineKeyboardButton(text='Случайный', callback_data='biletAB0')],
    [types.InlineKeyboardButton(text='1', callback_data='biletAB1'),
     types.InlineKeyboardButton(text='2', callback_data='biletAB2'),
     types.InlineKeyboardButton(text='3', callback_data='biletAB3'),
     types.InlineKeyboardButton(text='4', callback_data='biletAB4')],
    [types.InlineKeyboardButton(text='5', callback_data='biletAB5'),
     types.InlineKeyboardButton(text='6', callback_data='biletAB6'),
     types.InlineKeyboardButton(text='7', callback_data='biletAB7'),
     types.InlineKeyboardButton(text='8', callback_data='biletAB8')],
    [types.InlineKeyboardButton(text='9', callback_data='biletAB9'),
     types.InlineKeyboardButton(text='10', callback_data='biletAB10'),
     types.InlineKeyboardButton(text='11', callback_data='biletAB11'),
     types.InlineKeyboardButton(text='12', callback_data='biletAB12')],
    [types.InlineKeyboardButton(text='13', callback_data='biletAB13'),
     types.InlineKeyboardButton(text='14', callback_data='biletAB14'),
     types.InlineKeyboardButton(text='15', callback_data='biletAB15'),
     types.InlineKeyboardButton(text='16', callback_data='biletAB16')],
    [types.InlineKeyboardButton(text='17', callback_data='biletAB17'),
     types.InlineKeyboardButton(text='18', callback_data='biletAB18'),
     types.InlineKeyboardButton(text='19', callback_data='biletAB19'),
     types.InlineKeyboardButton(text='20', callback_data='biletAB20')],

]

buttons_set_quest = [
    getPartOfButtons(1, 10, 'В ', 'quest_'),
    getPartOfButtons(11, 20, 'В ', 'quest_'),
    [types.KeyboardButton(text='Закончить', callback_data='finish')]
]

buttons_statistic = [
    [types.KeyboardButton(text=f'Билеты AB'),
     types.KeyboardButton(text=f'Темы')],
    [types.KeyboardButton(text='Назад...')]
]

buttons_ref = [
    [types.KeyboardButton(text='Ref1'),
     types.KeyboardButton(text='Ref2')],
    [types.KeyboardButton(text='Ref3'),
     types.KeyboardButton(text='Назад...')]
]

buttons_bilets = [
    [types.KeyboardButton(text='Билеты АВ'),
     types.KeyboardButton(text='Экзамен')],
    [types.KeyboardButton(text='Темы'),
     types.KeyboardButton(text='Назад...')]
]

buttons_start = [
    [types.KeyboardButton(text='Теория📚'),
     types.KeyboardButton(text='Билеты🚗')],
    [types.KeyboardButton(text='Квиз🚦'),
     types.KeyboardButton(text='Справка📃'),
     types.KeyboardButton(text='Статистика📊')]
]
buttons_quiz = [
    [types.KeyboardButton(text='quiz1'),
     types.KeyboardButton(text='quiz2')],
    [types.KeyboardButton(text='quiz3'),
     types.KeyboardButton(text='Назад...')]
]
buttons_yn = [
    [types.InlineKeyboardButton(text='Завершить', callback_data='realnoFinish'),
     types.InlineKeyboardButton(text='Отмена', callback_data='otmenaFinisha')]
]
buttons_np = [
    [
        types.InlineKeyboardButton(text='Назад', callback_data='prevQuest'),
        types.InlineKeyboardButton(text='Дальше', callback_data='nextQuest')]
]


def getAnsKeyBoard(lst, x):
    buttons_answers = []
    if lst[x].a4 == "":
        buttons_answers = [
            [types.InlineKeyboardButton(text='1', callback_data='ans1'),
             types.InlineKeyboardButton(text='2', callback_data='ans2'),
             types.InlineKeyboardButton(text='3', callback_data='ans3')]
        ]
    elif lst[x].a5 == "":
        buttons_answers = [
            [types.InlineKeyboardButton(text='1', callback_data='ans1'),
             types.InlineKeyboardButton(text='2', callback_data='ans2'),
             types.InlineKeyboardButton(text='3', callback_data='ans3'),
             types.InlineKeyboardButton(text='4', callback_data='ans4')]
        ]
    else:
        buttons_answers = [
            [types.InlineKeyboardButton(text='1', callback_data='ans1'),
             types.InlineKeyboardButton(text='2', callback_data='ans2'),
             types.InlineKeyboardButton(text='3', callback_data='ans3'),
             types.InlineKeyboardButton(text='4', callback_data='ans4'),
             types.InlineKeyboardButton(text='5', callback_data='ans5')]
        ]

    keyboard_answers = types.InlineKeyboardMarkup(inline_keyboard=buttons_answers, resize_keyboard=True)
    return keyboard_answers


keyboard_start = types.ReplyKeyboardMarkup(keyboard=buttons_start, resize_keyboard=True)
keyboard_set_quest = types.ReplyKeyboardMarkup(keyboard=buttons_set_quest, resize_keyboard=True)
keyboard_bilets = types.ReplyKeyboardMarkup(keyboard=buttons_bilets, resize_keyboard=True)
keyboard_quiz = types.ReplyKeyboardMarkup(keyboard=buttons_quiz, resize_keyboard=True)
keyboard_theory = types.InlineKeyboardMarkup(inline_keyboard=buttons_theory, resize_keyboard=True)
keyboard_theme = types.InlineKeyboardMarkup(inline_keyboard=buttons_theme, resize_keyboard=True)
keyboard_statistic = types.ReplyKeyboardMarkup(keyboard=buttons_statistic, resize_keyboard=True)
keyboard_ref = types.ReplyKeyboardMarkup(keyboard=buttons_ref, resize_keyboard=True)
keyboard_ab = types.InlineKeyboardMarkup(inline_keyboard=buttons_bilet_ab, resize_keyboard=True)
keyboard_yes_or_no = types.InlineKeyboardMarkup(inline_keyboard=buttons_yn, resize_keyboard=True)
keyboard_next_prev = types.InlineKeyboardMarkup(inline_keyboard=buttons_np, resize_keyboard=True)
