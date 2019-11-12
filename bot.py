"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started.
Usage:
...
"""
import logging
import bot_keyboards
import requests
import secret_settings
from telegram import Update
from telegram.ext import (CallbackContext)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot_users = dict()


def get_info_from(key: str):
    name, parent_id = key.split('-')
    return name, parent_id


def login_parent(context, chat_id):
    context.user_data['status'] = 'Parent'
    context.user_data['children'] = {}
    bot_users[chat_id] = context.user_data


def login_child(context, name, parent_id, chat_id):
    context.user_data['name'] = name
    context.user_data['status'] = 'child'
    context.user_data['parent_id'] = parent_id
    context.user_data['tasks'] = []
    bot_users[chat_id] = context.user_data
    bot_users[int(parent_id)]['children'][name] = {chat_id, 'connected'}


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    key = context.args
    if key:
        logger.info(f"> Start child chat #{chat_id}")
        name, parent_id = get_info_from(key[0])
        login_child(context, name, parent_id, chat_id)
        home_child(update, context)
    else:
        logger.info(f"> Start parent chat #{chat_id}")
        login_parent(context, chat_id)
        add_child(update, context, chat_id)


def home_parent(update: Update, context: CallbackContext):
    pass


def home_child(update: Update, context: CallbackContext):
    pass


def add_child(update, context, chat_id):
    context.bot.send_message(chat_id=chat_id, text=f"Enter child's name:")


def adding_child(update, context):
    chat_id = update.effective_chat.id
    child_name = update.message.text
    logger.info(f"> Adding {child_name} to parent #{chat_id}")
    bot_users[int(chat_id)]['children'][child_name] = {}
    context.bot.send_message(chat_id=chat_id, text=f"Send your child this link to join this bot: "
                                                   f"\n https://t.me/teachild_bot?start={child_name}-{str(chat_id)}")
    home_parent(update, context)


def assign_task(update: Update, context: CallbackContext):
    pass


def get_report(update: Update, context: CallbackContext):
    pass


def start_ques1(update: Update, context: CallbackContext):
    pass


def get_answer(update: Update, context: CallbackContext):
    pass


def check_answer(update: Update, context: CallbackContext):
    pass


def next_task(update: Update, context: CallbackContext):
    pass


def done_task(update: Update, context: CallbackContext):
    pass


def generate_report(update: Update, context: CallbackContext):
    pass


def show_child_tasks(update, context):
    pass


def help(update: Update, context: CallbackContext):
    pass


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

