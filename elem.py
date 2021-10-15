import copy

elements = [None, 'Hydrogen', 'Helium', 'Lithium', 'Beryllium',
            'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',
            'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon',
            'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium',
            'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium',
            'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc',
            'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine',
            'Krypton', 'Rubidium', 'Strontium', 'Yttrium',
            'Zirconium', 'Niobium', 'Molybdenum', 'Technetium',
            'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium',
            'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine',
            'Xenon', 'Caesium', 'Barium', 'Lanthanum', 'Cerium',
            'Praseodymium', 'Neodymium', 'Promethium', 'Samarium',
            'Europium', 'Gadolinium', 'Terbium', 'Dysprosium',
            'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium',
            'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium',
            'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium',
            'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon',
            'Francium', 'Radium', 'Actinium', 'Thorium',
            'Protactinium', 'Uranium']


def make_atom(d):
    dic = {}
    for n, elem in enumerate(d):
        if n > 0:
            dic[elem] = n
    return dic


atom = make_atom(elements)







