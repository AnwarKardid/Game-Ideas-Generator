import random

# Example:
#  A [Sci-fi] game in [space], where you play with a [banana] against [time].

def get_data():
    with open('data_support/genres.txt', 'r', encoding='utf-8') as fl:
        genres = (fl.read()).split(',')
    with open('data_support/players.txt', 'r', encoding='utf-8') as fl:
        players = (fl.read()).split(',')
    with open('data_support/places.txt', 'r', encoding='utf-8') as fl:
        places = (fl.read()).split(',')
    with open('data_support/enemies.txt', 'r', encoding='utf-8') as fl:
        enemies = (fl.read()).split(',')        

    return genres, places, players, enemies

genres, places, players, enemies = get_data()
vowels = { 'a', 'e', 'i', 'o', 'u'}

genre = random.choice(genres).strip()
place = random.choice(places).strip()
player = random.choice(players).strip()
enemy = random.choice(enemies).strip()

print(f'A {genre} game in {place}, where you play as a' + ('n ' if player[0] in vowels else ' ') + f'{player} against ' + ('an ' if enemy[0] in vowels else 'a ') + enemy + '.')
