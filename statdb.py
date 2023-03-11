import sqlite3

import strings


def create_user_table():
    db = sqlite3.connect('database/statistics.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS results
                 (id INTEGER PRIMARY KEY, user_id INTEGER, bilet_id INTEGER, 
                 question_1 INTEGER, question_2 INTEGER, question_3 INTEGER, 
                 question_4 INTEGER, question_5 INTEGER, question_6 INTEGER,
                 question_7 INTEGER, question_8 INTEGER, question_9 INTEGER, 
                 question_10 INTEGER, question_11 INTEGER, question_12 INTEGER, 
                 question_13 INTEGER, question_14 INTEGER, question_15 INTEGER,
                 question_16 INTEGER, question_17 INTEGER, question_18 INTEGER, 
                 question_19 INTEGER, question_20 INTEGER)''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS statheme
            (id INTEGER PRIMARY KEY, user_id INTEGER, theme TEXT, score INTEGER, total_score INTEGER)''')
    db.commit()
    db.close()


def new_user(user_id):
    db = sqlite3.connect('database/statistics.db')
    cursor = db.cursor()

    cursor.execute('SELECT COUNT(*) FROM results WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    if result[0] > 0:
        #  print(f'{user_id} уже существует')
        return

    for i in range(1, 41):
        cursor.execute('''INSERT INTO results 
                     (user_id, bilet_id, question_1, question_2, question_3, 
                     question_4, question_5, question_6, question_7, question_8, 
                     question_9, question_10, question_11, question_12, question_13, 
                     question_14, question_15, question_16, question_17, question_18, 
                     question_19, question_20) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (user_id, i, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    db.commit()
    cursor.executemany('''INSERT INTO statheme
           (user_id, theme, score, total_score) VALUES (?, ?, 0, ?)''',
                       [(user_id, theme, len(results))
                        for theme in strings.theme_list
                        for results in cursor.execute("SELECT * FROM quests WHERE theme = ?", (theme,))])
    db.commit()
    db.close()


def set_cell_stat(user_id, lst_quests):
    database = sqlite3.connect('database/statistics.db')
    cursor = database.cursor()

    if all(elem.theme == lst_quests[1].theme for elem in lst_quests):
        count_ready = sum([1 for ticket in lst_quests if ticket.ready])
        cursor.execute('''UPDATE statheme SET score = ? WHERE user_id = ? AND theme = ?''',
                       (count_ready, user_id, lst_quests[1].theme))
        database.commit()
    else:
        for i, quests in enumerate(lst_quests):
            bilet_id = quests.quest_id // 100
            column_name = 'question_{}'.format(quests.quest_id % 100)
            cursor.execute('''UPDATE results SET {} = ? WHERE user_id = ? AND bilet_id = ?'''.format(column_name),
                           (quests.ready, user_id, bilet_id))
            database.commit()
    database.close()


def get_stat_results(user_id):
    with sqlite3.connect('database/statistics.db') as conn:
        c = conn.cursor()
        query = "SELECT " + ", ".join(
            [f"question_{i}" for i in range(1, 21)]) + " FROM results WHERE user_id = ? AND bilet_id = ?"
        lst_bilet = [c.execute(query, (user_id, i)).fetchone() for i in range(1, 41)]
    return lst_bilet


def get_stat_stattheme(user_id):
    with sqlite3.connect('database/statistics.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT theme, score, total_score FROM statheme WHERE user_id = ?', (user_id,))
        lst = cursor.fetchall()
    return lst
