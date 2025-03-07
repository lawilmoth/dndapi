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

get_class_details('bard')
