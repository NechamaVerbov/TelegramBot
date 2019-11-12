import random
import feedparser
import dict_questions
from pymongo.mongo_client import MongoClient
from datetime import datetime

client = MongoClient()
db = client.get_database("Teachild")
db.drop_collection('Parent')
db.drop_collection('Child')
db.drop_collection('Task')
parent_collection = db.get_collection('Parent')
child_collection = db.get_collection('Child')
task_collection = db.get_collection('Task')

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


def add_parent_to_db(update, chat_id):
    p = {
        'parent_id': chat_id,
        'name': update.message.from_user['first_name'],
        'children_ids': [],  # a list of children id's
        'children_names': []
    }

    response = parent_collection.replace_one({'parent_id': chat_id}, p, upsert=True)


def add_child_to_db(name, p_id, chat_id):
    c = {
        'child_id': chat_id,
        'name': name,
        'parent_id': p_id,
        'tasks': [],  # a list of dictionaries
        'current_task': 0
    }
    response = child_collection.replace_one({'child_id': chat_id}, c, upsert=True)


def add_task_to_db(c_id, p_id, level, dictionary):
    t = {
        'child_id': c_id,
        'parent_id': p_id,
        'level': level,
        'status': False,
        'date': datetime.now(),
        'task_dict': dictionary,
        'data_time_start': datetime.datetime(),
        'data_time_finishing': datetime.datetime(),
        'current_task': 0
    }
    response = task_collection.insert_one(t)


def get_date_task_send(task_id):
    task = db.collection.find({'_id': task_id})
    d = feedparser.parse(task['date'])
    return d.strftime("%d/%m/%Y %H:%M:%S")


def child_name_to_parent(chat_id, child_name):
    parent_collection.update({'parent_id': chat_id}, {'$push': {'children_names': child_name}})


def child_id_to_parent(parent_id, child_id):
    parent_collection.update({'parent_id': int(parent_id)}, {'$push': {'children_ids': child_id}})


def get_list_child_id(chat_id_parent):
    return parent_collection.find({'parent_id': chat_id_parent})[0]['children_ids']


def get_list_child_name(chat_id_parent):
    return parent_collection.find({'parent_id': chat_id_parent})[0]['children_names']


def is_parent(chat_id):
    return True if parent_collection.find({'parent_id': chat_id}).count() > 0 else False


def get_current_task(child_id):
    return child_collection.find({'child_id': child_id})[0]['current_task']


def create_task_in_db(parent_id, child_id, level):
    dictionary = send_task(level)
    add_task_to_db(child_id, parent_id, level, dictionary)
    print(child_id, level)


def get_report(parent_id, child_id):
    pass


def get_num_of_level():
    # כמה רמות יש לי
    return int(2)
