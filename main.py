import requests

def get_class_details(class_name):
    request = requests.get(f'https://www.dnd5eapi.co/api/2014/classes/{class_name}')

    if request.status_code == 200:
        class_data = request.json()

    else:
        class_data = None

    print("\nProficiencies:\n-------------")
    for proficiency in class_data['proficiencies']:
        print(proficiency['name'])

    print("\nProficiency Choices:\n-------------")
    for proficiency in class_data['proficiency_choices']:
        print(proficiency['desc'])
        for option in proficiency['from']['options']:
            print(option['item']['name'])

    print("\nSubclasses:\n-------------")
    for subclass in class_data['subclasses']:
        print(subclass['name'])

    print("\nStarting Equipment:\n-------------")
    for equipment in class_data['starting_equipment']:
        print(equipment['equipment']['name'])

    if 'spellcasting' in class_data.keys():     
        print("\nSpellcasting:\n-------------")
        print(f"Spallcasting Ability: {class_data['spellcasting']['spellcasting_ability']['name']}")
        for  info in class_data['spellcasting']['info']:
            print(info['name'], end=':\n')
            for desc in info['desc']:
                print(f"\t{desc}")
            print()

        get_spells(class_name)


def get_spells(class_name):
    request = requests.get(f'https://www.dnd5eapi.co/api/2014/classes/{class_name}/spells')

    if request.status_code == 200:
        class_data = request.json()

    else:
        class_data = None

    print("\nSpells:\n-------------")
    for spell in class_data['results']:
        print(f'{spell['name']} - {spell['level']}')
        get_spell_details(spell['index'])

def get_spell_details(spell_name):
    request = requests.get(f'https://www.dnd5eapi.co/api/spells/{spell_name}')

    if request.status_code == 200:
        spell_data = request.json()

    else:
        spell_data = None

    print(f"\n{spell_data['name']}:\n-------------")
    if spell_data["higher_level"]:
        print("Higher Level:")
        for desc in spell_data['higher_level']:
            print(f"- {desc}")
    print(f"Range: {spell_data['range']}")
    print(f"Components: {spell_data['components']}")
    print(f"Duration: {spell_data['duration']}")
    
    for desc in spell_data['desc']:
        print(f"- {desc}")

def get_level_details(class_name):
    request = requests.get(f'https://www.dnd5eapi.co/api/classes/{class_name}/levels')

    if request.status_code == 200:
        class_data = request.json()

    else:
        class_data = None
    
    for level in class_data:
        print(f"\n{level['level']}:\n-------------")
        print(f"Ability Score Improvement: {level['ability_score_bonuses']}")
        print(f"Proficiency Bonus: {level['prof_bonus']}")
        for feature in level['features']:
            print(f"Feature: {feature['name']}")
        if 'spellcasting' in level.keys():

            print(f"Cantrips Known: {level['spellcasting']['cantrips_known']}")
            for spell_slot_level in range(1, 10):
                print(f"Spell Slots Level {spell_slot_level}: {level['spellcasting'][f'spell_slots_level_{spell_slot_level}']}")


        print(f"Class Specific:")

        for feature, value in level['class_specific'].items():
            print(f"{feature.replace("_"," ").title()}: {value}")           



for class_name in ['rogue', 'sorcerer', 'warlock', 'wizard']:
    print(class_name)
    get_level_details(class_name)
