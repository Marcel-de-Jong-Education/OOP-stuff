from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random as r #For random damage and health
# Create an instance of Player
player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

weapon_weak = Weapon("Wooden Yo-yo", "Yo-yo", r.randint(13,14))


enemy_weak = Enemy("Milfo the Goblin", "Goblin", r.randint(15,18), r.randint(81,139))

# Print the player character details
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}\n")

print(
      f"Weapon Name: {weapon_weak.name}",'\n',
      f"Weapon Type: {weapon_weak.category}",'\n',
      f"Weapon Damage: {weapon_weak.damage}", '\n'
      )

print(
    f"Enemy Name: {enemy_weak.name}",'\n',
    f"Enemy Race: {enemy_weak.race}",'\n',
    f"Enemy Damage {enemy_weak.damage}",'\n',
    f"Enemy Health {enemy_weak.health}", '\n'
)

player_types = [
    player_character,
    Player('Aaliyah', 'Fairy', 'Tank', 2, 1024),
    Player('Harmony', 'Furry', 'Assassin', 150, 64),
    Player('Keylee', 'Cat Demiboy', 'Paladin', 64, 256)
]

weapon_types = [
    weapon_weak,
    Weapon('Titanium Gauntlets', 'Glove', 16),
    Weapon('Deadly Sabre', "Sword", 128),
    Weapon('Shock Hammer', 'Hammer', 64)
]

chosen_player = player_character

def select_player():
    a = True
    while a:
        print("Select Player:\n")
        for player in player_types:
            print("-", player.name)
        choice = input()
        for player in player_types:
            if choice == player.name: chosen_player = player; print("Selected player:", player.name); a = False; break
        if a: print("Invalid Selection! Try again!\n\n")
    
    a = True
    while a:
        print("Select Weapon:\n")
        for weapon in weapon_types:
            print("-", weapon.name)
        choice = input()
        for weapon in weapon_types:
            if choice == weapon.name: chosen_weapon = weapon; print("Selected weapon:", weapon.name, '\n', "Weapon type:", weapon.category); a= False; break
        if a: print("Invalid Selection! Try again!\n\n")

select_player()





    
