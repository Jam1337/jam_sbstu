# Ежемесячная зарплата
salary = 5000

# Траты за первый месяц
spend = 6000

# Количество месяцев, которое планируется протянуть без долгов
months = 10

# Ежемесячный рост цен
increase = 0.03

# Рассчитаем необходимую подушку безопасности
safety_net = 0

# Рассчитаем траты за каждый месяц с учетом роста цен
for month in range(1, months + 1):
    if month == 1:
        total_spend = spend
    else:
        total_spend = spend * (1 + increase)
    safety_net += total_spend
    safety_net -= salary

# Округлим подушку безопасности до целого числа
safety_net_rounded = round(safety_net)

# Выведем результат
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {safety_net_rounded}")
