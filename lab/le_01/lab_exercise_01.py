# START LAB EXERCISE 01
print('Lab Exercise 01 \n')

# PROBLEM 1 (1 point)
north_quad = "North Quad"
# ccrb = Central Campus Recreation Building
# @kelseymuseum = "Kelsey Museum of Archaeology"
mason_hall = "Mason Hall"
palmer = "Palmer Commons"
modern_lang = "Modern Languages Building"
kinesiology = "School of Kinesiology Building"
education = "School of Education Building"
# north_univ = "North University Ave. Building'
cccb = "Central Campus Classroom Building"
hatcher = "Harlan Hatcher Graduate Library"
shapiro = "Shapiro Undergraduate Library"

locations = [north_quad,mason_hall,palmer,modern_lang,kinesiology,education,cccb,hatcher,shapiro]




# PROBLEM 2 (1 point)
num_locations = len(locations)


# PROBLEM 3 (1 point)
north_quad_study_areas = 30
mason_hall_study_areas = 22
palmer_study_areas = 8
modern_lang_study_areas = 4
kinesiology_study_areas = 12
education_study_areas = 11
cccb_study_areas  = 4
hatcher_study_areas = 9
shapiro_study_areas = 4

total_study_areas = north_quad_study_areas + mason_hall_study_areas + \
    palmer_study_areas + modern_lang_study_areas + kinesiology_study_areas + \
        education_study_areas + cccb_study_areas + hatcher_study_areas + \
            shapiro_study_areas


# PROBLEM 4 (1 point)
avg_study_areas = total_study_areas // num_locations


# PROBLEM 5 (2 points)
study_areas = '''
North Quad; 30, Mason Hall; 22, Palmer Commons; 8,
Modern Languages Building; 4, School of Kinesiology Building; 12,
School of Education Building; 11, Central Campus Classroom Building; 4,
Harlan Hatcher Graduate Library; 9, Shapiro Undergraduate Library; 4
'''

fixed_locations = study_areas.replace(";",":")


# PROBLEM 6 (2 points)

count_building = fixed_locations.count("Building")
count_library = fixed_locations.count("Library")


# PROBLEM 7 (1 point)

statement = f"There are {count_building} locations with 'Building' in their name and {count_library} locations with 'Library' in their name."

# PROBLEM 8 (1 point)

hail = '''
Hail! to the victors valiant
Hail! to the conqu'ring heroes
Hail! Hail! to Michigan
the leaders and best
Hail! to the victors valiant
Hail! to the conqu'ring heroes
Hail! Hail! to Michigan,
the champions of the West!
'''

hail_lower = hail.lower()
hail_upper = hail.upper()


# END LAB EXERCISE
test = None
if not test:
    print('I am None')

