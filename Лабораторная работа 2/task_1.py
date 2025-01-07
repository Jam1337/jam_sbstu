# Подушка безопасности
money_capital = 20000

# Ежемесячная зарплата
salary = 5000

# Траты за первый месяц
spend = 6000

# Ежемесячный рост цен
increase = 0.05

# Инициализируем счетчик месяцев
months_without_debt = 0

# Основной цикл, который будет считать количество месяцев
while money_capital >= 0:
    # Первый месяц: траты равны расходам
    money_capital += salary
    money_capital -= spend

    # Следующие месяцы: траты увеличиваются на 5%
    for _ in range(1, months_without_debt + 1):
        money_capital += salary
        money_capital -= spend * (1 + increase)

    # Увеличиваем счетчик месяцев
    months_without_debt += 1

# Выведем результат
print("Количество месяцев, которое можно протянуть без долгов:", months_without_debt)