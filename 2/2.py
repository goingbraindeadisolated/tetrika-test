from mwclient import Site
import animation
import string

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' + string.ascii_uppercase 
animals = dict.fromkeys(alphabet, 0) 

@animation.simple_wait
def parse():
        site = Site('ru.wikipedia.org')
        category = site.categories['Животные_по_алфавиту']
        with open('animals.txt', 'w') as f:
                for page in category:
                        name = page.name
                        if name != 'Категория:Знаменитые животные по алфавиту' and name != 'Категория:Породы собак по алфавиту':
                                animals[name[0]] += 1
                                f.write(name)
                                f.write('\n')
        for i in animals:
                print(i, animals[i], sep=':')
if __name__ == '__main__':
        try:
                parse()
        except Exception as e:
                print(f'Exception was caught: {e.__class__.__name__}')
