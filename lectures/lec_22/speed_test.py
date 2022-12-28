import timeit

"""
https://docs.python.org/3/library/timeit.html

timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)

stmt: code to be timed
setup: setup details that must be executed before stmt is processed
timer: timer value, default value set, ignore it.
number: execute stmt n times (default = 1 million).
globals: specify a namespace in which to execute the code.

garbage collection turned off temporarily during the timing.
"""

# Setup: retrieve data
setup = """
import json
with open('./wb-groups-2021_2022.json', 'r', encoding='utf-8') as file_obj:
    groups = json.load(file_obj)

with open('./wb-economies-2021_2022.json', 'r', encoding='utf-8') as file_obj:
    countries = json.load(file_obj)"""

# Time for loop
for_loop = """
umc = []
for group in groups:
    for country in countries:
        if (group['group_code'] == 'UMC'
            and country['country_code'] == group['country_code']
            and country['region'] == 'Europe & Central Asia'):
            umc.append(country)"""

for_loop_time = timeit.timeit(stmt=for_loop, setup=setup, number=500)

print(f"\nFor loop execution time = {for_loop_time}")

# Time list comprehension
list_comp = """
umc = [
    country
    for group in groups
    for country in countries
    if group['group_code'] == 'UMC'
    and country['country_code'] == group['country_code']
    and country['region'] == 'Europe & Central Asia'
]"""

list_comp_time = timeit.timeit(stmt=list_comp, setup=setup, number=500)

print(f"\nlist comprehension execution time = {list_comp_time}")