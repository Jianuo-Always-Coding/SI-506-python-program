# SI 506 Lecture 07

from pprint import pprint # import statement


# 1.1 NESTED LISTS

# EV attributes: automaker, model, model year, range (miles)
elec_vehicles = [
    'Ford, Mustang Mach-E AWD, 2021, 211',
    'Kandi, K27, 2021, 59',
    'Chevrolet (GM), Bolt EV, 2021, 259',
    'Audi (Volkswagen), e-tron, 2021, 222',
    'Nissan, Leaf (40 kW-hr battery pack), 2021, 149',
    'Tesla, Model 3 Performance AWD, 2021, 315',
    'Volvo, XC40 AWD BEV, 2021, 208',
    'Volkswagen, ID.4 1st, 2021, 250',
    'BMW, i3s, 2021, 153',
    'MINI (BMW), Cooper SE Hardtop 2 door, 2021, 110',
    'Tesla, Model S Performance (19in Wheels), 2021, 387'
    ]

model = None # TODO Get Mustang Mach-E AWD

# print(f"\n1.1.1 Model = {model}")

elec_vehicles = [
    ['Ford', 'Mustang Mach-E AWD', '2021', '211'],
    ['Kandi', 'K27', '2021', '59'],
    ['Chevrolet (GM)', 'Bolt EV', '2021', '259'],
    ['Audi (Volkswagen)', 'e-tron', '2021', '222'],
    ['Nissan', 'Leaf (40 kW-hr battery pack)', '2021', '149'],
    ['Tesla', 'Model 3 Performance AWD', '2021', '315'],
    ['Volvo', 'XC40 AWD BEV', '2021', '208'],
    ['Volkswagen', 'ID.4 1st', '2021', '250'],
    ['BMW', 'i3s', '2021', '153'],
    ['MINI (BMW)', 'Cooper SE Hardtop 2 door', '2021', '110'],
    ['Tesla', 'Model S Performance (19in Wheels)', '2021', '387']
    ]

model = None # TODO Get Mustang Mach-E AWD

# print(f"\n1.1.2 Model = {model}")

# 1.2 FOR LOOP

# print('\n1.2.1 Print elements')

# TODO Implement for loop

# print('\n1.2.2 Print elements')

# TODO Implement for loop (slice)


# 1.3 IF STATEMENT

# print('\n1.3.1 Find Volvo and print')
# for vehicle in elec_vehicles:
    # TODO Implement if statement
        # print(vehicle)

# print('\n1.3.2 Get Volkswagens and print')
# for vehicle in elec_vehicles:
    # TODO Implement if statement
        # print(vehicle)

# print('\n1.3.3 Get non Volkswagens and print')
# for vehicle in elec_vehicles:
    # TODO Implement if statement
        # print(vehicle)


# 1.4 CHALLENGE 01

# print('\n1.4.1 Ch 01 Tesla EVs (membership in)')

# TODO Implement loop


# 2.0 ACCUMULATOR PATTERN

elec_vehicles = [
    ['Ford', 'Mustang Mach-E AWD', '2021', '211'],
    ['Kandi', 'K27', '2021', '59'],
    ['Chevrolet (GM)', 'Bolt EV', '2021', '259'],
    ['Audi (Volkswagen)', 'e-tron', '2021', '222'],
    ['Nissan', 'Leaf (40 kW-hr battery pack)', '2021', '149'],
    ['Tesla', 'Model 3 Performance AWD', '2021', '315'],
    ['Volvo', 'XC40 AWD BEV', '2021', '208'],
    ['Volkswagen', 'ID.4 1st', '2021', '250'],
    ['BMW', 'i3s', '2021', '153'],
    ['MINI (BMW)', 'Cooper SE Hardtop 2 door', '2021', '110'],
    ['Tesla', 'Model S Performance (19in Wheels)', '2021', '387']
    ]

teslas = []
# for vehicle in elec_vehicles:
#     if vehicle[0].lower().find('tesla') > -1:
#         teslas.append(vehicle)

# print('\n2.0 Teslas')
# pprint(teslas)

# TODO Uncomment

