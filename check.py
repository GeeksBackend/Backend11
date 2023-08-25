from pymystem3 import Mystem

def generate_forbidden_words():
    m = Mystem()
    forbidden_words = set()

    # Пример списка фраз, которые могут быть матерными
    phrases = [
        "грубая фраза 1",
        "неприличное выражение 2",
        "матерное слово 3",
        # Добавьте дополнительные фразы и слова сюда
    ]

    for phrase in phrases:
        lemmas = m.lemmatize(phrase)
        forbidden_words.update(lemmas)

    return forbidden_words

# Генерируем список запрещенных слов
forbidden_words = generate_forbidden_words()

# Пример вывода списка запрещенных слов
print("Запрещенные слова:")
for word in forbidden_words:
    print(word)