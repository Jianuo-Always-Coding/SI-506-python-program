# SI 506 Lecture 05

# 1.0 SEQUENCES: STRINGS, LISTS, AND TUPLES

# 1.1 String basics

comedy_series = 'Monty Python'

# The object's unique identifier in memory
# comedy_series_id = id(comedy_series)

# print(f"\n1.1.1 comedy_series (id={comedy_series_id}) = {comedy_series}")

# Return the object's type
# comedy_series_type = type(comedy_series)

# print(f"\n1.1.2 comedy_series type (id={comedy_series_id}) = {comedy_series_type}")

# Return the object's length
# comedy_series_len = len(comedy_series)

# print(f"\n1.1.3 comedy_series length (id={comedy_series_id}) = {comedy_series_len}")

# UNCOMMENT: Immutability check
# comedy_series[0] = 'm' # TypeError: 'str' object does not support item assignment

# String concatenation
# comedy_series = None # TODO concatenate two strings

# print(f"\n1.1.4 comedy_series (id={comedy_series_id}) = {comedy_series}")


# 1.2 LIST BASICS

pythons = [
    'Graham Chapman',
    'John Cleese',
    'Terry Jones',
    'Eric Idle',
    'Michael Palin'
    ]

# The object's unique identifier in memory
pythons_id = id(pythons)

# print(f"\n1.2.1 pythons (id={id(pythons)}) = {pythons}")

# Return the type
pythons_type = type(pythons)

# print(f"\n1.2.2 pythons type (id={id(pythons)}) = {pythons_type}")

# Return the length
pythons_len = len(pythons)

# print(f"\n1.2.3 pythons len (id={id(pythons)}) = {pythons_len}")

# TODO Uncomment

# In-place method call mutates the list.
# pythons.append('Terry Gilliam')
# pythons.insert(-1, 'Terry Gilliam')
# pythons.extend(['Terry Gilliam'])

# print(f"\n1.2.4 pythons (id={id(pythons)}) = {pythons}")

# List concatenation
pythons = None # TODO add Neil Innes

# print(f"\n1.2.5 pythons (id={id(pythons)}) = {pythons}") # new identity

# 1.3 Tuple basics

silly_walks = ('Monty Python', 'Sketch', 'The Ministry of Silly Walks', '15 September 1970')

# The object's unique identifier in memory
silly_walks_id = id(silly_walks)

# print(f"\n1.3.1 silly_walks (id={id(silly_walks)}) = {silly_walks}")

# Return the type
silly_walks_type = type(silly_walks)

# print(f"\n1.3.2 silly_walks type (id={id(silly_walks)}) = {silly_walks}")

# Return the length
silly_walks_len = len(silly_walks)

# print(f"\n1.3.3 silly_walks len (id={id(silly_walks)}) = {silly_walks_len}")

# Single item tuple

python_theme_song = None # TODO single item tuple

# print(f"\n1.3.4 Flying Circus theme song = {python_theme_song}")

python_theme_song = None # TODO tuple concatenation

# print(f"\n1.3.5 Flying Circus theme song composer = {python_theme_song}")

holy_grail = (
    'Monty Python and the Holy Grail',
    1975,
    [
        'Arthur, King of the Britons',
        'Sir Lancelot the Brave',
        'Sir Bedevere the Wise',
        'Sir Galahad the Pure'
        ]
    )

# holy_grail[1] = '3 April 1975' # Illegal

holy_grail[2].append('Patsy') # Mutates tuple list item with a new element

# print(f"\n1.3.6 Tuple mutable elements = {holy_grail}")


## 2.0 CREATE A LIST FROM A STRING

# 2.0.1 str.split()

sketch_comedy = "Monty Python's Flying Circus"
words = sketch_comedy.split()

# print(f"\n2.0.1.1 Split title = {words}")

sketches = 'Dead Parrot Sketch, The Spanish Inquisition, The Argument Clinic'
sketches = sketches.split(', ')

# print(f"\n2.0.1.2 Split sketches = {sketches}")

