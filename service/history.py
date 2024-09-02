# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File  : history.py
@Author: White Gui
@Date  : 2024/9/2
@Desc :
"""
import sqlite3
import streamlit as st

DB_PATH = "./data/history.db"


def create_table():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS history(id INTEGER PRIMARY KEY,question, result, date,actual,mark)")


def load_histories():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM history")
    result = res.fetchall()
    return result


def insert_history(data: tuple):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("INSERT INTO history(question,result,date,actual,mark) VALUES(?, ?, ?, ? , ?)", data)
    con.commit()


def update_history():
    for idx, change in st.session_state.changes["edited_rows"].items():
        print(idx, ": ", change)
        for label, value in change.items():
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute(f"UPDATE history set {label}={value} WHERE id={idx}")
            con.commit()


def delete_all():
    con = sqlite3.connect(DB_PATH)
    con.execute("DELETE FROM history")
    con.commit()
