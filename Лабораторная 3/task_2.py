# TODO Напишите функцию для поиска индекса товара
def find_first_occurrence(items_list, item):
    if item in items_list:
        return items_list.index(item)
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
find_items = ['банан', 'груша', 'персик']

for find_item in find_items:
    index_item = find_first_occurrence(items_list, find_item)    # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
