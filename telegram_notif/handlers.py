from telegram import Update
from telegram.ext import ContextTypes
from keyboards import get_reply_keyboard


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    START komanda - rodo mygtukus, prisegtus apacioje
    MessageHandler paspaudus fiksuota migtuka START atsako:
    "Sveiki! Aš esu Jūsų bot'as.
    Pasirinkite veiksmą žemiau:"
    """
    reply_markup = get_reply_keyboard()

    await update.message.reply_text(
        "🎮 Sveiki! Aš esu Jūsų bot'as.\n\n"
        "Pasirinkite veiksmą žemiau:",
        reply_markup=reply_markup
    )


async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    PING komanda - paspaudus fiksuotamigtuka apacioje atsako: "OK, ping komanda aktyvi"
    """
    await update.message.reply_text("OK, ping komanda aktyvi ✅")
