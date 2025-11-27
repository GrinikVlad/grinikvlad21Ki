def main():
    # Створюємо порожній словник для збереження студентів і їхніх оцінок
    students = {}

    # Безкінечний цикл для введення даних
    while True:
        # Вводимо ім'я студента
        name = input("Введіть ім'я студента (або stop для завершення): ")

        # Якщо користувач ввів stop — виходимо з циклу
        if name == "stop":
            break

        # Вводимо оцінку (поки ще як текст)
        grade_str = input("Введіть оцінку за практичну роботу: ")

        # Перевіряємо, чи оцінка є числом
        if not grade_str.isdigit():
            continue  # якщо ні — пропускаємо і просимо ввести наступного студента

        # Перетворюємо текст у число
        grade = int(grade_str)

        # Зберігаємо ім'я та оцінку в словник
        students[name] = grade

    # Виводимо всіх студентів
    print("Список студентів та їх оцінки:")
    for name, grade in students.items():
        print(name + " - " + str(grade))

    # Якщо студентів не було введено
    if len(students) == 0:
        print("Немає даних для обробки.")
        return  # завершуємо програму

    # Обчислюємо суму всіх балів
    total = sum(students.values())

    # Обчислюємо середній бал
    average = total / len(students)

    # Формуємо списки студентів за категоріями
    excellent = [name for name, grade in students.items() if 10 <= grade <= 12]  # відмінники
    good = [name for name, grade in students.items() if 7 <= grade <= 9]        # хорошисти
    average_students = [name for name, grade in students.items() if 4 <= grade <= 6]  # середні
    failed = [name for name, grade in students.items() if 1 <= grade <= 3]      # незадовільно

    # Виводимо розраховані результати
    print("Середній бал по групі: " + str(average))
    print("Відмінники (" + str(len(excellent)) + "): " + ", ".join(excellent))
    print("Хорошисти (" + str(len(good)) + "): " + ", ".join(good))
    print("Відстаючі (" + str(len(average_students)) + "): " + ", ".join(average_students))
    print("Не здали (" + str(len(failed)) + "): " + ", ".join(failed))

# Запускаємо програму, якщо файл виконується напряму
if (__name__ == "__main__"):
    main()
