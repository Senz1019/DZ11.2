"""Функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами"""
def convert_to_uppercase(string):
    return string.upper()

# Пример использования функции
input_string = input()
output_string = convert_to_uppercase(input_string)
print(output_string)

"""Новая функция, которая делает заглавными первые буквы каждого слова в строке, поступившей на вход функции"""

def capitalize_words(input_string):
    words = input_string.split()  # Разделение строки на список слов
    capitalized_words = [word.capitalize() for word in words]  # Преобразование каждого слова в список с заглавной буквы
    output_string = ' '.join(capitalized_words)  # Объединение слов обратно в строку с пробелами
    return output_string

# Пример использования функции
input_str = "hello world! how are you?"
capitalized_str = capitalize_words(input_str)
print(capitalized_str)

