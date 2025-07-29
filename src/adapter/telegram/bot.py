import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from src.adapter.telegram.handlers.start import start_command
from src.adapter.telegram.handlers.echo import echo_message
from src.adapter.config.config import load_config
from src.adapter.logging.logging import setup_logging

def start_bot():
    setup_logging()
    config = load_config()

    application = ApplicationBuilder().token(config.telegram.token).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))

    logging.info("Бот запущен")
    application.run_polling()