# 2.0.2 str.splitlines()

excerpt = """Nobody expects the Spanish Inquisition.
Our chief weapon is surprise.
Surprise and fear. Fear and surprise.
Our two weapons are fear and surprise ...
and ruthless efficieny.
Our three weapons are fear and surprise and ruthless efficiency ...
and an almost fanatical devotion to the pope.
Uh! Four. No.
Amongst our weapons ....
Amongst our weaponry are such elements as fear, su -- I'll come in again.
"""

lines = excerpt.splitlines()

print(f"\n2.0.2.1 Excerpt splitlines = {lines}")


## 2.1 CHALLENGE 01

arthur = 'The Lady of the Lake, '\
    'her arm clad in the purest shimmering samite, '\
    'held aloft Excalibur from the bosom of the water '\
    'signifying by Divine Providence that '\
    'I, Arthur, was to carry Excalibur. '\
    'That is why I am your king.'

dennis = (
    'Listen, strange women lying in ponds distributing swords '
    'is no basis for a system of government. '
    'Supreme executive power derives from a mandate from the masses, '
    'not from some farcical aquatic ceremony.'
    )

# TODO Join strings and split into list of sentences

# print(f"\n2.1 Arthur and Dennis = {excalibur}")


# 3.0 INDEXING

# 3.1 Accessing a character by position

name = 'Monty Python'
letter = None # TODO index # first letter (zero-based index)

# print(f"\n3.1.1 Letter = {letter}")

letter = None # TODO

# print(f"\n3.1.2 Letter = {letter}")

letter = None # TODO

# print(f"\n3.1.3 Letter = {letter}")


# 3.2 Index operator (list)

menu = [
    'Egg and bacon',
    'Egg, sausage and bacon',
    'Egg and Spam',
    'Egg, bacon and Spam',
    'Egg, bacon, sausage and Spam',
    'Spam, bacon, sausage and Spam',
    'Spam, egg, Spam, Spam, bacon and Spam',
    'Spam, Spam, Spam, egg and Spam',
    'Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam',
    'Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top and Spam'
    ]

menu_item = None # TODO access second element (zero-based index)

# print(f"\n3.2.1 Menu item = {menu_item}")

menu_item = None # TODO access second to last element

# print(f"\n3.2.2 Menu item = {menu_item}")


# 3.3 Trigger an IndexError exception
# menu_item = menu[10] # IndexError: list index out of range#


# 3.4 CHALLENGE 02

order = None # TODO access menu item

# print(f"\n3.4 Menu order = {order}")


# 4.0 SLICING

cast = [
    'Terry Jones, Waitress',
    'Eric Idle, Mr Bun',
    'Graham Chapman, Mrs Bun',
    'John Cleese, The Hungarian',
    'Michael Palin, Historian',
    'Extra, Viking 01',
    'Extra, Viking 02',
    'Extra, Viking 03',
    'Extra, Viking 04',
    'Extra, Viking 05',
    'Extra, Viking 06',
    'Extra, Police Constable'
]

# 4.1 slice from index 0 to index n (stride = 1)

# Return Mr and Mrs Bun
cast_members = None # TODO slice

# print(f"\n4.1.1 The Buns = {cast_members}")

# Return Mr and Mrs Bun (negative slice)
named_cast_members = None # TODO slice

# print(f"\n4.1.2 The Buns (negative slice) = {named_cast_members}")

# Slice from index 0 to index n (stride = 1)
named_cast_members = None # TODO slice

# print(f"\n4.1.3 Named cast members = {named_cast_members}")

# Slice from index -n to end of list inclusive (stride = 1)
unnamed_cast_members = None # TODO slice

# print(f"\n4.1.4 Extras = {unnamed_cast_members}")


# 4.2 CHALLENGE 03

cleese_palin = None # TODO slice

# print(f"\n4.2 Cleese and Palin = {cleese_palin}")


# 4.3 CHALLENGE 03

vikings = None # TODO slice

# print(f"\n4.3 Vikings = {vikings}")
