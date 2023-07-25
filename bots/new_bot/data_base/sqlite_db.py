import sqlite3 as sq

def sq_start():
    global base, cur 
    base = sq.connect()