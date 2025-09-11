# Змінні всіх основних типів
age = 15                      # створюємо змінну "вік"
height = 1.70                 # створюємо змінну "зріст"
name = "Yevhen"               # створюємо змінну "ім’я"
is_student = True             # створюємо змінну "чи студент"
hobbies = ["dota 2", "rust", "cs sourse"]   # створюємо список хобі
grades = (12, 11, 10)         # створюємо кортеж оцінок
person = {"name": "Yevhen", "age": 15}  # створюємо словник з даними
unique_numbers = {1, 2, 3}    # створюємо множину унікальних чисел
none_value = None             # створюємо змінну без значення (None)


# Виводимо всі змінні
print("age", age)             # виводимо вік
print("height", height)       # виводимо зріст
print("name", name)           # виводимо ім’я
print("is_student", is_student)  # виводимо чи студент
print("hobbies", hobbies)     # виводимо хобі
print("grades", grades)       # виводимо оцінки
print("person", person)       # виводимо словник
print("unique_numbers", unique_numbers)   # виводимо множину
print("none_value", none_value)           # виводимо пусте значення


# Арифметичні оператори
x, y = 10, 3                  # створюємо змінні x=10, y=3
print(f"x + y = {x + y}")     # додаємо числа
print(f"x - y = {x - y}")     # віднімаємо числа
print(f"x * y = {x * y}")     # множимо числа
print(f"x / y = {x / y}")     # ділимо (звичайне ділення)
print(f"x // y = {x // y}")   # ділення без дробу (цілочисельне)
print(f"x % y = {x % y}")     # залишок від ділення
print(f"x ** y = {x ** y}")       # підносимо до степеня


# Логічні оператори
a, b = True, False            # створюємо змінні a=True, b=False
print(f"a and b : {a and b}") # перевіряємо чи обидва True
print(f"a or b : {a or b}")   # перевіряємо чи хоча б один True
print(f"not a : {not a}")     # заперечуємо значення a