import requests
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

def translate_openl(text):
    """
    Переводит текст с английского на русский с использованием AI Translate API.

    Параметры:
    text (str): Текст, который нужно перевести.

    Возвращает:
    str: Переведенный текст или сообщение об ошибке.
    """
    # Устанавливаем URL для API перевода
    url = "https://openl-translate.p.rapidapi.com/translate"

    # Подготавливаем данные для запроса
    payload = {
        "target_lang": "ru",  # Целевой язык - русский
        "text": text          # Текст для перевода
    }

    # Устанавливаем заголовки для запроса
    headers = {
        "x-rapidapi-key": os.getenv("API_KEY"),  # Получаем ключ API из переменной окружения
        "x-rapidapi-host": "openl-translate.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    # Отправляем POST-запрос на перевод текста
    response = requests.post(url, json=payload, headers=headers)

    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        # Возвращаем результат перевода в формате JSON
        return response.json()
    else:
        # Если произошла ошибка, возвращаем сообщение об ошибке с кодом состояния
        return {"error": f"Ошибка API: {response.status_code}"}
