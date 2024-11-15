from re import sub

weapons_list = [
    {
        'name': "guard's kanabo",
        'faction': None,
        'element': 'tempestae',
        'type': 'melee',
    },
    {
        'name': "guard's sword",
        'faction': None,
        'element': None,
        'type': 'melee',
    },
    {
        'name': "recruit's sword",
        'faction': None,
        'element': None,
        'type': 'melee',
    },
    {
        'name': "guard's halberd",
        'faction': None,
        'element': 'cryonae',
        'type': 'melee',
    },
    {
        'name': "guard's longsword",
        'faction': None,
        'element': None,
        'type': 'melee',
    },
    {
        'name': "guard's pike",
        'faction': None,
        'element': 'arborae',
        'type': 'melee',
    },
    {
        'name': "carthian plumbatae",
        'faction': None,
        'element': 'infernae',
        'type': 'ranged',
    },
    {
        'name': "guard's plumbatae",
        'faction': None,
        'element': 'tempestae',
        'type': 'ranged',
    },
    {
        'name': "recruit's bow",
        'faction': None,
        'element': None,
        'type': 'ranged',
    },
    {
        'name': "guard's bow",
        'faction': None,
        'element': None,
        'type': 'ranged',
    },
    {
        'name': "flanged mace",
        'faction': 'cryoknight',
        'element': 'tempestae',
        'type': 'melee',
    },
    {
        'name': "shortsword",
        'faction': 'cryoknight',
        'element': 'infernae',
        'type': 'melee',
    },
    {
        'name': "rapier",
        'faction': 'cryoknight',
        'element': 'cryonae',
        'type': 'melee',
    },
    {
        'name': "battleaxe",
        'faction': 'cryoknight',
        'element': 'necromae',
        'type': 'melee',
    },
    {
        'name': "broadsword",
        'faction': 'cryoknight',
        'element': 'cryonae',
        'type': 'melee',
    },
    {
        'name': "longsword",
        'faction': 'cryoknight',
        'element': None,
        'type': 'melee',
    },
    {
        'name': "throwing knives",
        'faction': 'cryoknight',
        'element': 'infernae',
        'type': 'ranged',
    },
    {
        'name': "throwing axes",
        'faction': 'cryoknight',
        'element': 'tempestae',
        'type': 'ranged',
    },
    {
        'name': "throwing twinblades",
        'faction': 'cryoknight',
        'element': None,
        'type': 'ranged',
    },
    {
        'name': "throwing rings",
        'faction': 'cryoknight',
        'element': 'cryonae',
        'type': 'ranged',
    },
    {
        'name': "metal javelins",
        'faction': 'cryoknight',
        'element': 'necromae',
        'type': 'ranged',
    },
    {
        'name': "metal bow",
        'faction': 'cryoknight',
        'element': 'arborae',
        'type': 'ranged',
    },
    {
        'name': "club",
        'faction': 'guardian',
        'element': 'necromae',
        'type': 'melee',
    },
    {
        'name': "cudgel",
        'faction': 'guardian',
        'element': None,
        'type': 'melee',
    },
    {
        'name': "truncheon",
        'faction': 'guardian',
        'element': 'arborae',
        'type': 'melee',
    },
    {
        'name': "poleaxe",
        'faction': 'guardian',
        'element': 'infernae',
        'type': 'melee',
    },
    {
        'name': "quarterstaff",
        'faction': 'guardian',
        'element': 'arborae',
        'type': 'melee',
    },
    {
        'name': "spear",
        'faction': 'guardian',
        'element': 'cryonae',
        'type': 'melee',
    },
    {
        'name': "blowpipe",
        'faction': 'guardian',
        'element': 'tempestae',
        'type': 'ranged',
    },
    {
        'name': "javelins",
        'faction': 'guardian',
        'element': None,
        'type': 'ranged',
    },
    {
        'name': "light crossbow",
        'faction': 'guardian',
        'element': 'cryonae',
        'type': 'ranged',
    },
    {
        'name': "heavy crossbow",
        'faction': 'guardian',
        'element': 'necromae',
        'type': 'ranged',
    },
    {
        'name': "longbow",
        'faction': 'guardian',
        'element': 'arborae',
        'type': 'ranged',
    },
    {
        'name': "recurve bow",
        'faction': 'guardian',
        'element': 'infernae',
        'type': 'ranged',
    },
    {
        'name': "hammerfist",
        'faction': 'hammermage',
        'element': None,
        'type': 'melee',
    },
    {
        'name': "stone mace",
        'faction': 'hammermage',
        'element': 'arborae',
        'type': 'melee',
    },
    {
        'name': "war hammer",
        'faction': 'hammermage',
        'element': 'tempestae',
        'type': 'melee',
    },
    {
        'name': "double headed hammer",
        'faction': 'hammermage',
        'element': 'infernae',
        'type': 'melee',
    },
    {
        'name': "great hammer",
        'faction': 'hammermage',
        'element': 'tempestae',
        'type': 'melee',
    },
    {
        'name': "great stone mace",
        'faction': 'hammermage',
        'element': 'necromae',
        'type': 'melee',
    },
    {
        'name': "bolas",
        'faction': 'hammermage',
        'element': None,
        'type': 'ranged',
    },
    {
        'name': "throwing stones",
        'faction': 'hammermage',
        'element': 'necromae',
        'type': 'ranged',
    },
    {
        'name': "sling",
        'faction': 'hammermage',
        'element': 'arborae',
        'type': 'ranged',
    },
    {
        'name': "stone discs",
        'faction': 'hammermage',
        'element': 'cryonae',
        'type': 'ranged',
    },
    {
        'name': "throwing clubs",
        'faction': 'hammermage',
        'element': 'infernae',
        'type': 'ranged',
    },
    {
        'name': "throwing hammers",
        'faction': 'hammermage',
        'element': 'tempestae',
        'type': 'ranged',
    }
]

