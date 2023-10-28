# TODO Напишите функцию find_common_participants
def find_common_participants(participants_1, participants_2, separator=','):
        participants_1_ = participants_1.split(separator)
        participants_2_ = participants_2.split(separator)
        common_participants = list(set(participants_1_).intersection(participants_2_))
        common_participants.sort()
        return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group,participants_second_group, '|')
print(participants)

