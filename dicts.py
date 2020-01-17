#DICTIONARY

vampireDiaries = {
    "Brother1": "Damon Salvatore",
    "Brother2": "Stefan Salvatore",
    "The Girl": "Elena",
    "The Doppelganger": "Katerina"
}

print(len(vampireDiaries))

vampireDiaries['The Guardian'] = 'Alaric'
print(vampireDiaries)
print('\n')

for actor,names in vampireDiaries.items():
    print(names)

for actor in vampireDiaries:
    print(actor)

for names in vampireDiaries.values():
    print(names)

for actor in vampireDiaries.keys():
    print(actor)

#vampireDiaries.popitem()
print(vampireDiaries)

print(vampireDiaries.get('The Girl'))

vampireDiaries.update({'The Witch' : 'Bonnie'})

print(vampireDiaries.keys())

for actors in vampireDiaries.keys():
    print(actors.split(' '))

vD2 = vampireDiaries.copy()
print(vD2)