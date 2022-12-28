from pprint import pprint # import statement

# SI 506 Lecture 06

# 1.0 SLICING STRIDE VALUES

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

# 1.1.1 Retrieve Named cast members
cast_members = cast[:5:1] # equivalent to cast[:5], cast[0:5] or cast[0:5:1]

print('\n1.1.1 Named cast members\n')
pprint(cast_members) # Pretty print


# 1.1.2 Retrieve the late Terry Jones and Graham Chapman
cast_members = cast[:3:2]

print('\n1.1.2 Deceased cast members\n')
pprint(cast_members) # Pretty print


# 1.1.3 Return cast members in reverse order
cast_members = cast[::-1]

print('\n1.1.3 Cast members reverse order\n')
pprint(cast_members) # Pretty print


# 1.1.4 Return every other cast member starting from the first element
cast_members = cast[::2]

print('\n1.1.4 Every other cast member\n')
pprint(cast_members) # Pretty print

# 1.1.5 Return every other cast member starting from the last element (negative stride)
cast_members = cast[::-2] # reverse

print('\n1.1.5 Every other cast member (negative stride)\n')
pprint(cast_members) # Pretty print

# 1.1.6 Return every other Viking starting with Viking 01.
cast_members = cast[5:11:2]

print('\n1.1.6 Every other Viking\n')
pprint(cast_members) # Pretty print

# BONUS. Return every other Viking starting with Viking 01 in reverse order.
cast_members = cast[5:11:-2] # Fails: empty list returned

print('\n1.1.6.1 Every other Viking reverse order \n')
pprint(cast_members) # Pretty print

# Workaround
cast_members = cast[5:11]
cast_members = cast_members[::-2]

print('\n1.1.6.2 Every other Viking reverse order workaround\n')
pprint(cast_members) # Pretty print


# 1.2 Slice Assignment

cast[4] = 'Michael Palin, The Historian' # Adds the definite article "The"

mounties = [
    'Extra, Canadian Mountie 01',
    'Extra, Canadian Mountie 02',
    'Extra, Canadian Mountie 03',
    'Extra, Canadian Mountie 04',
    'Extra, Canadian Mountie 05',
    'Extra, Canadian Mountie 06'
]

# 1.2.1 Replace part of a list (length unchanged)
cast[5:11] = mounties[0:] # replace Vikings with Mounties

print('\n1.2.1 Replace Vikings with Canadian Mounties\n')
pprint(cast) # Pretty print

# 1.2.2 Replace part of a list (length changes)
cast[5:11] = mounties[1:5] # replace Vikings with mounties 02-04 (negative slice)

print('\n1.2.2 Replace Vikings with mounties 02-04\n')
pprint(cast) # Pretty print


# 1.3 Built-in del() function and slicing

# Delete a slice with built-in del() function

# Delete the Mounties (retain the Police Constable)
del(cast[-5:-1])
# del(cast[5:9])

print('\n1.3 Delete Mounties\n')
pprint(cast) # Pretty print


# 1.4 Built-in slice() function

# slice([start, ]end[, step]) object
s = slice(1, 4, 2) # Returns Idle and Cleese
cast_members = cast[s]

print('\n1.4 slice() example\n')
pprint(cast_members) # Pretty print


## 2.0 STR AND LIST METHODS

menu_item = 'Spam, egg, Spam, Spam, bacon and Spam'

# str.lower() -- no argument method
menu_item_lower = menu_item.lower()

print(f"\n2.0.1 lower case = {menu_item_lower}")

# str.count(value, start=0, end=len(str) - 1) -- start and end are optional
spam_count = menu_item.count('Spam')

print(f"\n2.0.2 Spam count = {spam_count}")

# str.split(sep=' ', maxsplit=-1) -- sep and maxsplit are optional
items = menu_item.split(', ') # returns list

print('\n2.0.3\n')
pprint(items) # Pretty print

# list.remove(element) -- in place operation; removes 1st occurence; returns None
items.remove('egg')

print('\n2.0.4\n')
pprint(items) # Pretty print

# Do not do this: items variable no longer points to a list object
items = items.remove('bacon and Spam') # None is returned

print('\n2.0.5\n')
pprint(items) # Pretty print


# 2.1 Chained method calls
menu_item = 'Egg, bacon, sausage and Spam'

# Good. Replace, convert to lower case, and split.
items = menu_item.replace(' and', ',').lower().split(', ')

print('\n2.1.1 Menu reformatted\n')
pprint(items) # Pretty print

# Bad. The trailing list.append() returns None (oops!)
items = menu_item.replace(' and', ',').lower().split(', ').append('pancakes')

print('\n2.1.2 Bad chaining order\n')
pprint(items) # Pretty print

# Ugly. Premature split. Calling lower on a list object raises a runtime error
# AttributeError: 'list' object has no attribute 'lower'

# TODO UNCOMMENT (WARN: RAISES EXCEPTION)
# items = menu_item.replace(' and', ',').split(', ').lower()

# print('\n2.1.3\n')
# pprint(items) # Pretty print


# 2.2 SELECT STR METHODS

# 2.2.1 str.strip()
monty_python = " Monty Python's Flying Circus \n" # note apostrophe

print(f"\n2.2.1.1 Monty Python (unstripped) = {monty_python}")

monty_python = monty_python.strip() # note reassignment

print(f"\n2.2.1.2 Monty Python (stripped) = {monty_python}")

