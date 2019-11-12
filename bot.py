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


def get_info_from(key: str):
    name, parent_id = key.split('-')
    return name, parent_id


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    key = context.args
    print(key)
    if key:
        logger.info(f"> Start child chat #{chat_id}")
        name, parent_id = get_info_from(key)
        context.user_data['name'] = name
        context.user_data['parent_id'] = parent_id
        context.user_data['tasks'] = []
        home_child()
    else:
        logger.info(f"> Start parent chat #{chat_id}")
        child_name = add_child(context, chat_id)
        context.bot.send_message(chat_id=chat_id, text=f"Send your child this link to join this bot: "
                                                       f"\n https://t.me/teachild_bot?start={child_name}-{str(chat_id)}")
        home_parent(update, context)


def home_parent(update: Update, chat_id, context: CallbackContext):
    bot_keyboards.main_parent_keyboard(update, chat_id, context)


def home_child(update: Update, context: CallbackContext):
    pass


def add_child(context, chat_id):
    context.bot.send_message(chat_id=chat_id, text=f"Enter child's name:")
    return "michal"


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
