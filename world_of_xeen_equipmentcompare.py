# 2019.04
# v0.3.08.7c.A Mark IIc - Model Y
# world_of_xeen_equipmentcompare.py

from tkinter import *
from tkinter import messagebox
import world_of_xeen_dictionary as wox_dictionary

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

def update_label(side):
    stats_label = stats1 if side == 'L' else stats2
    equipment = equipment1 if side == 'L' else equipment2
    attribute = attribute1 if side == 'L' else attribute2
    stats = wox_dictionary.update_stats(attr=attribute.get(), name=equipment.get())
    stats = [str(x) for x in stats]
    stats_label.set('\n'.join(stats))
    return None

def updatevariables():
    update_label('L')
    update_label('R')
    return None


root = Tk()
root.title("Might & Magic 4-5: World of Xeen - Equipment Identifier for cheapskates."
           "  v0.3.08.7c.A Mark IIc - Model Y")

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

attribute1 = StringVar()
equipment1 = StringVar()
attribute2 = StringVar()
equipment2 = StringVar()

enter_atrib1 = Entry(master=root, textvariable=attribute1)
enter_equip1 = Entry(master=root, textvariable=equipment1)
enter_atrib2 = Entry(master=root, textvariable=attribute2)
enter_equip2 = Entry(master=root, textvariable=equipment2)

enter_atrib1.grid(row=0, column=1, padx=(0,0), pady=5)
enter_equip1.grid(row=0, column=2, padx=(0,0), pady=5)

Label(master=root, text='vs').grid(row=0, column=3)

enter_atrib2.grid(row=0, column=4, padx=(0,0), pady=5)
enter_equip2.grid(row=0, column=5, padx=(0,100), pady=5)

enter_atrib1.bind('<Return>', lambda _:updatevariables())
enter_equip1.bind('<Return>', lambda _:updatevariables())
enter_atrib2.bind('<Return>', lambda _:updatevariables())
enter_equip2.bind('<Return>', lambda _:updatevariables())


DYNLAB="""to Hit:
Physical Damage:
Elemental Damage:
Elemental Resistance:
Armor Class Bonus:
Attribute Bonus:"""

Label(master=root, text=DYNLAB, justify="right").grid(row=1, column=0, pady=5)

stats1 = StringVar()
stats2 = StringVar()

Label(master=root, textvariable=stats1).grid(row=1, column=1, columnspan=2)
Label(master=root, textvariable=stats2).grid(row=1, column=4, columnspan=2)

Button(master=root, text="COMPARE", width=80, command=updatevariables).grid(row=3, column=0, columnspan=6)

bottom_text = ("• Make sure to mispell just like the game does:\n"
               "e.g. 'Burgler', 'Wakazashi', 'Venemous'\n\n"
               "• Ignore Special Weapon powers such as \n"
               "Bug Zapper, Beast Bopper...\n"
               "(Check Important info on what they mean)\n\n"
               "• Use correct .txt files otherwise information is not reliable.\n"
               "                    Files found:")
Label(master=root, text=bottom_text, justify='left').grid(row=4, column=0, columnspan=6, pady=(30,0))


files_loaded = zip(wox_dictionary.files,wox_dictionary.exists)
loaded_str = '\n'.join([x+"  "+('\u2713' if y == True else 'X') for x,y in files_loaded])
Label(master=root, text=loaded_str, justify='right').grid(row=5, column=2, columnspan=3, pady=(0,30))

img = PhotoImage(file="game.gif")
canvas = Canvas(master=root, width=80, height=80)
canvas.grid(row=4, column=0, padx=10)
canvas.create_image(40, 40, image=img)
canvas2 = Canvas(master=root, width=80, height=80)
canvas2.grid(row=4, column=5, padx=10)
canvas2.create_image(40, 40, image=img)

root.mainloop()
