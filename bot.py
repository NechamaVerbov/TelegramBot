"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started.
Usage:
...
"""
import logging
import bot_keyboards
import re
import secret_settings
from io import BytesIO
from PIL import Image
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler)
from telegram import Update
from model import add_parent_to_db, add_child_to_db, child_name_to_parent, is_parent, child_id_to_parent
from telegram.ext import (CallbackContext)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot_users = dict()


def get_info_from(key: str):
    name, parent_id = key.split('-')
    return name, parent_id


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    key = context.args
    if key:
        logger.info(f"> Start child chat #{chat_id}")
        name, parent_id = get_info_from(key[0])
        add_child_to_db(name, parent_id, chat_id)
        child_id_to_parent(parent_id, chat_id)
        home_child(update, context, chat_id)
    else:
        logger.info(f"> Start parent chat #{chat_id}")
        add_parent_to_db(update, chat_id)
        context.bot.send_message(chat_id=chat_id, text=f"Welcome! {update.message.from_user['first_name']}")
        add_child(update, context, chat_id)


def home_parent(update: Update, chat_id, context: CallbackContext):
    bot_keyboards.main_parent_keyboard(update, chat_id, context)


def home_child(update: Update, context: CallbackContext, chat_id):
    bot_keyboards.main_child_keyboard(update, chat_id, context)


def add_child(update, context, chat_id):
    context.bot.send_message(chat_id=chat_id, text=f"Enter your child's name:")


def adding_child(update, context, child_name):
    chat_id = update.effective_chat.id
    logger.info(f"> Adding {child_name} to parent #{chat_id}")

    child_name_to_parent(chat_id,child_name)
    context.bot.send_message(chat_id=chat_id, text=f"Send your child this link to join this bot: "
                                                   f"\n https://t.me/teachild_bot?start={child_name}-{str(chat_id)}")
    home_parent(update, chat_id, context)


def assign_task(update: Update, context: CallbackContext):
    bot_keyboards.choose_child_for_task(update, context, update.effective_chat.id)
    # child_id = bot_keyboards.choose_child_for_task(update, chat_id, context)
    # level_task = bot_keyboards.choose_level_task(update)
    # model.set_task_for_child(child_id, level_task)
    # context.bot.send_message(chat_id=child_id, text=f"Hi, you have a new assignment 😃")


def start_task_one(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    level = 0  # task list- rather the first one that's not completed
    context.bot.send_message(chat_id=chat_id, text=f"You are solving Math - level {level}.\n Good luck!!!")
    amount_questions = 7  # length of questions in that level
    # get task
    context.bot.send_photo(chat_id=chat_id, photo=open('screenshots/shopping-list-bot-1.png', 'rb'),
                           caption=f"Question #1/{amount_questions}")
    bot_keyboards.child_in_task_keyboard(update, chat_id, context)


def next_task(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    current_ques = 2  # get current task + 1
    amount_questions = 7  # length of questions in that level
    # get task
    context.bot.send_photo(chat_id=chat_id, photo=open('screenshots/shopping-list-bot-1.png', 'rb'),
                           caption=f"Question #1/{amount_questions}")


def callback_query_handler_choose_child(update, context):
    parent_id = update.effective_chat.id
    # child_id = update.callback_query.data
    context.user_data['choose_child'] = update.callback_query.data
    # bot_keyboards.model.create_task_in_DB(child_id, parent_id)
    bot_keyboards.choose_level_task(update, context)


def callback_query_handler_choose_level(update, context):
    child_level = update.callback_query.data
    bot_keyboards.model.create_task_in_DB(context.user_data['choose_child'], child_level.replace('x', ''))


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    if text == 'Add child':
        add_child(update, context, chat_id)
    elif text == 'Assign task':
        assign_task(update, context)
    elif text == 'Get report':
        pass
    elif text == 'Start Task':
        start_task_one(update, context)
    elif text == 'Show Tasks':
        pass
    elif is_parent(chat_id):
        adding_child(update, context, text)
    else:
        next_task(update, context)



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    # Create the Updater and pass it your bot's token.
    updater = Updater(secret_settings.BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # log all errors
    dispatcher.add_error_handler(error)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)

    echo_handler = MessageHandler(Filters.text, respond)
    dispatcher.add_handler(echo_handler)

    dispatcher.add_handler(CallbackQueryHandler(callback_query_handler_choose_child, pattern=re.compile(r'\d')))

    dispatcher.add_handler(CallbackQueryHandler(callback_query_handler_choose_level, pattern=re.compile(r'x\d+')))

    logger.info("* Start polling...")
    updater.start_polling()  # Starts polling in a background thread.
    updater.idle()  # Wait until Ctrl+C is pressed
    logger.info("* Bye!")


if __name__ == '__main__':
    main()
