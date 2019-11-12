import logging
import secret_settings
import bot
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackContext)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(secret_settings.BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    start_task_handler = CommandHandler('start_task', bot.start_ques1)
    dispatcher.add_handler(start_task_handler)

    show_task_handler = CommandHandler('show_task', bot.show_child_tasks)
    dispatcher.add_handler(show_task_handler)

    logger.info("* Start polling...")
    updater.start_polling()  # Starts polling in a background thread.
    updater.idle()  # Wait until Ctrl+C is pressed
    logger.info("* Bye!")


if __name__ == '__main__':
    main()
