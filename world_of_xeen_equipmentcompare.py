# 2019.04
# v0.0.00.3c.A.3 Mark II
# world_of_xeen_equipmentcompare.py

from tkinter import *
from tkinter import messagebox
import world_of_xeen_dictionary as wox_dictionary

def hlep():
    messagebox.showinfo(title="About", message="World of Xeen equipment information."+
        "\n\nUncopyright© 2019-2046.")
    return None

def contac():
    message = "Email: bruno7497@gmail.com\n Only message me if you have spicy memes."
    messagebox.showinfo(title="Contact", message=message)
    return None

def important_info(what):
    if what == 'material':
        message = "Material enchantments on **accessories** do not " +\
            "affect armor class and thus have no effect at all when equipped.\n\n" +\
            "For example: steel ring, ebony belt, emerald pendant, etc. are useless"
    elif what == 'elemental':
        message = "Elemental enchantments on weapons *only* grant the capacity to cause elemental " +\
            "damage.\n\nOn other items, they *only* increase resistance."
    elif what == 'special':
        message = "\tSPECIAL WEAPON POWERS:\n\n" +\
        "Beast Bopper   - 3x damage against Beasts\n" +\
        "Bug Zapper     - 3x damage against Insects\n" +\
        "Dragon Slayer  - 3x damage against Dragons\n" +\
        "Golem Smasher  - 3x damage against Golems\n" +\
        "Monster Masher - 3x damage against Monsters\n" +\
        "Undead Eater   - 3x damage against Undead\n"
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
root.title("Might & Magic 4: World of Xeen -- Equipment Identifier for cheapskates. v0.0.00.3c.A.3 Mark II")

menu = Menu(root)
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

enter_atrib1.grid(row=0, column=1, padx=0, pady=5)
enter_equip1.grid(row=0, column=2, padx=(0,25), pady=5)
enter_atrib2.grid(row=0, column=3, padx=(25,0), pady=5)
enter_equip2.grid(row=0, column=4, padx=(0,50), pady=5)

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
Label(master=root, textvariable=stats2).grid(row=1, column=3, columnspan=2)

Button(master=root, text=f"{'COMPARE':^50}", command=updatevariables).grid(row=3, column=2, columnspan=2)

bottom_text = ("Make sure the .txt files are correct please.\n"
               "Ignore Special Weapon powers such as Bug Zapper, etc... (Check Important info)\n"
               "")
Label(master=root, text=bottom_text).grid(row=4, column=1, columnspan=3, pady=(30,10))

img = PhotoImage(file="game.gif")
canvas = Canvas(master=root, width=80, height=80)
canvas.grid(row=4, column=0, padx=10)
canvas.create_image(40, 40, image=img)

canvas2 = Canvas(master=root, width=80, height=80)
canvas2.grid(row=4, column=4, padx=10)
canvas2.create_image(40, 40, image=img)

root.mainloop()
