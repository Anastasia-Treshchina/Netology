queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
count = 0
count_2 = 0
count_3 = 0

for query in queries:
    query = query.split(' ')
    #print(len(query))
    if query:
        count += 1
        #print(count)
    if len(query) == 2:
        count_2 += 1
        #print(count_2)
    elif len(query) == 3:
        count_3 += 1
        #print(count_3)

query_2 = round(count_2 * 100 / count)
print(f'Поисковых запросов из 2х слов - {query_2}')

query_3 = round(count_3 * 100 / count)
print(f'Поисковых запросов из 3х слов - {query_3}')