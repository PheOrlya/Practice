# Загрузка данных из файла
def load_data(file_name):
    subjects = {}
    with open(file_name, 'r') as file:
        for line in file:
            subject, count = line.strip().split(',')
            subjects[subject] = int(count)
    return subjects

# Вывод таблицы с предметами и количеством студентов
def print_table(subjects):
    print("Предмет\t\tКоличество студентов")
    print("----------------------------------")
    for subject, count in subjects.items():
        print(f"{subject}\t\t{count}")

# Загрузка данных из файла и вывод таблицы
file_name = input("Введите имя файла: ")
data = load_data(file_name)
print_table(data)
