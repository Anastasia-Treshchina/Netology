queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'сериалы этим летом сериалы этим летом сериалы этим летом',
    'сериалы этим летом сериалы этим летом',
    'сериалы',
]

total_request_quantity = len(queries)  # общее кол-во запросов

dct = {}  # Временный словарь куда пишем статистику своеобразная база данных

for query in queries:
    count = len(query.split())
    #print(count)
    dct[count] = dct.get(count, 0) + 1
    #print(dct)
print(f'всего запросов - {total_request_quantity}')
print(f' результирующий словарь - {dct}')

# Для каждого элемента словаря, т.е. для каждого кол-ва слов расчитываем процент и выводим на печать
for key in dct:
    percent_of_queries = round(dct[key] / total_request_quantity * 100)
    print(f'Кол-во слов в запросе {key}  - {percent_of_queries}')