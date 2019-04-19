# 2019.04
# v0.8
# world_of_xeen_dictionary_maker.py

import re
import os.path
import pickle

bigequip = {}
bigattrib = {}

################################################## ERROR CHECKS

def readfiles():

    files = ['wox_weapons.txt', 'wox_armor.txt', 'wox_elements.txt',
            'wox_material.txt', 'wox_attributes.txt']

    exists = []

    for file in files:
        exists.append(os.path.isfile(file))

    if False in exists:
        error_message = ["Missing dictionary files. Please recheck:\n"]
        for index,file in enumerate(files):
            error_message.append(file+" Found"*exists[index])

        print("\n".join(error_message))

    ################################################## BUILDING EQUIPMENT DICTIONARY

    if exists[0]:
        with open('wox_weapons.txt', 'r') as f:
            data = f.read().splitlines()[1:]

        for line in data:
            if not line:
                continue
            weapon, strdamage, *_ = re.split(r'\s{2,}', line)
            no_rolls, dice_size = map(int, strdamage.split("d"))

            bigequip.setdefault(weapon.lower(),{})['damage'] = strdamage
            bigequip[weapon.lower()]['damagerange'] = (no_rolls, no_rolls*dice_size)
            bigequip[weapon.lower()]['type'] = 'weapon'

    if exists[1]:
        with open('wox_armor.txt', 'r') as f:
            data = f.read().splitlines()[1:]

        for line in data:
            if not line:
                continue
            weapon, ac, *_ = re.split(r'\s{2,}', line)
            bigequip.setdefault(weapon.lower(),{})['ac'] = int(ac)

    ################################################## BUILDING ATTRIBUTE DICTIONARY
    if exists[2]:
        with open('wox_elements.txt', 'r') as f:
            data = f.read().splitlines()[1:]

        for line in data:
            if line == "":
                continue
            elif len(line.split()) == 1:
                ELEM = line.title()
                continue
            attrib, res, dam, *_ = re.split(r'\s{2,}', line)
            bigattrib.setdefault(attrib.lower(),{})['element'] = ELEM
            bigattrib[attrib.lower()]['elem_res'] = res
            bigattrib[attrib.lower()]['elem_dam'] = dam
            bigattrib[attrib.lower()]['ac'] = int(ac)

    if exists[3]:
        with open('wox_material.txt', 'r') as f:
            data = f.read().splitlines()[1:]

        for line in data:
            if not line:
                continue
            material, to_hit, dam, ac, *_ = re.split(r'\s{2,}', line)
            bigattrib.setdefault(material.lower(),{})['to_hit'] = int(to_hit)
            bigattrib[material.lower()]['damage'] = int(dam)
            bigattrib[material.lower()]['ac'] = int(ac)


    if exists[4]:
        with open('wox_attributes.txt', 'r') as f:
            data = f.read().splitlines()[1:]

        for line in data:
            if line == "":
                continue
            elif len(line.split()) in (1,2):
                ATTRIBU = line.title()
                continue
            attrib, bonus, *_ = re.split(r'\s{2,}', line)
            bigattrib.setdefault(attrib.lower(),{})['attribute'] = f"{ATTRIBU}  {bonus}"

    return bigattrib, bigequip

########################################################

def build_pickle_file(bigattrib, bigequip):
    with open("dictionary.pkl", "wb") as handle:
        pickle.dump((bigattrib, bigequip), handle, protocol=3)
    return


# stats = [to hit, damage, elem_dam, elem_res, ac, attribute]
def update_stats(attr,name):
    name = name.lower().strip()
    attr = attr.lower().strip()
    ATTR_DIC = bigattrib.get(attr,{})
    EQU_DIC = bigequip.get(name,{})

    stats = [None]*6

    stats[0] = f"{ATTR_DIC.get('to_hit',0):+d}"
    result_attack = ((ATTR_DIC.get('damage',0) + att) for att in EQU_DIC.get('damagerange',(0,0)))
    stats[1] = f"{next(result_attack)} → {next(result_attack)}  ({EQU_DIC.get('damage',0)}  {ATTR_DIC.get('damage',0):+d})"
    stats[2] = f"{ATTR_DIC.get('element',0)}  {ATTR_DIC.get('elem_dam',0)}"
    stats[3] = f"{ATTR_DIC.get('element',0)}  {ATTR_DIC.get('elem_res',0)}"
    stats[4] = f"{EQU_DIC.get('ac',0) + ATTR_DIC.get('ac',0):+d}"
    stats[5] = ATTR_DIC.get('attribute', None)

    if attr == 'power': #Edge case
        for x in [2,3,5]: stats[x] = stats[x]+' (maybe)' 

    if not name:
        pass
    elif EQU_DIC['type'] == 'weapon':
        stats[3:5] = ['-']*2
    else:
        stats[:3] = ['-']*3

    return stats

def main():
    bigattrib, bigequip = readfiles()
    build_pickle_file(bigattrib, bigequip)
    print("[to hit, damage, elem_dam, elem_res, ac, attribute]")
    print(update_stats("fiery","long sword"))

if __name__ == "__main__": main()
