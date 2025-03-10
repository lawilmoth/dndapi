import requests

def get_monster_info(monster_name):
    request = requests.get(f'https://www.dnd5eapi.co/api/monsters/{monster_name}')

    if request.status_code == 200:
        monster_data = request.json()

    else:
        monster_data = None

    print(f"\n{monster_data['name']}:\n-------------")
    print(f"Size: {monster_data['size']}")
    print(f"Type: {monster_data['type']}")
    print(f"Alignment: {monster_data['alignment']}")
    print(f"Armor Class:")
    for ac in monster_data['armor_class']:
        for key, value in ac.items():
            if key == 'armor':
                print("\rArmor:")
                for arm_dict in value:
                    print(f"\t{arm_dict['name']}")
                
            else:
                print(f"\t{key.title()}: {value}")
    print(f"Hit Points: {monster_data['hit_points']}")
    print(f"Hit Dice: {monster_data['hit_dice']}")
    print(f"Speed:")
    for key, value in monster_data['speed'].items():
        print(f"\t{key.title()}: {value}")
    print(f"Strength: {monster_data['strength']}")
    print(f"Dexterity: {monster_data['dexterity']}")
    print(f"Constitution: {monster_data['constitution']}")
    print(f"Intelligence: {monster_data['intelligence']}")
    print(f"Wisdom: {monster_data['wisdom']}")
    print(f"Charisma: {monster_data['charisma']}")

    print(f"Proficiencies:")
    for proficiency in monster_data['proficiencies']:
        print(f"\t{proficiency['proficiency']['name']}-{proficiency['value']}")

    print(f"Damage Vulnerabilities: ")
    for damage in monster_data['damage_vulnerabilities']:
        print(f"\t{damage.title()}")
    print(f"Damage Resistances:")
    for damage in monster_data['damage_resistances']:
        print(f"\t{damage.title()}")
    print(f"Damage Immunities: ")
    for damage in monster_data['damage_immunities']:
        print(f"\t{damage.title()}")
    print(f"Condition Immunities:")
    for condition in monster_data['condition_immunities']:
        print(f"\t{condition['name']}")
    print(f"Senses:")
    for key, value in monster_data['senses'].items():
        print(f"\t{key.title()}: {value}")
    print(f"Languages: {monster_data['languages']}")
    print(f"Challenge Rating: {monster_data['challenge_rating']}")
    
    for ability in monster_data['special_abilities']:
        print(f"\t{ability['name']}: {ability['desc']}")
    print(f"Actions:")
    for action in monster_data['actions']:
        print(f"\t{action['name']}: {action['desc']}")
        if 'attack_bonus' in action.keys():
            print(f"\t\tAttack Bonus: {action['attack_bonus']}")
        if 'damage' in action.keys():
            for dmg in action['damage']:
                print(f"\t\tDamage: {dmg['damage_dice']} {dmg['damage_type']['name']}")
    for la in monster_data['legendary_actions']:
        print(f"\t{la['name']}: {la['desc']}")
        
    if 'image' in monster_data.keys():
        print(f"Image: {monster_data['image']}")
get_monster_info('tarrasque')
