ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

ids_list = []

for users, number_id in ids.items():
    ids_list += number_id

ids_set = set(ids_list)
print(ids_set)

# print(ids_set)
