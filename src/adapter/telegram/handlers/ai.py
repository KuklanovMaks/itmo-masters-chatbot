from telegram import Update
from telegram.ext import ContextTypes
from pathlib import Path
from parser_utils.pdf_reader import read_curriculum_pdf
from src.adapter.config.config import load_config

async def ai_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    config = load_config()
    pdf_path = Path(config.files.ai)
    df = read_curriculum_pdf(pdf_path)

    if df.empty:
        await update.message.reply_text("Не удалось извлечь данные из учебного плана AI.")
        return

    sem_counts = df.groupby("semester")["discipline"].count()
    message = "Учебный план программы 'Искусственный интеллект':\n"
    for sem, count in sem_counts.items():
        message += f"Семестр {sem}: {count} дисциплин\n"
    await update.message.reply_text(message)