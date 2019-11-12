# YOUR BOT LOGIC/STORAGE/BACKEND FUNCTIONS HERE
import os
import random

import dict_questions

'''
#0-39
dict_questions.dict_questions_math_level1
#0-29
dict_questions.dict_questions_math_level2
'''
NUMBER_Q_IN_TASK = 10


def make_task_for_level(dictt: dict) -> dict:
    return dict(zip(range(NUMBER_Q_IN_TASK), random.choices(dictt, k=NUMBER_Q_IN_TASK)))


def send_task(level) -> dict:
    if int(level) == 1:
        return make_task_for_level(dict_questions.dict_questions_math_level1)
    if int(level) == 2:
        return make_task_for_level(dict_questions.dict_questions_math_level2)


def check_answer(name_img_q: str, answer) -> bool:
    return int(name_img_q.split('=')[1].split('.')[0]) == int(answer)
