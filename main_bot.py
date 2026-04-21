import os
from dotenv import load_dotenv
from telegram import Update
from telegram_notif.handlers import (start_command,top_cheapest_command,
                                    top_expensive_command, help_command)
from telegram.ext import (Application, CommandHandler, MessageHandler, filters)


load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def main():
    print("🚀 Paleidžiamas botas...")
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # START button handler
    app.add_handler(MessageHandler(filters.Text("START"), start_command))
    # Command handler /start
    app.add_handler(CommandHandler("start", start_command))

    # HELP mygtukas
    app.add_handler(MessageHandler(filters.Text("HELP"), help_command))
    # Command handler /help
    app.add_handler(CommandHandler("help", help_command))

    # Command handler /top_cheap
    app.add_handler(CommandHandler("top_cheap", top_cheapest_command))
    app.add_handler(CommandHandler("top_expensive", top_expensive_command))

    # Run bot
    print("✅ Botas paleistas!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
