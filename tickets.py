import json
import random
import sqlite3

import strings


class Ticket:
    def __init__(self, quest_id, num, text, suc, a1, a2, a3, a4, a5, descript, image, theme, ready):
        self.quest_id = quest_id
        self.num = num
        self.text = text
        self.suc = suc
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.descript = descript
        self.image = image
        self.theme = theme
        self.ready = ready


def get_bilet_by_id(numBilet: int):
    database = sqlite3.connect('database/quests.db')
    cursor = database.cursor()
    my_list = []

    for i in range(1, 21):
        quest_id = int(numBilet) * 100 + i
        cursor.execute("SELECT * FROM quests WHERE quest_id = ?", (quest_id,))
        result = cursor.fetchone()
        ticket = Ticket(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8],
                        result[9],
                        result[10], result[11], result[12], False)
        my_list.append(ticket)
    database.close()
    return my_list


def get_bilet_by_theme(theme: str):
    database = sqlite3.connect('database/quests.db')
    cursor = database.cursor()
    cursor.execute("SELECT * FROM quests WHERE theme = ?", (theme,))
    results = cursor.fetchall()
    my_list = []
    for result in results:
        ticket = Ticket(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8],
                        result[9],
                        result[10], result[11], result[12], False)
        my_list.append(ticket)
    database.close()
    return my_list


def get_bilet_by_exam():
    database = sqlite3.connect('database/quests.db')
    cursor = database.cursor()
    my_list = []
    themes = random.sample(strings.theme_list, 20)
    for i in range(len(themes)):
        cursor.execute("SELECT * FROM quests WHERE theme = ?", (themes[i],))
        results = cursor.fetchall()
        result = results[random.randrange(0, len(results))]
        ticket = Ticket(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8],
                        result[9],
                        result[10], result[11], result[12], False)
        my_list.append(ticket)

    database.close()
    return my_list
