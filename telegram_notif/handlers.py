from telegram import Update
from telegram.ext import ContextTypes
from telegram_notif.keyboards import get_reply_keyboard
from supabase_db.connect_database import (get_cheapest_tires,
                                          get_supabase_client,
                                          get_expensive_tires)



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    START komanda - rodo mygtukus, prisegtus apacioje
    MessageHandler paspaudus fiksuota migtuka START atsako:
    "Sveiki! Aš esu Jūsų bot'as.
    Pasirinkite veiksmą žemiau:"
    """
    reply_markup = get_reply_keyboard()

    await update.message.reply_text(
        "Sveiki! Aš esu Jūsų bot'as.\n\n"
        "Aš rodau www.padangos123.lt puslapyje pagal specifikacijas 245/45 R18\n"
        "top 10 brangiausiu ir pigiausiu padangu pagal kainą.\n"
        "Pasirinkite veiksmą žemiau:",
        reply_markup=reply_markup
    )


def format_tires_message(tires: list, title: str) -> str:
    """
    Format tires list into a readable message.
    Args:
        tires (list): List of tire dictionaries.
        title (str): Title for the message.
    Returns:
        str: Formatted message string.
    """
    message = f"🏆 {title}:\n\n"
    for i, tire in enumerate(tires, start=1):
        tech = tire["technical_info"]
        dimension = f"{tech['width']}/{tech['height']} R{tech['diameter']}"
        message += (
            f"{i}. {tire['brand']} {tire['model']}\n"
            f"   📐 {dimension}\n"
            f"   💰 {tire['price']}€\n"
            f"   🔗 {tire['url']}\n\n"
        )
    return message


async def top_cheapest_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    TOP CHEAPEST komanda - rodo 10 pigiausias padangas.
    """
    client = get_supabase_client()
    tires = get_cheapest_tires(client, limit=10)
    message = format_tires_message(tires, "Top pigiausios padangos")
    await update.message.reply_text(message)


async def top_expensive_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    TOP EXPENSIVE komanda - rodo 10 brangiausias padangas.
    """
    client = get_supabase_client()
    tires = get_expensive_tires(client, limit=10)
    message = format_tires_message(tires, "Top brangiausios padangos")
    await update.message.reply_text(message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    HELP komanda - rodo visas komandas ir trumpus aprašymus
    """
    message = (
        "Komandos:\n\n"
        "/start - Pradžia, rodo pagrindinius mygtukus\n"
        "/top_cheap - Rodo pigiausias padangas\n"
        "/top_expensive - Rodo brangiausias padangas\n"
        "/help - Rodo visas komandas ir trumpus aprašymus\n"
    )
    await update.message.reply_text(message)
