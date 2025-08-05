import time
from datetime import datetime, timedelta
from telegram import Bot

# Вставьте сюда ваш токен бота
TELEGRAM_TOKEN = 'ВАШ_ТОКЕН_ТЕЛЕГРАММ_БОТА'
# Вставьте сюда ваш chat_id
CHAT_ID = 'ВАШ_CHAT_ID'

bot = Bot(token=TELEGRAM_TOKEN)

def send_reminder():
    message = "Не забудьте сделать гимнастику для глаз! 👁️"
    bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    start_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    end_time = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

    # Если сейчас позже 8 утра, начинаем с текущего времени
    now = datetime.now()
    if now > start_time:
        next_time = now
    else:
        next_time = start_time

    # Цикл до 18:00
    while next_time <= end_time:
        # Время до следующего напоминания
        sleep_duration = (next_time - datetime.now()).total_seconds()
        if sleep_duration > 0:
            time.sleep(sleep_duration)
        try:
            send_reminder()
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
        # Следующее напоминание через 45 минут
        next_time += timedelta(minutes=45)

if __name__ == "__main__":
    main()