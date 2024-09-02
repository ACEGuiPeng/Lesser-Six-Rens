# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File  : history.py
@Author: White Gui
@Date  : 2024/9/2
@Desc :
"""
import sqlite3

DB_PATH = "./data/history.db"

def create_table():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS history(question, result, date)")


def load_histories():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM history")
    result = res.fetchall()
    return result


def insert_history(data: tuple):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("INSERT INTO history VALUES(?, ?, ?)", data)
    con.commit()
