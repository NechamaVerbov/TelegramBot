import random
import dict_questions
from pymongo.mongo_client import MongoClient

client = MongoClient()
db = client.get_database("Teachild")
parent_collection = db.get_collection('Parent')
child_collection = db.get_collection('Child')

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


def add_parent_to_db(context, update, chat_id):
    p = {
        'parent_id': chat_id,
        'name': update.message.from_user['first_name'],
        'children ids': [],  # a list of children id's
        'children names': []
    }

    response = parent_collection.replace_one({'parent_id': chat_id}, p, upsert=True)


def add_child_to_db(context, name, p_id, chat_id):
    c = {
        'child_id': chat_id,
        'name': name,
        'parent_id': p_id,
        'tasks': {},  # a list of dictionaries
    }
    response = child_collection.replace_one({'child_id': chat_id}, c, upsert=True)


def child_name_to_parent(chat_id, child_name):
    parent_collection.update({'parent_id': chat_id}, {'$push': {'children_names': child_name}})