armor_list = [
    # Guard
    {'faction': None, 'name': 'guard strapped helmet'},
    {'faction': None, 'name': 'guard leather mail helmet'},
    {'faction': None, 'name': 'guard helmet studded helmet'},
    {'faction': None, 'name': 'guard studded helmet'},
    {'faction': None, 'name': 'guard ribbed torso'},
    {'faction': None, 'name': 'guard chainmail torso'},
    {'faction': None, 'name': 'guard studded torso'},
    {'faction': None, 'name': 'guard padded torso'},
    {'faction': None, 'name': 'guard leather mail torso'},
    {'faction': None, 'name': 'guard studded leather gloves'},
    {'faction': None, 'name': 'guard pulled leather gloves'},
    {'faction': None, 'name': 'guard studded legs'},
    {'faction': None, 'name': 'guard ribbed legs'},
    {'faction': None, 'name': 'guard chainmail legs'},
    {'faction': None, 'name': 'guard leather mail legs'},
    {'faction': None, 'name': 'guard padded legs'},
    {'faction': None, 'name': 'guard round shield'},
    {'faction': None, 'name': 'guard elegant shield'},
    {'faction': None, 'name': 'guard tower shield'},
    {'faction': None, 'name': 'guard heater shield'},
    {'faction': None, 'name': 'guard steel toe boots'},
    {'faction': None, 'name': 'guard pulled leather boots'},

    # Hammermage
    {'faction': 'hammermage', 'name': 'flared robe bottom'},
    {'faction': 'hammermage', 'name': 'flared robe top'},
    {'faction': 'hammermage', 'name': 'leather helm'},
    {'faction': 'hammermage', 'name': 'polished stone shield'},
    {'faction': 'hammermage', 'name': 'stonesheen hood'},
    {'faction': 'hammermage', 'name': 'sparkweave hood'},
    {'faction': 'hammermage', 'name': 'stonesheen robe top'},
    {'faction': 'hammermage', 'name': 'stonesheen robe bottom'},
    {'faction': 'hammermage', 'name': 'stonesheen boots'},
    {'faction': 'hammermage', 'name': 'stonesheen gloves'},
    {'faction': 'hammermage', 'name': 'stone slab shield'},
    {'faction': 'hammermage', 'name': 'stone chunk shield'},

    # Guardian
    {'faction': 'guardian', 'name': 'angular bone legs'},
    {'faction': 'guardian', 'name': 'angular bone torso'},
    {'faction': 'guardian', 'name': 'bone boots'},
    {'faction': 'guardian', 'name': 'bone circlet'},
    {'faction': 'guardian', 'name': 'bone gauntlets'},
    {'faction': 'guardian', 'name': 'horned helmet'},
    {'faction': 'guardian', 'name': 'polished bone cap'},
    {'faction': 'guardian', 'name': 'polished bone legs'},
    {'faction': 'guardian', 'name': 'polished bone torso'},
    {'faction': 'guardian', 'name': 'rib torso'},
    {'faction': 'guardian', 'name': 'wooden hexagon shield'},
    {'faction': 'guardian', 'name': 'wooden round shield'},
    {'faction': 'guardian', 'name': 'wooden square shield'},

    # Cryoknight
    {'faction': 'cryoknight', 'name': 'great helm'},
    {'faction': 'cryoknight', 'name': 'sallet helmet'},
    {'faction': 'cryoknight', 'name': 'kettle helmet'},
    {'faction': 'cryoknight', 'name': 'chainmail torso'},
    {'faction': 'cryoknight', 'name': 'plate torso'},
    {'faction': 'cryoknight', 'name': 'cuirass'},
    {'faction': 'cryoknight', 'name': 'plate gauntlets'},
    {'faction': 'cryoknight', 'name': 'plate legs'},
    {'faction': 'cryoknight', 'name': 'chainmail legs'},
    {'faction': 'cryoknight', 'name': 'plate boots'},
    {'faction': 'cryoknight', 'name': 'metal kite shield'},
    {'faction': 'cryoknight', 'name': 'metal heater shield'},
    {'faction': 'cryoknight', 'name': 'metal buckler'},
]


