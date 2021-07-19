
from source.models.Person import Persons as Persons

persons_list = []

for _ in range(10):
    p = Persons()
    persons_list.append(p)

for person in persons_list:
    print(person)
