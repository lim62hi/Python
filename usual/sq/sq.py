import sqlite3 as sq

base = sq.connect('usual\sq\\new.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, password text)'.format('data'))
base.commit()

base.execute('DROP TABLE IF EXISTS data')
base.commit()
base.close()