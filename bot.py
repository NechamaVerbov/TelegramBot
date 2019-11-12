"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started.
Usage:
...
"""
import logging
import bot_keyboards
import secret_settings
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler)
from telegram import Update
from model import add_parent_to_db, add_child_to_db
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
        add_child_to_db(context, name, parent_id, chat_id)
        home_child(update, context, chat_id)
    else:
        logger.info(f"> Start parent chat #{chat_id}")
        add_parent_to_db(context, update, chat_id)
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

    #child_name_to_parent(chat_id,child_name)
    context.bot.send_message(chat_id=chat_id, text=f"Send your child this link to join this bot: "
                                                   f"\n https://t.me/teachild_bot?start={child_name}-{str(chat_id)}")
    home_parent(update, chat_id, context)


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    if text == 'Add child':
        add_child(update, context, chat_id)
    elif text == 'Assign task':
        pass
    elif text == 'Get report':
        pass
    elif text == 'Start Task':
        pass
    elif text == 'Show Tasks':
        pass
    else:
        adding_child(update, context, text)


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

    logger.info("* Start polling...")
    updater.start_polling()  # Starts polling in a background thread.
    updater.idle()  # Wait until Ctrl+C is pressed
    logger.info("* Bye!")


if __name__ == '__main__':
    main()
