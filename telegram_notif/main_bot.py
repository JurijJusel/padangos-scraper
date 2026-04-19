import os
from dotenv import load_dotenv
from telegram import Update
from handlers import ping_command, start_command
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)


load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def main():
    print("🚀 Paleidžiamas botas...")
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # START button handler
    app.add_handler(MessageHandler(filters.Text("START"), start_command))
    # Command handler /start
    app.add_handler(CommandHandler("start", start_command))

    # PING mygtukas
    app.add_handler(MessageHandler(filters.Text("PING"), ping_command))
    #Command handler /ping
    app.add_handler(CommandHandler("ping", ping_command))

    # Run bot
    print("✅ Botas paleistas!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
