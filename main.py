import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Инициализируем переводчик
translator = Translator()


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса


        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и его определение на русский
        translated_word = translator.translate(english_word, src='en', dest='ru').text
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

        # Возвращаем переведенные результаты
        return {
            "word": translated_word,
            "definition": translated_definition
        }
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Используем результат функции-словаря
        word_dict = get_english_words()
        if not word_dict:
            print("Не удалось получить данные, попробуйте снова.")
            continue

        word = word_dict.get("word")
        word_definition = word_dict.get("definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user.lower() == word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()