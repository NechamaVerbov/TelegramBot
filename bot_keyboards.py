from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton)


def main_parent_keyboard(update, chat_id, context):
    menu_main = [[KeyboardButton('Add child')],
                 [KeyboardButton('Assign task')],
                 [KeyboardButton('Get report')],
                 [KeyboardButton('/help')]]
    reply_markup = ReplyKeyboardMarkup(menu_main)
    update.message.reply_text(f"Main menu:",
                               reply_markup=reply_markup)


def main_child_keyboard(update, chat_id, context):
    menu_main = [[KeyboardButton('Start Task')],
                 [KeyboardButton('Show Tasks')],
                  [KeyboardButton('/help')]]
    reply_markup = ReplyKeyboardMarkup(menu_main)
    update.message.reply_text(f"Welcome! {update.message.from_user['first_name']}",
                               reply_markup=reply_markup)


def choose_child_keyboard(update, chat_id, context):
    menu_main = [[InlineKeyboardButton('Next')],
                 [InlineKeyboardButton('Done task')],
                  [InlineKeyboardButton('/help')]]
    reply_markup = ReplyKeyboardMarkup(menu_main)
    update.message.reply_text(f".....bla bla bla ",
                               reply_markup=reply_markup)
