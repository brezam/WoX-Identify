# 2019.04
# v0.9.3
# world_of_xeen_equipmentcompare.py

from tkinter import *
from tkinter import messagebox
import pickle
from pathlib import Path

def hlep():
    message = ("World of Xeen equipment information.\n\n"
                "I made this because I was annoyed.\n"
                "Don't expect much out of it.\n\n\n"
                "Uncopyright© 2019-2046.")
    messagebox.showinfo(title="About", message=message)
    return None

def contac():
    message = "Email: bruno7497@gmail.com\nOnly message me if you have spicy memes."
    messagebox.showinfo(title="Contact", message=message)
    return None

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
    return None

def color_label(att_fail, equ_fail, side):
    status_label = status_left if side == "L" else status_right
    if att_fail:
        status_label[0].config(bg="red")
    else:
        status_label[0].config(bg="green")
    if equ_fail:
        status_label[1].config(bg="red")
    else:
        status_label[1].config(bg="green")
    return

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
    elif EQU_DIC.get('type') == 'weapon':
        stats[3:5] = ['-']*2
    else:
        stats[:3] = ['-']*3

    return stats, ATTR_DIC == {}, EQU_DIC == {}

def update_label(side):
    stats_label = stats1 if side == 'L' else stats2
    equipment = equipment1 if side == 'L' else equipment2
    attribute = attribute1 if side == 'L' else attribute2
    stats, att_fail, equ_fail  = update_stats(attr=attribute.get(), name=equipment.get())
    stats = [str(x) for x in stats]
    stats_label.set('\n'.join(stats))
    color_label(att_fail, equ_fail, side)
    return

def updatevariables():
    update_label('L')
    update_label('R')
    return None

def load_dictionary_file(expected_pkl_size):
    file = Path() / 'dictionary.pkl'
    if not file.exists():
        file = Path() / 'world_of_xeen_dictionary_maker' / 'dictionary.pkl'
        if not file.exists():
            print("Dictionary file (dictionary.pkl) not found.\n")
            input("Press Enter to exit.")
            raise SystemExit()

    with open(file, "rb") as handle:
        bigattrib, bigequip = pickle.load(handle)
    
    size = file.stat().st_size
    ignoretxt = Path() / 'ignore.txt'

    if size != expected_pkl_size and not ignoretxt.exists():
        print("Maybe you have the wrong dictionary.pkl file. Use it anyway?")
        answer = input("[Y]es, [N]o, [I]gnore this warning for all time.\n>").lower()
        if answer[:1] == 'n':
            raise SystemExit()
        if answer[:1] == 'i':
            with open("ignore.txt", "w") as f:
                pass

    return bigattrib, bigequip, size

expected_pkl_size = 8749
bigattrib, bigequip, pkl_file_size = load_dictionary_file(expected_pkl_size)

root = Tk()
root.title("Might & Magic 4-5: World of Xeen -- Equipment Identifier  v0.9.2")

menu = Menu(master=root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)

importantmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Important info', menu=importantmenu)
importantmenu.add_command(label='Item Material Enchantments', command= lambda: important_info('material'))
importantmenu.add_command(label='Item Elemental Enchantments', command= lambda: important_info('elemental'))
importantmenu.add_command(label='Special Weapon Powers', command= lambda: important_info('special'))


helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=hlep)
helpmenu.add_separator()
helpmenu.add_command(label='Contact', command=contac)


Label(master=root, text='Attribute | Name', relief="groove").grid(row=0, column=0, padx=5)

attribute1, equipment1, attribute2, equipment2 = (StringVar() for _ in range(4))

enter_atrib1 = Entry(master=root, textvariable=attribute1)
enter_equip1 = Entry(master=root, textvariable=equipment1)
enter_atrib2 = Entry(master=root, textvariable=attribute2)
enter_equip2 = Entry(master=root, textvariable=equipment2)

enter_atrib1.grid(row=0, column=1, padx=(0,0), pady=5)
enter_equip1.grid(row=0, column=2, padx=(0,0), pady=5)

Label(master=root, text='vs').grid(row=0, column=3)

enter_atrib2.grid(row=0, column=4, padx=(0,0), pady=5)
enter_equip2.grid(row=0, column=5, padx=(0,100), pady=5)

for item in (enter_atrib1, enter_atrib2, enter_equip1, enter_equip2):
    item.bind('<Return>', lambda _:updatevariables())

status_left = [Label(master=root, bg="red", font=('TkDefaultFont',1)) for _ in range(2)]
status_right = [Label(master=root, bg="red", font=('TkDefaultFont',1)) for _ in range(2)]


status_left[0].grid(row=1, column=1, padx=0)
status_left[1].grid(row=1, column=2, padx=0)
status_right[0].grid(row=1, column=4, padx=0)
status_right[1].grid(row=1, column=5, padx=(0,100))

DYNLAB="""to Hit:
Physical Damage:
Elemental Damage:
Elemental Resistance:
Armor Class Bonus:
Attribute Bonus:"""

Label(master=root, text=DYNLAB, justify="right").grid(row=2, column=0, pady=5)

stats1 = StringVar()
stats2 = StringVar()

Label(master=root, textvariable=stats1).grid(row=2, column=1, columnspan=2)
Label(master=root, textvariable=stats2).grid(row=2, column=4, columnspan=2)

Button(master=root, text="COMPARE", width=80, command=updatevariables).grid(row=4, column=0, columnspan=6)

bottom_text = ("• Make sure to mispell just like the game does:\n"
               "e.g. 'Burgler', 'Wakazashi', 'Venemous'\n\n"
               "• Ignore Special Weapon powers such as \n"
               "Bug Zapper, Beast Bopper...\n"
               "(Check Important info on what they mean)\n\n"
               "• Use correct .pkl file otherwise information is not reliable.")
Label(master=root, text=bottom_text, justify='left').grid(row=5, column=0, columnspan=6, pady=(30,0))

loaded_pkl = (".pkl size found: {} bytes\n".format(pkl_file_size)+
              ".pkl size expected: {} bytes".format(expected_pkl_size))
Label(master=root, text=loaded_pkl, justify='right').grid(row=6, column=2, columnspan=3, pady=(0,30))

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
