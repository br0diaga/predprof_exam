from csv import reader, writer

# Выполнение 1-й части задания
with open('songs.csv', encoding='utf-8') as data_file:
    # Открыть файл с данными как объект reader
    csv_data = reader(data_file, delimiter=',')
    # Линейным поиском получить ответ
    for row in csv_data:
        if row[4][3] > '2002' :
            print(f'{row[3]} - {row[2]} - {row[1]}')

# Вторая часть задания
with open('students.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    artist_data = list(reader(data_file, delimiter=','))
    # Строка с подписями столбцов
    header_line = artist_data.pop(0)
    # Словарь класс:[кол-во учащихся, сумма оценок]
    school_classes = dict()
    for artist in artist_data:
        class_name = artist[3]
        grade = artist[4]
        if class_name not in school_classes.keys():
            school_classes[class_name] = [0, 0]
        if grade != 'None':
            school_classes[class_name][0] += 1
            school_classes[class_name][1] += int(grade)
    # Замена оценок None на среднюю по классу
    for artist in artist_data:
        if artist[4] == 'None':
            average_grade = school_classes[artist[3]][1] / school_classes[artist[3]][0]
            # В OO Calc разделитель дробной части - запятая
            artist[4] = str(round(average_grade, 3)).replace('.', ',')

with open('students_new.csv', 'w', encoding='utf-8') as data_file:
    # Запись в объект writer
    data_writer = writer(data_file, delimiter=',')
    # Строка с подписями столбцов
    data_writer.writerow(header_line)
    # Список строк с исправленными оценками
    data_writer.writerows(pupil_data)

