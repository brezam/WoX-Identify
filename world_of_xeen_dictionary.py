# 2019.04
# v0.3.08.7c.A Mark IIc - Model Y
# world_of_xeen_dictionary.py

import re
import os.path
from collections import defaultdict


bigequip = defaultdict(lambda: defaultdict(int))
bigattrib = defaultdict(lambda: defaultdict(int))

################################################## ERROR CHECKS

files = ['wox_weapons.txt', 'wox_armor.txt', 'wox_elements.txt',
        'wox_material.txt', 'wox_attributes.txt']

exists = []

for file in files:
    exists.append(os.path.isfile(file))

if False in exists:
    error_message = ["Missing dictionary files. Please recheck:\n"]
    for index,file in enumerate(files):
        error_message.append(f"{file} {exists[index]},")

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

        bigequip[weapon.lower()]['damage'] = strdamage
        bigequip[weapon.lower()]['damagerange'] = (no_rolls, no_rolls*dice_size)
        bigequip[weapon.lower()]['type'] = 'weapon'

if exists[1]:
    with open('wox_armor.txt', 'r') as f:
        data = f.read().splitlines()[1:]

    for line in data:
        if not line:
            continue
        weapon, ac, *_ = re.split(r'\s{2,}', line)
        bigequip[weapon.lower()]['ac'] = int(ac)

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
        bigattrib[attrib.lower()]['element'] = ELEM
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
        bigattrib[material.lower()]['to_hit'] = int(to_hit)
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
        bigattrib[attrib.lower()]['attribute'] = f"{ATTRIBU}  {bonus}"

##################################################

# stats = [to hit, damage, elem_dam, elem_res, ac, attribute]
def update_stats(attr,name):
    name = name.lower().strip()
    attr = attr.lower().strip()
    ATTR_DIC = bigattrib[attr]
    EQU_DIC = bigequip[name]

    stats = ['']*6

    if isinstance(EQU_DIC['damagerange'], int): 
        EQU_DIC['damagerange'] = (0,0)

    stats[0] = f"{ATTR_DIC['to_hit']:+d}"
    result_attack = ((ATTR_DIC['damage'] + att) for att in EQU_DIC['damagerange'])
    stats[1] = f"{next(result_attack)} → {next(result_attack)}  ({EQU_DIC['damage']}  {ATTR_DIC['damage']:+d})"
    stats[2] = f"{ATTR_DIC['element']}  {ATTR_DIC['elem_dam']}"
    stats[3] = f"{ATTR_DIC['element']}  {ATTR_DIC['elem_res']}"
    stats[4] = f"{EQU_DIC['ac'] + ATTR_DIC['ac']:+d}"
    stats[5] = ATTR_DIC['attribute']

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
    print(update_stats("",""))
    print("You should be running the other file. world_of_xeen_equipmentcompare.py\n")
    input("Press enter to finish: >")

if __name__ == "__main__": main()
