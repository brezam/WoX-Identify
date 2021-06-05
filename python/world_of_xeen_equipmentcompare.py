#!/usr/bin/env python3
# world_of_xeen_equipmentcompare.py
# 2019.08
# v0.9.7

from tkinter import *
from tkinter import messagebox
import json
from pathlib import Path


def hlep():
    message = ("World of Xeen equipment information.\n\n"
               "v0.9.7")
    messagebox.showinfo(title="About", message=message)


def important_info(what):
    if what == 'material':
        message = ("Material enchantments on **accessories** do not "
                   "affect armor class and thus have no effect at all when equipped.\n\n"
                   "For example: steel ring, ebony belt, emerald pendant, etc. are useless")
    elif what == 'elemental':
        message = ("Elemental enchantments on weapons *only* grant the capacity to cause elemental "
                   "damage.\n\nOn other items, they *only* increase resistance."
                   "This is accounted for in the display result ('-').")
    elif what == 'special':
        message = ("\tSPECIAL WEAPON POWERS:\n\n"
                   "Beast Bopper   - 3x damage against Beasts\n"
                   "Bug Zapper     - 3x damage against Insects\n"
                   "Dragon Slayer  - 3x damage against Dragons\n"
                   "Golem Smasher  - 3x damage against Golems\n"
                   "Monster Masher - 3x damage against Monsters\n"
                   "Undead Eater   - 3x damage against Undead")
    else:
        message = "There should be something here."
    messagebox.showinfo(title="Important Info", message=message)


def color_label(att_fail, equ_fail, side, status_dots):
    status_dot = status_dots[side == 'L']
    if att_fail:
        status_dot[0].config(bg="red")
    else:
        status_dot[0].config(bg="green")
    if equ_fail:
        status_dot[1].config(bg="red")
    else:
        status_dot[1].config(bg="green")


def update_stats(attr, name, attributes_dict, equip_dict):
    name = name.strip().lower()
    attr = attr.strip().lower()
    ATTR_DIC = attributes_dict.get(attr, {})
    EQU_DIC = equip_dict.get(name, {})

    stats = [None]*6

    stats[0] = "{:+d}".format(ATTR_DIC.get('to_hit', 0))
    result_attack = ((ATTR_DIC.get('damage', 0) + att)
                     for att in EQU_DIC.get('damagerange', (0, 0)))
    stats[1] = "{} → {}  ({}  {:+d})".format(*result_attack,
                                             EQU_DIC.get('damage', 0), ATTR_DIC.get('damage', 0))
    stats[2] = "{}  {}".format(ATTR_DIC.get(
        'element', 0), ATTR_DIC.get('elem_dam', 0))
    stats[3] = "{}  {}".format(ATTR_DIC.get(
        'element', 0), ATTR_DIC.get('elem_res', 0))
    stats[4] = "{:+d}".format(EQU_DIC.get('ac', 0) + ATTR_DIC.get('ac', 0))
    stats[5] = ATTR_DIC.get('attribute', None)

    if attr == 'power':  # Edge case
        for x in [2, 3, 5]:
            stats[x] = stats[x]+' (maybe)'

    if not name:
        pass
    elif EQU_DIC.get('type') == 'weapon':
        stats[3:5] = ['-']*2
    else:
        stats[:3] = ['-']*3

    return stats, ATTR_DIC == {}, EQU_DIC == {}


def update_label(side, status_labels, status_dots, equip_vars, attr_vars, attributes_dict, equip_dict):
    stats, att_fail, equ_fail = update_stats(
        attr_vars[side == 'L'].get(),
        equip_vars[side == 'L'].get(),
        attributes_dict,
        equip_dict)
    stats = [str(x) for x in stats]
    status_labels[side == 'L'].set('\n'.join(stats))
    color_label(att_fail, equ_fail, side, status_dots)


def updatevariables(status_labels, status_dots, equip_vars, attr_vars, attributes_dict, equip_dict):
    update_label('L', status_labels, status_dots, equip_vars,
                 attr_vars, attributes_dict, equip_dict)
    update_label('R', status_labels, status_dots, equip_vars,
                 attr_vars, attributes_dict, equip_dict)