# 2.2.2 str.find()
menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.find('Spam')

print(f"\n2.2.2.1 Index position = {position}")

menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.find('ham')

print(f"\n2.2.2.2 Index position = {position}")

# 2.2.3 str.index()
menu_item = 'Spam, Spam, Spam, egg and Spam'
position = menu_item.index('egg and Spam')

print(f"\n2.2.3.1 Index position = {position}")

# TODO UNCOMMENT (WARN: RAISES RUNTIME EXCEPTION)
# position = menu_item.index('ham')

# print(f"\n2.2.3.2 Index position = {position}")

# 2.2.4 str.join()
items = ['Oatmeal', 'Fruit', 'Spam'] # a list
menu_item = ''.join(items) # join to blank or empty string (not so good in this case)

print(f"\n2.2.4.1 Menu item = {menu_item}")

menu_item = ', '.join(items) # better

print(f"\n2.2.4.2 Menu item = {menu_item}")


# 2.2.5 CHALLENGE 07

menu = """Egg and bacon
Egg, sausage and bacon
Egg and Spam
Egg, bacon and Spam
Egg, bacon, sausage and Spam
Spam, bacon, sausage and Spam
Spam, egg, Spam, Spam, bacon and Spam
Spam, Spam, Spam, egg and Spam
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam
Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top and Spam
"""

healthy_choice = 'Oatmeal'

# Multiline expression expressed across multiple lines
menu_v2 = (menu
    .replace('sausage', 'toast')
    .replace('Spam, Spam, Spam', f"Spam, Spam, {healthy_choice}")
    .lower()
    .splitlines()
    )

# Alternative
# menu_v2 = menu.replace('sausage', 'toast') \
#     .replace('Spam, Spam, Spam', 'Spam, Spam, ' + healthy_choice) \
#     .lower() \
#     .splitlines()

print('\n2.2.5 menu_v2')
pprint(menu_v2, width=125) # Pretty print


# 3.0 LIST METHODS

# 3.0.1 list.append() (in-place)
menu_v2.append('red beans and rice') # modify in-place (no variable assignment)

print('\n3.0.1 New menu item\n')
pprint(menu_v2, width=125) # Pretty print

# 3.0.2 list.remove() (in-place)
item = menu_v2[-2] # Lobster Thermidor
menu_v2.remove(item)

print('\n3.0.2 Lobster Thermidor removed\n')
pprint(menu_v2, width=125) # Pretty print

# 3.0.3 list.extend() (in-place)
healthy_items = ['cereal, yogurt, and spam', 'oatmeal, fruit plate, and spam']
menu_v2.extend(healthy_items)

print('\n3.0.3 new menu extended\n')
pprint(menu_v2, width=125) # Pretty print

# 3.0.4 list.index()
index = menu_v2.index('egg, bacon and spam')

print(f"\n3.0.4 Index postion = {index}")

# 3.0.5 list.insert() (in-place)
menu_v2.insert(1, 'belgian waffle, strawberries, and spam')

print('\n3.0.5 Belgian waffle added to the menu\n')
pprint(menu_v2, width=125) # Pretty print

# 3.0.6 list.sort() (in-place)
menu_v2.sort() # default alpha sort

print('\n3.0.6 New menu sorted\n')
pprint(menu_v2, width=125) # Pretty print


# 3.1 CHALLENGE 08

menu_v3 = menu_v2[::-1]

print(f"\n3.1.1 Menu_v2 (id={id(menu_v2)}, len={len(menu_v3)})\n")
pprint(menu_v2, width=125)

print(f"\n3.1.2 Menu_v3 (id={id(menu_v3)}, len={len(menu_v3)})\n")
pprint(menu_v3, width=125)

# Eliminate 'egg and spam' menu item

menu_v3.remove('egg and spam')

print(f"\n3.1.3 Menu_v3 (id={id(menu_v3)}, len={len(menu_v3)})\n")
pprint(menu_v3, width=125)

menu_v3.insert(5, 'blueberry pancakes')

print(f"\n3.1.4 Menu_v3 (id={id(menu_v3)}, len={len(menu_v3)})\n")
pprint(menu_v3, width=125)


# 3.2 CHALLENGE 09

# Retrieve
idx = menu_v3.index('egg, toast and bacon')

print(f"\n3.2.1 Index value = {idx}")

# Calculate length
length = len(menu_v3)

print(f"\n3.2.2 menu_v3 len = {length}")

# Egg first dishes
# WARN: indexes are zero-based.
egg_first_dishes = menu_v3[idx:length - 2]

print('\n3.2.3 Egg first dishes\n')
pprint(egg_first_dishes)


# 4.0 STRING FORMATTING

# Formatted string literal (f-string)
special_item = 'egg, bacon, spam and sausage'
question = f"Why can't she have {special_item}?"

print(f"\n4.1 f-string = {question}") # embedded variable

# str.format()s
question = "Could I have {}, {}, {} and {}, without the spam?".format('egg', 'bacon', 'spam', 'sausage')

print(f"\n4.2 str.format() = {question}")

# 7.3 C-style or simple provisional formatting
question = "No, it wouldn't be %s, %s, %s and %s, would it?" % ('egg', 'bacon', 'spam', 'sausage')

print(f"\n4.3.1 C-style = {question}")

string = "%s %i %c" % ('Spam Sketch (', 1970, ')')

print(f"\n4.3.2 C-style = {string}")