def determine_item_name(item):
    return (item.lower()
            .replace('guards', "guard's")
            .replace('gurd', 'guard')
            .replace('leathlr', 'leather'))


def determine_item_untuned(ocr):
    return (len([r for r in ocr if "obelisk" in r]) > 0)

def determine_item_rarity(ocr):
    # Check to see if the first index of the OCR result includes
    # something other than the item rarity.
    el_contains_item = len(
        ocr[0].replace('UNCOMMON', '')
        .replace('COMMON', '')
        .replace('RARE', '')
        .replace('EPIC', '')
    ) != 0

    if el_contains_item:
        split = ocr[0].split(' ')
        ocr.insert(0, split[0])
        ocr[1] = ' '.join(split[1:])

    if ('COMMON' in ocr[1] or
            'UNCOMMON' in ocr[1] or
            'RARE' in ocr[1] or
            'EPIC' in ocr[1]):
        split = ocr[1].split(' ')
        ocr[0] = split[0]
        ocr[1] = ' '.join(split[1:])

    return ocr, ocr[0].lower()


def determine_item_level(ocr):
    return int(ocr[-1])


def determine_item_characteristics(item):
    weapon = next((weapon for weapon in weapons_list if weapon['name'] == item), None)

    if weapon:
        return 'weapon', weapon

    armor = next((armor for armor in armor_list if armor['name'] == item), None)
    if armor:
        return 'armor', armor

    return 'UNKNOWN', None


def determine_item_value(val):
    value = sub('[^0-9]', '', val)
    # Sometimes OCR thinks the icon is a number too.
    # We only need the first 3 characters from this as things always round down.
    # This may be an issue in the future if we have items with gold prices over 999.
    if len(value) >= 3 and value.isnumeric():
        return int(value[:3])
    elif value.isnumeric():
        # Convert single and double-digit item values into silver values
        # for example: 1s -> 1000, 23s -> 23000
        # Will become an issue when we encounter items with gold value.
        return int(value) * 1000

    return 0


def determine_item_stats_and_value(ocr, type, characteristics):
    stats_value = {
        'impact_res': None,
        'cryonae_res': None,
        'arborae_res': None,
        'tempestae_res': None,
        'infernae_res': None,
        'necromae_res': None,
        'strength': None,
        'magic_chance': None,
        'magic_element': None,
        'value': None,
        'faction': None,
    }

    value_pos = 3

    if type == 'armor':
        stats_value['faction'] = characteristics['faction']
        # Check to see if the list item is numeric when spaces are removed
        # 99.9% of samples have the stats in index 2.
        stats_pos = 2 if ocr[2].replace(' ',  '').isnumeric() else 3
        # This fixes bugged/06.png (it adds an additional 'F' into the list)
        value_pos = 4 if stats_pos == 3 else 3

        # Now we split the stats index and check that it has a length of 6 as there are
        # 6 different resistances.
        stats = ocr[stats_pos].split(' ')
        if len(stats) != 6:
            stats = f'{ocr[stats_pos]} {ocr[stats_pos + 1]}'.split(' ')
            value_pos = 4 if stats_pos == 2 else 5
        if len(stats) != 6:
            stats = f'{ocr[stats_pos]} {ocr[stats_pos + 1]} {ocr[stats_pos + 2]}'.split(' ')
            value_pos = 5 if stats_pos == 2 else 6

        if len(stats) != 6:
            # We can't figure out the stats from the data, so return it empty.
            return stats_value

        # Set the resistance values.
        try:
            stats_value['impact_res'] = int(stats[0])
            stats_value['cryonae_res'] = int(stats[1])
            stats_value['arborae_res'] = int(stats[2])
            stats_value['tempestae_res'] = int(stats[3])
            stats_value['infernae_res'] = int(stats[4])
            stats_value['necromae_res'] = int(stats[5])
        except ValueError:
            print('Needs manual intervention!')

        # Determine the value of an armor piece.
        stats_value['value'] = determine_item_value(ocr[value_pos])
    elif type == 'weapon':
        stats_value['faction'] = characteristics['faction']
        # Sometimes magic chance gets bundled in with strength, so check for that.
        split = ocr[2].split(' ')
        if (len(split) > 1):
            ocr[2] = split[0]
            ocr.insert(3, split[1])

        stats_value['strength'] = int(sub('[^0-9]', '', ocr[2]))

        # We need to remove the % sign from the magic chance.
        magic_chance = sub(r'(%\d+)|(%)', '', ocr[3])
        magic_chance = sub('[^0-9]', '', magic_chance)
        # Only take the first 2 characters until we can confirm magic_chance can be 100%
        magic_chance = int(magic_chance[:2])

        if magic_chance != '0':
            stats_value['magic_chance'] = magic_chance
            # Use the defined element from the item characteristics.
            stats_value['magic_element'] = characteristics['element']


        value_pos = 7 if 'hand' in ocr[6].lower() else 6
        stats_value['value'] = determine_item_value(ocr[value_pos])

    return ocr, stats_value