# 2.0.1 Max range (does not handle ties)
# vehicle_max_range = None
# max_range = 0
# for vehicle in elec_vehicles:
#     vehicle_range = int(vehicle[-1]) # cast str to int
#     if vehicle_range > max_range:
#         max_range = vehicle_range
#         vehicle_max_range = f"{vehicle[0]} {vehicle[1]}" # automaker model

# print(f"\n2.0.1 Max range ({max_range} mpg) = {vehicle_max_range}")


# 2.1 ACCUMULATING COUNTS

# TODO Uncomment

# bmw_count = 0
# for vehicle in elec_vehicles:
    # TODO implement if statement
       # TODO Accumulate count # assignment addition equivalent to bmw_count = bmw_count + 1

# print(f"\n2.1 BMW count = {bmw_count}")


# 2.2 CHALLENGE 02

# Implement challenge

# print(f"\n2.2 Ch 02 mpg > 250 mi = {vehicle_count}")


# 3.0 LOOPING WITH RANGE()

# 3.1 range() behaviors

# seq = range(10)

# print(f"\n3.1.1 seq (type={type(seq)}) = {seq}") # <class 'range'>

# seq = list(range(10)) # convert range object to a list

# print(f"\n3.1.2 range seq = {seq}")

# seq = list(range(5, 10))

# print(f"\n3.1.3 range seq start/stop = {seq}")

# seq = list(range(5, 21, 5))

# print(f"\n3.1.4 range seq start/stop/step = {seq}")

# seq = list(range(20, 4, -5))

# print(f"\n3.1.5 range seq start/stop/step reversed = {seq}")

# print(f"\n3.1.6 for loop with range()\n")
# for i in range(5):
#     print("I want an EV!")


# 3.2 The `for` loop and `range`

automakers = [
    'Bayerische Motoren Werke AG',
    'Ford Motor Co.',
    'General Motors Co.',
    'Kandi Technologies Group',
    'Nissan Motor Co.',
    'Volkswagen AG',
    'Volvo Group',
    'Tesla, Inc.'
    ]

# print(f"\n3.2 access automakers with range()\n")

# TODO implement for i in range()

# TODO Uncomment
# Replace immutable string value (fail)

# for automaker in automakers:
#     automaker = automaker.upper() # assigns new string to loop variable only

# print('\n3.3.1 automaker to uppercase (fail)')
# pprint(automakers)

# Replace immutable element value (success)
# for i in range(len(automakers)):
#     automakers[i] = automakers[i].upper() # assigns new string to element

# print('\n3.3.2 automaker to uppercase')
# pprint(automakers)

# Modify every third element commencing from index 0
# for i in range(0, len(automakers), 3):
#     automakers[i] = automakers[i].lower() # assigns new string elements at positions 0, 3, 6

# print(f"\n3.3.3 to lowercase (sequence = {list(range(0, len(automakers), 3))})")
# pprint(automakers)


# 3.4 Subscript notation chaining

tesla_s_range = None # TODO chain subscript operators

# print(f"\n3.4.1 Tesla Model S range (mpg) = {tesla_s_range}")

# tesla_s_range = 0
# for i in range(len(elec_vehicles)):
#     if elec_vehicles[i][1] == 'Model S Performance (19in Wheels)':
#         tesla_s_range = elec_vehicles[i][-1]

# print(f"\n3.4.2 Tesla Model S range (mpg) = {tesla_s_range}")


# 3.5 CHALLENGE 03

elec_vehicles = [
    ['Ford', 'Mustang Mach-E AWD', '2021', '211'],
    ['Kandi', 'K27', '2021', '59'],
    ['Chevrolet (GM)', 'Bolt EV', '2021', '259'],
    ['Audi (Volkswagen)', 'e-tron', '2021', '222'],
    ['Nissan', 'Leaf (40 kW-hr battery pack)', '2021', '149'],
    ['Tesla', 'Model 3 Performance AWD', '2021', '315'],
    ['Volvo', 'XC40 AWD BEV', '2021', '208'],
    ['Volkswagen', 'ID.4 1st', '2021', '250'],
    ['BMW', 'i3s', '2021', '153'],
    ['MINI (BMW)', 'Cooper SE Hardtop 2 door', '2021', '110'],
    ['Tesla', 'Model S Performance (19in Wheels)', '2021', '387']
    ]

# TODO Implement loop

# print('\n3.5 Ch 03 Automaker + Model name')
# pprint(elec_vehicles)
