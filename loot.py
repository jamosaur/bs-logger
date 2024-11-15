import easyocr
import numpy
import requests
from PIL import Image

from image_utils import determine_profession
from items import determine_item_name, determine_item_rarity, determine_item_untuned, determine_item_level, \
    determine_item_characteristics, determine_item_stats_and_value


async def extract_loot(file_url, remote=True):
    if remote:
        img = Image.open(requests.get(file_url, stream=True).raw)
    else:
        img = Image.open(file_url)

    width, height = img.size
    resized_image = img.resize((width * 4, height * 4))

    profession = determine_profession(img)

    pic = numpy.array(resized_image)
    reader = easyocr.Reader(['en'])
    ocr_result = reader.readtext(pic, detail=0, paragraph=True)

    ocr = list(filter(bool, ocr_result))
    ocr, item_rarity = determine_item_rarity(ocr)
    print(ocr)
    item_name = determine_item_name(ocr[1])
    item_untuned = determine_item_untuned(ocr)
    item_level = determine_item_level(ocr)
    item_type, characteristics = determine_item_characteristics(item_name)
    ocr, stats_value = determine_item_stats_and_value(ocr, item_type, characteristics)

    loot_item = {
        'type': item_type,
        'coins_drop': None,
        'qty': None,
        'item': item_name,
        'value': stats_value['value'],
        'real_value': None,
        'rarity': item_rarity,
        'untuned': item_untuned,
        'level_req': item_level,
        'impact_res': stats_value['impact_res'],
        'cryonae_res': stats_value['cryonae_res'],
        'arborae_res': stats_value['arborae_res'],
        'tempestae_res': stats_value['tempestae_res'],
        'infernae_res': stats_value['infernae_res'],
        'necromae_res': stats_value['necromae_res'],
        'strength': stats_value['strength'],
        'magic_chance': stats_value['magic_chance'],
        'magic_element': stats_value['magic_element'],
        'faction': stats_value['faction'],
        'profession': profession[0]
    }

    return loot_item


def create_coins_drop(amount):
    return {
        'type': 'currency',
        'coins_drop': amount,
        'qty': None,
        'item': 'coins',
        'value': None,
        'real_value': None,
        'rarity': None,
        'untuned': None,
        'level_req': None,
        'impact_res': None,
        'cryonae_res': None,
        'arborae_res': None,
        'tempestae_res': None,
        'infernae_res': None,
        'necromae_res': None,
        'strength': None,
        'magic_chance': None,
        'magic_element': None,
        'faction': None,
        'profession': None
    }

if __name__ == '__main__':
    print('Hello!')
