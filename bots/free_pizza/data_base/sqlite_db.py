import sqlite3 as sq
from create import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

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

async def read_info(id):
    if id == 5221868883:
        for el in cur.execute('SELECT * FROM menu').fetchall():
            await bot.send_photo(id, el[0], f'{el[1]}\nОписание: {el[2]}\nЦена: {el[3]}', reply_markup=\
                                 InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {el[1]}', callback_data=\
                                 f'удалить {el[1]}')))
    else:
        for el in cur.execute('SELECT * FROM menu').fetchall():
            await bot.send_photo(id, el[0], f'{el[1]}\nОписание: {el[2]}\nЦена: {el[3]}')

async def del_info(name):
    cur.execute('DELETE FROM menu WHERE name == ?', (name,))
    base.commit()