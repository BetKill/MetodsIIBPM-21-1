from flask import Flask, render_template, request
from api.openl_translate import translate_openl
from api.ai_translate import translate_ai

# Инициализируем Flask-приложение
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Главная функция приложения, обрабатывающая запросы.

    Возвращает:
    str: HTML-шаблон с переводами текста.
    """
    # Переменные для хранения переводов
    translation_openl = ""
    translation_ai = ""

    # Проверяем, был ли выполнен POST-запрос
    if request.method == 'POST':
        # Получаем текст для перевода из формы
        text_to_translate = request.form['text']

        # Получаем перевод от OpenL Translate API
        translation_openl = translate_openl(text_to_translate).get('translatedText', 'Ошибка перевода')

        # Получаем перевод от AI Translate
        translation_ai = translate_ai(text_to_translate)

    # Рендерим HTML-шаблон с полученными переводами
    return render_template('index.html', translation_openl=translation_openl, translation_ai=translation_ai)

# Запускаем приложение в режиме отладки
if __name__ == '__main__':
    app.run(debug=True)
