import json

def format_for_csv(username, loot_object):
    return ','.join([
        username if username else '',
        'None',
        '',
        loot_object['type'].title() if loot_object['type'] else '',
        str(loot_object['coins_drop']) if loot_object['coins_drop'] else '',
        '',
        loot_object['item'].title().replace("'S", "'s") if loot_object['item'] else '',
        str(loot_object['value']) if loot_object['value'] else '',
        '',
        str(loot_object['rarity'].title()) if loot_object['rarity'] else '',
        '' if loot_object['type'] == 'currency' else ('Yes' if loot_object['untuned'] else 'No'),
        str(loot_object['level_req']) if loot_object['level_req'] else '',
        str(loot_object['impact_res']) if loot_object['impact_res'] else '',
        str(loot_object['cryonae_res']) if loot_object['cryonae_res'] else '',
        str(loot_object['arborae_res']) if loot_object['arborae_res'] else '',
        str(loot_object['tempestae_res']) if loot_object['tempestae_res'] else '',
        str(loot_object['infernae_res']) if loot_object['infernae_res'] else '',
        str(loot_object['necromae_res']) if loot_object['necromae_res'] else '',
        str(loot_object['strength']) if loot_object['strength'] else '',
        str(loot_object['magic_chance']) if loot_object['magic_chance'] else '',
        str(loot_object['magic_element'].title()) if loot_object['magic_element'] else '',
        str(loot_object['faction'].title()) if loot_object['faction'] else '',
        str(loot_object['profession']) if loot_object['profession'] else ''
    ])

def format_for_json(username, loot_object):
    loot_object['username'] = username

    return json.dumps(loot_object, indent=4)
