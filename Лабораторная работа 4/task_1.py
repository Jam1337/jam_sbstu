# TODO решите задачу
def task() -> float:
    # Инициализация переменной для хранения суммы произведений
    total_product = 0

    # Перебор каждого словаря в списке
    for dictionary in data:
        # Извлечение значений "score" и "weight"
        score = dictionary.get("score")
        weight = dictionary.get("weight")

        # Проверка наличия обоих значений
        if score and weight:
            # Вычисление произведения и добавление его к общей сумме
            product = score * weight
            total_product += product

    # Округление результата до 3 знаков после запятой и возврат
    return round(total_product, 3)

    # Пример использования функции с предоставленным JSON


data = [
    {
        "score": 0.0009456152645028281,
        "weight": 1
    }
]

# Вычисление и вывод суммы произведений
result = task()
print(task())
