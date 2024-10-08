import requests
import os
from dotenv import load_dotenv

def translate_ai(text):
    """
    Переводит текст с английского на русский с использованием OpenL Translate API.

    Параметры:
    text (str): Текст, который нужно перевести.

    Возвращает:
    dict: Результат перевода в формате JSON или сообщение об ошибке.
    """
    # Устанавливаем URL для API перевода HTML
    url = "https://ai-translate.p.rapidapi.com/translateHtml"

    # Подготавливаем данные для запроса
    payload = {
        "texts": [text],
        "tl": "ru",  # Целевой язык - русский
        "sl": "en"   # Исходный язык - английский
    }

    # Устанавливаем заголовки для запроса
    headers = {
        "x-rapidapi-key": os.getenv("API_KEY"),
        "x-rapidapi-host": "ai-translate.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    # Отправляем POST-запрос на перевод текста
    response = requests.post(url, json=payload, headers=headers)

    # Проверяем, что ответ успешный
    if response.status_code == 200:
        result = response.json()
        # Проверяем наличие данных в ответе
        if 'data' in result and result['data']:
            # Извлекаем перевод
            return result['data'][0][0]  # Получаем текст перевода
        else:
            return "Ошибка перевода: нет данных"
    else:
        # Возвращаем сообщение об ошибке API с кодом состояния
        return f"Ошибка API: {response.status_code}"
