from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я помогу тебе выбрать магистратуру ИТМО. Введи /ai или /ai_product")


# src/adapter/telegram/handlers/echo.py
from telegram import Update
from telegram.ext import ContextTypes

async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Вы написали: {update.message.text}")