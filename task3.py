"""
Решение задачи 3 предпрофессионального экзамена.
Программа читает данные из файла.
Далее в бесконечном цикле запрашивает номер проекта и
ищет его линейным поиском.
Выход из цикла - по значению СТОП
"""

from csv import reader

with open('songs.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    artist_data = list(reader(data_file, delimiter=','))
# Ввод первого значения
project_id = input('Введите имя артиста или 0: ')
# Цикл до ввода СТОП
while project_id != '0':
    # Линейный поиск позиции искомого значения
    position = -1
    for i in range(len(artist_data)):
        if artist_data[i][2] == project_id:
            position = i
            break
    # Вывод на экран
    if position >= 0:
        print(f'У {artist_data[2]} найдена песня: {artist_data[3]}')
    else:
        print('К сожалению, ничего не удалось найти')
    # Чтение следующего значения
    project_id = input('Введите имя артиста или 0: ')


#“У <артист> найдена песня: <название песни>”



