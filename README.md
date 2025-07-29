# 🤖 ITMO Masters Chatbot

Телеграм-бот, который помогает абитуриенту выбрать подходящую магистратуру в ИТМО:  
**«Искусственный интеллект»** или **«AI Product»**,  
анализируя содержание учебных планов и отвечая на вопросы по программам.

---

## 🔍 Возможности

📄 Парсинг PDF-учебных планов программ с сайтов:  
[AI](https://abit.itmo.ru/program/master/ai)  
[AI Product](https://abit.itmo.ru/program/master/ai_product)

💬 Telegram-диалог с пользователем  
📊 Статистика дисциплин по семестрам  
🎯 Простые рекомендации по выбору программы  
🧠 Ответы только по релевантным вопросам об обучении

---

## ⚙️ Стек

Python 3.12+  
python-telegram-bot  
pandas, pdfplumber  
Poetry (для управления зависимостями и запуском)

---

## 🚀 Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your-username/itmo-project.git
cd itmo-project
```

### 2. Установить Poetry (если ещё не установлен)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Установить зависимости проекта

```bash
poetry install
```

### 4. Создать конфигурационный файл

Создайте файл `example_config.json` в корне проекта:

```json
{
  "telegram": {
    "token": "ВАШ_ТОКЕН_ОТ_BotFather"
  },
  "files": {
    "ai": "training_plans/ai.pdf",
    "ai_product": "training_plans/ai_product.pdf"
  }
}
```

### 5. Запуск бота

```bash
poetry run python main.py
```

---

## 🗂 Структура проекта

```
itmo-project/
├── main.py                          # Точка входа: запускает Telegram-бота
├── example_config.json              # Конфиг с токеном бота и путями к PDF-файлам
├── training_plans/                  # Сюда кладутся PDF-файлы учебных планов
│   ├── ai.pdf
│   └── ai_product.pdf
├── parser_utils/                    # Парсеры HTML и PDF
│   └── pdf_reader.py                # Извлечение таблиц дисциплин из PDF
└── src/
    └── adapter/
        ├── telegram/                # Telegram-интерфейс
        │   ├── bot.py               # Инициализация приложения и хендлеров
        │   └── handlers/            # Обработка команд: /start, /ai, /ai_product
        ├── config/                  # Загрузка конфига и обработка ошибок
        └── logging/    
```

---

## 📌 Пример команд

```
/start
Привет! Я помогу тебе выбрать магистратуру ИТМО...

/ai
Учебный план программы 'Искусственный интеллект':
Семестр 1: 5 дисциплин
...

/ai_product
Учебный план программы 'AI Product':
Семестр 1: 6 дисциплин
...
```

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. Свободно используйте, улучшайте и расширяйте.
