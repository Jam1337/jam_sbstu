list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определим общее количество игроков
total_players = len(list_players)

# Индекс середины списка
middle_index = total_players // 2

# Разделим игроков на две равные команды
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# Выведем каждую команду на отдельной строке
print("Первая команда:", first_team)
print("Вторая команда:", second_team)