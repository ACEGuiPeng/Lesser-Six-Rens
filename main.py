"""
    小六壬随机取数验吉凶
    1. 询问卦神何事？
    2. 开始取三个卦数
    3. 输出卦数结果
"""
import random
import time
from datetime import datetime

import pandas as pd
import streamlit as st

from service.history import create_table, insert_history, load_histories

gua_list = ["Very Smooth(大安)", "Loss(流连)", "Quickly Good Result(速喜)", "Easy Quarrel(赤口)", "Small Luck(小吉)",
            "Lost Everything(空亡)"]


def get_random():
    time_str = str(time.time())
    random_str = time_str.split(".")[-1][:3]
    return int(random_str) % 6


def random_sleep():
    time.sleep(random.uniform(0.5, 1))


def get_final_index(first_gua, second_gua, third_gua):
    second_start = first_gua - 1
    third_start = second_start + second_gua - 1
    final_index = (third_start + third_gua) % 6 - 1
    return gua_list[final_index]


if __name__ == '__main__':
    # init
    think_time = 10
    create_table()

    # load history
    history = load_histories()

    st.write("## Welcome to use Chinese Lesser Six Rens")
    st.write("Hello, please enter what you would like to ask the Divina tors:")
    thing = st.text_input("question")

    if st.button("Start predicting"):
        st.write(
            f"Dear, the thing you want to consult the Divina tors is:： {thing}, please silently read the divinatory things in your heart, {think_time} seconds later for you to interpret the divina things.")
        time.sleep(think_time)
        first_gua = get_random()
        random_sleep()
        second_gua = get_random()
        random_sleep()
        third_gua = get_random()
        random_sleep()
        st.write(f"Dear, "
                 f""
                 f"three hexagrams have been obtained: {first_gua},{second_gua},{third_gua}, we are deciphering the hexagrams for you.")
        final_result = get_final_index(first_gua, second_gua, third_gua)
        st.write(
            f"Dear, what you are consulting:：{thing}, the final result of the small six Sirens given by the Divinatory God is: {final_result}")

        # insert to session
        item = (thing, final_result, datetime.now())
        history.append(item)
        insert_history(item)

    # show history
    st.write("## Predict History")
    df = pd.DataFrame(history)
    if history:
        df.columns = ["question", "result", "date"]
    st.dataframe(df)
