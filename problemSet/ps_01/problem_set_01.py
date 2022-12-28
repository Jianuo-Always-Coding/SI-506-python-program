# START PROBLEM SET 1
print('Problem Set 1 \n')

# PROBLEM 01 (10 points)
print('\nPROBLEM 01')

# 1frita_batidos = 'Frita Batidos'
# zingerman's Delicatessen = "Zingerman's Delicatessen"
# nypd = New York Pizza Depot
hopcat = 'Hopcat'
fleetwood_diner = "Fleetwood Diner"
# tomukun_noodle_bar = 'Tomukun Noodle Bar
jerk_pit = "Jamaican Jerk Pit"
# mama satto = 'Mama Satto'
# hola_seoul = 'Hola Seoul"
# @shalimar = 'Shalimar'

cottage_inn = "Cottage Inn Pizza"
print(cottage_inn)

madras_masala = "Madras Masala"
print(madras_masala)

# PROBLEM 02 (30 points)
print('\nPROBLEM 02')

hopcat_all_upper = hopcat.upper()
print(f"all_upper: {hopcat_all_upper}")

jerk_pit_all_lower = jerk_pit.lower()
print(f"all_lower: {jerk_pit_all_lower}")

madras_masala_count_a = madras_masala.count("a")
print(f"number of letter a: {madras_masala_count_a}")

has_pizza = cottage_inn.endswith("Pizza") 
print(has_pizza)

has_madras = madras_masala.startswith("madras")
print(has_madras)

comment = 'Truly authentic Jamaican food & drinks'
updated_comment = comment.replace("&","and")
print(f"updated comment: {updated_comment}")

# PROBLEM 03 (30 points)
print('\nPROBLEM 03')

num_chars = len(updated_comment)
print(f"number of characters: {num_chars}")

restaurants = ['Frita Batidos',
               "Zingerman's Delicatessen",
               'New York Pizza Depot',
               'Hopcat',
               'Fleetwood Diner',
               'Tomukun Noodle Bar',
               'Jamaican Jerk Pit',
               'Mama Satto',
               'Hola Seoul',
               'Shalimar',
               'Cottage Inn Pizza',
               'Madras Masala'
               ]

# TODO: print the type of the variable restaurants
print(type(restaurants))


num_restaurants = len(restaurants)
print(f"number of restaurants: {num_restaurants}")

total_price = 10 + 10 + 5.5 +12
print(f"total price: {total_price}")

total_bill = total_price * (1 + 0.2 + 0.06)
print(f"total bill: {total_bill}")

each_pay = total_bill / 4
print(f"each person pays: {each_pay}")

# PROBLEM 04 (5 points)
print('\nPROBLEM 04')

# TODO: Use f-string to print out the sentence
print("markdown")
print(f"Someone said '{updated_comment}' on Yelp for the restaurant {jerk_pit}.")
# END PROBLEM SET