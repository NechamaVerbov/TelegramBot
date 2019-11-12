import secret_settings

print(secret_settings.BOT_TOKEN)

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started.
Usage:
...
"""
from telegram import Update
from telegram.ext import (CallbackContext)
import bot_keyboard


def start(update: Update, context: CallbackContext):
    pass


def home_parent(update: Update, context: CallbackContext):
    pass


def home_child(update: Update, context: CallbackContext, chat_id):
    bot_keyboard.main_child_keyboard(update, chat_id, context)


def add_child(update: Update, context: CallbackContext):
    pass


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