def load_dictionary_file():
    file = Path() / 'dictionary.json'
    if not file.exists():
        file = Path() / 'world_of_xeen_dictionary_maker' / 'dictionary.json'
        if not file.exists():
            print("Dictionary file (dictionary.json) not found.\n")
            input("Press Enter to exit.")
            raise SystemExit(1)
    with open(file, "r") as fp:
        bigattrib, bigequip = json.load(fp)
    return bigattrib, bigequip


def main():
    bigattrib, bigequip = load_dictionary_file()

    root = Tk()
    root.title("Might & Magic 4-5: World of Xeen -- Equipment Identifier  v0.9.7")

    menu = Menu(master=root)
    root.config(menu=menu)

    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Exit', command=root.quit)

    importantmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Important info', menu=importantmenu)
    importantmenu.add_command(
        label='Item Material Enchantments', command=lambda: important_info('material'))
    importantmenu.add_command(
        label='Item Elemental Enchantments', command=lambda: important_info('elemental'))
    importantmenu.add_command(
        label='Special Weapon Powers', command=lambda: important_info('special'))

    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About', command=hlep)
    helpmenu.add_separator()

    Label(master=root, text='Attribute | Name',
          relief="groove").grid(row=0, column=0, padx=5)

    attribute1, equipment1, attribute2, equipment2 = (
        StringVar() for _ in range(4))

    enter_atrib1 = Entry(master=root, textvariable=attribute1)
    enter_equip1 = Entry(master=root, textvariable=equipment1)
    enter_atrib2 = Entry(master=root, textvariable=attribute2)
    enter_equip2 = Entry(master=root, textvariable=equipment2)

    enter_atrib1.grid(row=0, column=1, padx=(0, 0), pady=5)
    enter_equip1.grid(row=0, column=2, padx=(0, 0), pady=5)

    Label(master=root, text='vs').grid(row=0, column=3)

    enter_atrib2.grid(row=0, column=4, padx=(0, 0), pady=5)
    enter_equip2.grid(row=0, column=5, padx=(0, 100), pady=5)

    for item in (enter_atrib1, enter_atrib2, enter_equip1, enter_equip2):
        item.bind('<Return>', lambda _: updatevariables(
            (stats1, stats2),
            (status_left, status_right),
            (equipment1, equipment2),
            (attribute1, attribute2),
            bigattrib,
            bigequip))

    status_left = [Label(master=root, bg="red", font=(
        'TkDefaultFont', 1)) for _ in range(2)]
    status_right = [Label(master=root, bg="red", font=(
        'TkDefaultFont', 1)) for _ in range(2)]

    status_left[0].grid(row=1, column=1, padx=0)
    status_left[1].grid(row=1, column=2, padx=0)
    status_right[0].grid(row=1, column=4, padx=0)
    status_right[1].grid(row=1, column=5, padx=(0, 100))

    DYNLAB = """to Hit:
    Physical Damage:
    Elemental Damage:
    Elemental Resistance:
    Armor Class Bonus:
    Attribute Bonus:"""

    Label(master=root, text=DYNLAB, justify="right").grid(
        row=2, column=0, pady=5)

    stats1 = StringVar()
    stats2 = StringVar()

    Label(master=root, textvariable=stats1).grid(row=2, column=1, columnspan=2)
    Label(master=root, textvariable=stats2).grid(
        row=2, column=4, columnspan=2, padx=(0, 100))

    Button(master=root, text="COMPARE", width=80, command=lambda: updatevariables(
        (stats1, stats2),
        (status_left, status_right),
        (equipment1, equipment2),
        (attribute1, attribute2),
        bigattrib,
        bigequip)).grid(row=4, column=0, columnspan=6)

    try:
        img = PhotoImage(file="game.gif")
        canvas = Canvas(master=root, width=80, height=80)
        canvas.grid(row=5, column=0, padx=10)
        canvas.create_image(40, 40, image=img)
        canvas2 = Canvas(master=root, width=80, height=80)
        canvas2.grid(row=5, column=5, padx=10)
        canvas2.create_image(40, 40, image=img)
    except TclError:
        pass

    root.mainloop()


if __name__ == "__main__":
    main()
