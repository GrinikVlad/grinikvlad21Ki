age = 15                      # створюємо змінну "вік"
height = 1.70                 # створюємо змінну "зріст"
name = "Vlad"               # створюємо змінну "ім’я"
is_student = True             # створюємо змінну "чи студент"
hobbies = ["pubg", "rust", "cs sourse"]   # створюємо список хобі
grades = (12, 11, 10)         # створюємо кортеж оцінок
person = {"name": "Vlad", "age": 15}  # створюємо словник з даними
unique_numbers = {1, 2, 3}    # створюємо множину унікальних чисел
none_value = None             # створюємо змінну без значення (None)

# Виводимо всі змінні з типом
print("age:", age, "type:", type(age))
print("height:", height, "type:", type(height))
print("name:", name, "type:", type(name))
print("is_student:", is_student, "type:", type(is_student))
print("hobbies:", hobbies, "type:", type(hobbies))
print("grades:", grades, "type:", type(grades))
print("person:", person, "type:", type(person))
print("unique_numbers:", unique_numbers, "type:", type(unique_numbers))
print("none_value:", none_value, "type:", type(none_value))

# Арифметичні оператори
x, y = 10, 3
print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"x // y = {x // y}")
print(f"x % y = {x % y}")
print(f"x  y = {x  y}")

# Логічні оператори
a, b = True, False
print(f"a and b : {a and b}")
print(f"a or b : {a or b}")
print(f"not a : {not a}")
