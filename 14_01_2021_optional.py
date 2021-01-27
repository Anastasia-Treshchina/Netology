list_1 = ['2018-01-01', 'yandex', 'cpc', 100]

base_len = len(list_1)

while len(list_1):
    if base_len == len(list_1):
        value = list_1.pop()
        key = list_1.pop()
        dict_data = {key: value}
    else:
        dict_data = {list_1.pop(): dict_data}
print(dict_data)