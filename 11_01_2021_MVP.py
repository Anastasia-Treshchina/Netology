boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys = sorted(boys)
girls = sorted(girls)

if len(boys) != len(girls):
    print("Кто-то останется без пары")
else:
   zip(boys, girls)
   print("Идеальные пары:")
   for name_boys, name_girls in zip(boys, girls):
     print(name_boys, 'и', name_girls)


