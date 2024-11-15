import numpy
from cv2 import cvtColor, imread, matchTemplate, minMaxLoc
from cv2 import COLOR_RGB2BGR, IMREAD_COLOR, TM_SQDIFF_NORMED
from glob import glob

def determine_profession(img):
    # Convert the PIL Image into a cv2 image.
    img = cvtColor(numpy.array(img), COLOR_RGB2BGR)

    professions = ['guard', 'scout', 'minefighter', 'watchperson']
    profession_list = []

    for profession in professions:
        prof_templates = glob(f'img/prof/{profession}/*.png')
        for t in prof_templates:
            template = imread(t, IMREAD_COLOR)
            result = matchTemplate(img, template, TM_SQDIFF_NORMED)
            min_val, _, _, _ = minMaxLoc(result)
            profession_list.append((profession, min_val, t))

    return sorted(profession_list, key=lambda x: x[1])[0]
