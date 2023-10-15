list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_players = len(list_players)
middle_index = count_players // 2
command1 = list_players[:middle_index]
command2 = list_players[middle_index:]
print(command1)
print(command2)
