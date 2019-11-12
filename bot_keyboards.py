from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton,
                      InlineKeyboardMarkup)
import func_help
import model


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


def child_in_task_keyboard(update, chat_id, context):
    menu_main = [[InlineKeyboardButton('Next')],
                 [InlineKeyboardButton('Done task')],
                 [InlineKeyboardButton('/help')]]
    reply_markup = ReplyKeyboardMarkup(menu_main)
    update.message.reply_text(f"Enter your answer or press one of the buttons below: ",
                              reply_markup=reply_markup)


def choose_child_for_task(update, context, chat_id):
    button_list = []
    for id, name in zip(model.get_list_child_id(chat_id), model.get_list_child_name(chat_id)):
        button_list.append(InlineKeyboardButton(name, callback_data=id))
    reply_markup = InlineKeyboardMarkup(func_help.build_menu(button_list, n_cols=1))
    update.message.reply_text("Choose child", reply_markup=reply_markup)


def choose_level_task(update, context):
    button_list = []
    for level in range(model.get_num_of_level()):
        button_list.append(InlineKeyboardButton(f'Level {level}', callback_data='x' + str(level)))
    reply_markup = InlineKeyboardMarkup(func_help.build_menu(button_list, n_cols=1))
    context.bot.send_message(chat_id=update.effective_chat.id, text='Choose Level', reply_markup=reply_markup)
