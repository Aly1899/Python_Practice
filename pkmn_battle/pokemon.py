import os
import time
import random

class Pokemon:
    def __init__(self, attributes):
        self.number = opponent_number
        self.name = attributes['Name']
        self.type1 = attributes['Type1']
        self.type2 = attributes['Type2']
        self.total = attributes['Total']
        self.hp = attributes['HP']
        self.attack = attributes['Attack']
        self.defense = attributes['Defense']
        self.special_atk = attributes['SpecialAtk']
        self.special_def = attributes['SpecialDef']
        self.speed = attributes['Speed']
        self.generation = attributes['Generation']
        self.legendary = attributes['Legendary']
        
class Player(Pokemon):
    def __init__(self, attributes, opponent_number):
        Pokemon.__init__(self, attributes, opponent_number)
        
        
    def attack_opponent(self, opponent):
        time.sleep(0.3)
        attack_type = str(input('Do you want to [a]ttack or use a [s]pecial attack?\n'))
        os.system('cls')
        print("\n")
        
        if attack_type.lower()[0] == 'a':
            damage = self.attack - opponent.defense
        elif attack_type.lower()[0] == 's':
            damage = self.special_atk - opponent.special_def
        else: 
            print("Uhh you must have misunderstood... try again.")
        
        if damage < 1:
            damage = 1
        elif damage > 10:
            damage = 10
            
        print(f'{self.name} attacked {opponent.name}!')
        time.sleep(0.3)
        print(f'It caused {damage} damage!\n')
        time.sleep(0.3)
        
        opponent.hp -= damage
        
        
        if opponent.hp > 0: 
            time.sleep(0.3)
            print(f'{opponent.name} has {opponent.hp} HP left.\n')
            time.sleep(0.8)
            
        else:
            print(f'{opponent.name} has fainted!')
            
    
class Opponent(Pokemon):
    def __init__(self, attributes, opponent_number):
        Pokemon.__init__(self, attributes, opponent_number)

    
    def attack_player(self, opponent):
        
        engage_type = random.choice(['attack', 'defend'])    
        attack_type = random.choice(['regular', 'special'])

        if engage_type == 'attack':
            if attack_type == 'regular':
                damage = self.attack - opponent.defense
            else:
                damage = self.special_atk - opponent.special_def
                
            if damage < 1:
                damage = 1
            elif damage > 10:
                damage = 10

            print(f'{self.name} attacked {opponent.name}!')
            time.sleep(0.3)
            print(f'It caused {damage} damage!\n')
            time.sleep(0.5)

            opponent.hp -= damage

            if opponent.hp > 0: 
                print(f'{opponent.name} has {opponent.hp} HP left.\n')
                #time.sleep(0.5)

            else:
                print(f'{opponent.name} has fainted!')
                time.sleep(3)

        else:
            time.sleep(0.3)
            print(f"{self.name} rested.\n")
            time.sleep(0.8)
            
