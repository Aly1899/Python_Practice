import pandas as pd
import random
from pokemon import Pokemon

df = pd.read_csv('pokemon first gen (no dups).csv', index_col=0, )

def create_opponent(number_id: int) -> object:
    '''
    This function creates a pokemon instance for the opponent.
    :param number_id: A number between 1 and 150 relating to the gen 1 pokemon pokedex number.
    :return: a Pokemon()
    '''


    opponent = Pokemon(df.loc[number_id])
    return opponent


opponent_id = random.randint(1, 150)
opponent = create_opponent(opponent_id)



print(f'A wild {opponent.name} appeared!')
print(f'Using your pokedex you find its stats. \n'
      f'HP: {opponent.hp} \t'
      f'Attack: {opponent.attack} \n'
      f'Defense: {opponent.defense} \t'
      f'Special Attack: {opponent.special_atk} \n'
      f'Special Defense: {opponent.special_def} \t'
      f'Speed: {opponent.speed} \n'
      f'{opponent.name} is a {opponent.type1.lower()} type pokemon.')

if opponent.legendary:
    print(f"It's the legendary pokemon {opponent.name}!")
    
