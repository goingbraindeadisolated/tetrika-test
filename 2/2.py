from mwclient import Site
import animation

@animation.simple_wait
def parse():
        site = Site('ru.wikipedia.org')
        category = site.categories[r'Животные_по_алфавиту']
        with open('animals.txt', 'w') as f:
                for page in category:
                        f.write(page.name)
                        f.write('\n')

if __name__ == '__main__':
    parse()
