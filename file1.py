"""
Задание 3 - работа с файлами

Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt

"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        source_line = ''.join([x for x in f])

    chars_counter = len(source_line)
    word_counter = len(source_line.split(' '))
    replaced_line = source_line.replace('.', '!')

    print(f'Количество символов - {chars_counter}')
    print(f'Количество слов - {word_counter}')

    with open('referat2.txt', 'w', encoding='utf-8') as f2:
        f2.write(replaced_line)


if __name__ == '__main__':
    main()