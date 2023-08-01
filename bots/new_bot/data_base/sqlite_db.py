import sqlite3 as sq
from create import bot

def sq_start():
    global base, cur 
    base = sq.connect('data_base\pizza.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT, description TEXT, price TEXT)')
    base.commit()

async def load_info(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()

async def read_info(message):
    for el in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, el[0], f'{el[1]}\nОписание: {el[2]}\nЦена: {el[3]}')
