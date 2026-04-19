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
        "🎮 Sveiki! Aš esu Jūsų bot'as.\n\n"
        "Pasirinkite veiksmą žemiau:",
        reply_markup=reply_markup
    )


async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    PING komanda - paspaudus fiksuotamigtuka apacioje atsako: "OK, ping komanda aktyvi"
    """
    await update.message.reply_text("OK, ping komanda aktyvi ✅")


async def top_cheapest_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    TOP CHEAPEST komanda - rodo 5 pigiausias padangas
    su pavadinimu, dimensijomis, kaina ir url
    """
    client = get_supabase_client()
    tires = get_cheapest_tires(client, limit=5)

    message = "🏆 Top 5 pigiausios padangos:\n\n"

    for i, tire in enumerate(tires, start=1):
        tech = tire["technical_info"]
        dimension = f"{tech['width']}/{tech['height']} R{tech['diameter']}"
        message += (
            f"{i}. {tire['brand']} {tire['model']}\n"
            f"   📐 {dimension}\n"
            f"   💰 {tire['price']}€\n"
            f"   🔗 {tire['url']}\n\n"
        )

    await update.message.reply_text(message)


async def top_expensive_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    TOP EXPENSIVE komanda - rodo 5 brangiausias padangas
    su pavadinimu, dimensijomis, kaina ir url
    """
    client = get_supabase_client()
    tires = get_expensive_tires(client, limit=5)

    message = "🏆 Top 5 brangiausios padangos:\n\n"

    for i, tire in enumerate(tires, start=1):
        tech = tire["technical_info"]
        dimension = f"{tech['width']}/{tech['height']} R{tech['diameter']}"
        message += (
            f"{i}. {tire['brand']} {tire['model']}\n"
            f"   📐 {dimension}\n"
            f"   💰 {tire['price']}€\n"
            f"   🔗 {tire['url']}\n\n"
        )

    await update.message.reply_text(message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    HELP komanda - rodo visas komandas ir trumpus aprašymus
    """
    message = (
        "🆘 Komandos:\n\n"
        "/start - Pradžia, rodo pagrindinius mygtukus\n"
        "/ping - Patikrina ar botas veikia\n"
        "/top_cheap - Rodo 5 pigiausias padangas\n"
        "/top_expensive - Rodo 5 brangiausias padangas\n"
        "/help - Rodo visas komandas ir trumpus aprašymus\n"
    )
    await update.message.reply_text(message)
