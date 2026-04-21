from telegram import(KeyboardButton, ReplyKeyboardMarkup)


def get_reply_keyboard():
    """
    Sukuria fiksuotą klaviatūrą apačioje (START/PING)
    """
    keyboard = [
        [KeyboardButton("START"), KeyboardButton("HELP")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
