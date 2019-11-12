from bot import logger, error, start, add_child, get_report, assign_task
import secret_settings
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)


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

    echo_handler = MessageHandler(Filters.text, add_child)
    dispatcher.add_handler(echo_handler)

    parent_handler = CommandHandler('add_child', add_child)
    dispatcher.add_handler(parent_handler)
    parent_handler = CommandHandler('assign_task', assign_task)
    dispatcher.add_handler(parent_handler)
    parent_handler = CommandHandler('get_report', get_report)
    dispatcher.add_handler(parent_handler)

    logger.info("* Start polling...")
    updater.start_polling()  # Starts polling in a background thread.
    updater.idle()  # Wait until Ctrl+C is pressed
    logger.info("* Bye!")


if __name__ == '__main__':
    main()
