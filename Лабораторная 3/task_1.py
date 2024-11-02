# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    # Разбиваем строки на списки участников
    first_group = set(participants_first_group.split(delimiter))
    second_group = set(participants_second_group.split(delimiter))

    # Находим общие участники
    common_participants = first_group.intersection(second_group)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
# Вызываем функцию
common = find_common_participants(participants_first_group, participants_second_group, '|')
print(common)