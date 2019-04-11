# 2019.04
# v0.0.00.3c.A.3 Mark II
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

    raise SystemExit("\n".join(error_message))

################################################## BUILDING EQUIPMENT DICTIONARY

with open('wox_weapons.txt', 'r') as f:
    data = f.read().splitlines()[1:]

for line in data:
    if line == "":
        continue
    weapon, strdamage, *_ = re.split(r'\s{2,}', line)
    no_rolls, dice_size = map(int, strdamage.split("d"))

    bigequip[weapon.lower()]['damage'] = strdamage
    bigequip[weapon.lower()]['damagerange'] = (no_rolls, no_rolls*dice_size)


with open('wox_armor.txt', 'r') as f:
    data = f.read().splitlines()[1:]

for line in data:
    if line == "":
        continue
    weapon, ac, *_ = re.split(r'\s{2,}', line)
    bigequip[weapon.lower()]['ac'] = int(ac)

################################################## BUILDING ATTRIBUTE DICTIONARY

with open('wox_material.txt', 'r') as f:
    data = f.read().splitlines()[1:]

for line in data:
    if line == "":
        continue
    material, to_hit, dam, ac, *_ = re.split(r'\s{2,}', line)
    bigattrib[material.lower()]['to_hit'] = int(to_hit)
    bigattrib[material.lower()]['damage'] = int(dam)
    bigattrib[material.lower()]['ac'] = int(ac)


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


with open('wox_attributes.txt', 'r') as f:
    data = f.read().splitlines()[1:]

for line in data:
    if line == "":
        continue
    elif len(line.split()) in (1,2):
        ATTRIBU = line.title()
        continue
    attrib, bonus, *_ = re.split(r'\s{2,}', line)
    bigattrib[attrib.lower()]['attribute'] = f"{ATTRIBU} {bonus}"

##################################################

# stats = [to hit, damage, elem_dam, elem_res, ac, attribute]
def update_stats(attr,name):

    ATTR_DIC = bigattrib[attr.lower().strip()]
    EQU_DIC = bigequip[name.lower()]

    stats = ['']*6
    stats[0] = ATTR_DIC['to_hit']

    if isinstance(EQU_DIC['damagerange'], int): 
        EQU_DIC['damagerange'] = (0,0)
    result_attack = ((ATTR_DIC['damage'] + att) for att in EQU_DIC['damagerange'])
    stats[1] = f"{next(result_attack)} → {next(result_attack)}  ({EQU_DIC['damage']}  {ATTR_DIC['damage']:+d})"

    stats[2] = ATTR_DIC['elem_dam']
    stats[3] = ATTR_DIC['elem_res']
    stats[4] = EQU_DIC['ac'] + ATTR_DIC['ac']
    stats[5] = ATTR_DIC['attribute']

    return stats

def main():
    print(update_stats("",""))
    print("You should be running the other file. world_of_xeen_equipmentcompare.py")
    input()

if __name__ == "__main__": main()
