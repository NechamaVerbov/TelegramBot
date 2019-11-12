from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardButton)


def main_parent_keyboard(update, chat_id, context):
    menu_main = [[InlineKeyboardButton('/add_child')],
                 [InlineKeyboardButton('/assign_task')],
                  [InlineKeyboardButton('/get_report')],
                   [InlineKeyboardButton('/help')]]
    reply_markup = ReplyKeyboardMarkup(menu_main)
    update.message.reply_text(f"Welcome! {update.message.from_user['username']}",
                               reply_markup=reply_markup)


def main_child_keyboard(update, chat_id, context):
    menu_main = [[InlineKeyboardButton('/start_task')],
                 [InlineKeyboardButton('/show_tasks')],
                  [InlineKeyboardButton('/help')]]
    reply_markup = ReplyKeyboardMarkup(menu_main)
    update.message.reply_text(f"Welcome! {update.message.from_user['username']}",
                               reply_markup=reply_markup)


def choose_child_keyboard(update, chat_id, context):
    menu_main = [[InlineKeyboardButton('/next')],
                 [InlineKeyboardButton('/done_task')],
                  [InlineKeyboardButton('/help')]]
    reply_markup = ReplyKeyboardMarkup(menu_main)
    update.message.reply_text(f".....bla bla bla ",
                               reply_markup=reply_markup)
