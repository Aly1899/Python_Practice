# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:25:58 2018

@author: sanchez
"""

# This is just a test
import pandas as pd
import time
import random
import os

from pokemon_creatures import Player, Opponent

df = pd.read_csv('pokemon first gen (no dups).csv', index_col = 0,)

opponent_number = random.randint(1, 150)
player_number = int(input('Choose your Pokemon\' number: '))

os.system('cls')

opponent = Opponent(df.loc[opponent_number], opponent_number)
player = Player(df.loc[player_number], player_number)

print(f'A wild {opponent.name} appeared!')
time.sleep(.8)
print(f"Using your pokedex you can learn more about it.") 
time.sleep(0.2)
print(f"This {opponent.name}'s stats are: ")
time.sleep(0.2)
print(f"HP: {opponent.hp}") 
time.sleep(0.2)
print(f"Attack: {opponent.attack}")
time.sleep(0.2)
print(f"Defense: {opponent.defense}")
time.sleep(0.2)
print(f"Sp. Attack: {opponent.special_atk}")
time.sleep(0.2)
print(f"Sp. Defense: {opponent.special_def}")
time.sleep(0.2)
print(f"Speed: {opponent.speed}")
time.sleep(0.2)
print(f"and it's of {opponent.type1.lower()} type.\n")
time.sleep(0.2)
if opponent.legendary:
    print(f"It's the legendary {opponent.name}!\n\n")
    

    
while True:
    time.sleep(0.5)
    print(f"It's your turn {player.name}: ")
    time.sleep(0.5)
    #print(f"{player.name} has {player.hp} left.\n")
    #time.sleep(0.5)
    player.attack_opponent(opponent)
    
    if opponent.hp <= 0:
        print(f"{opponent.name} was defeated!\n")
        break
    time.sleep(.8)
    print(f"It's {opponent.name}'s turn.\n")
    time.sleep(.8)
    opponent.attack_player(player)
    if player.hp <= 0:
        print(f"Oh no! {player.name} fainted.")
        os.system('cls')
        break
        
    time.sleep(.8)
    
