# SI 506 Lecture 08

from pprint import pprint

elec_vehicles = [
    ['powertrain', 'make', 'model', 'type', 'propulsion', 'drivetrain', 'city/combined/highway_mpge', 'range'],
    ['BEV', 'Audi', 'e-tron GT', 'Sedan/Wagon', '175 kW electric motor; 129 Ah battery', 'AWD', '81/82/83', '238'],
    ['BEV', 'Audi', 'Q4 e-tron Sportback quattro', 'SUV', '80 kW and 150 kW electric motors; 234 Ah battery', 'AWD', '100/95/89', '241'],
    ['BEV', 'BMW', 'i4 eDrive40 Gran Coupe (18" Wheels)', 'Sedan/Wagon', '250 kW electric motor; 211 Ah battery', 'RWD', '109/109/108', '301'],
    ['BEV', 'BMW', 'iX xDrive50 (20" Wheels)', 'SUV', '190 and 230 kW electric motors; 303 Ah battery', 'AWD', '86/86/87', '324'],
    ['BEV', 'Chevrolet', 'Bolt EV', 'Sedan/Wagon', '150 kW electric motor; 189 Ah battery', 'FWD', '131/120/109', '259'],
    ['BEV', 'Ford', 'F150 Lightning 4WD Extended Range', 'Pickup', '210 kW electric motors (X2); 410 Ah battery', 'AWD', '78/70/63', '320'],
    ['BEV', 'Ford', 'Mustang Mach-E AWD California Route 1', 'SUV', '258 kW electric motors (x2); 288 Ah battery', 'AWD', '105/98/91', '312'],
    ['BEV', 'Hyundai', 'Ioniq 5 RWD (Long Range)', 'SUV', '168 kW electric motor; 111 Ah battery', 'RWD', '132/114/98', '303'],
    ['BEV', 'Kia', 'EV6 AWD (Long Range)', 'Sedan/Wagon', '74 kW and 165 kW electric motors; 111 Ah battery', 'AWD', '116/105/94', '274'],
    ['BEV', 'Kia', 'EV6 RWD (Long Range)', 'Sedan/Wagon', '168 kW electric motor; 111 Ah battery', 'RWD', '134/117/101', '310'],
    ['BEV', 'Lucid USA, Inc.', 'Air Dream P AWD w/19" wheels', 'Sedan/Wagon', '370kW and 459kW electrics motors; 150Ah battery', 'AWD', '117/116/114', '471'],
    ['BEV', 'Lucid USA, Inc.', 'Air Dream R AWD w/19" wheels', 'Sedan/Wagon', '198kW and 498kW electrics motors; 150Ah battery', 'AWD', '126/125/125', '520'],
    ['BEV', 'Mazda', 'MX-30', 'Sedan/Wagon', '81 kW electric motor; 100 Ah battery', 'FWD', '98/92/85', '100'],
    ['BEV', 'Mercedes-Benz', 'EQS450+', 'Sedan/Wagon', '245 kW electric motor; 282 Ah battery', 'RWD', '97/97/97', '350'],
    ['BEV', 'Mini', 'Cooper SE Hardtop 2 door', 'Sedan/Wagon', '135 kW electric motor; 93 Ah battery', 'FWD', '119/110/100', '114'],
    ['BEV', 'Nissan', 'Leaf (62 kWh battery pack)', 'Sedan/Wagon', '160 kW electric motor; 176 Ah battery', 'FWD', '118/108/97', '226'],
    ['BEV', 'Polestar Automotive USA', 'Polestar 2 (Single Motor)', 'Sedan/Wagon', '170kW electric motor; 196 Ah battery', 'FWD', '113/107/100', '270'],
    ['BEV', 'Porsche', 'Taycan 4 Cross Turismo', 'Sedan/Wagon', '175 and 320 kW electric motors; 129 Ah battery', 'AWD', '76/76/77', '215'],
    ['BEV', 'Rivian', 'R1S', 'SUV', '162, 162, 163, 163kW electric independent electric motors; 360Ah battery', 'Part-Time 4WD', '73/69/65', '316'],
    ['BEV', 'Rivian', 'R1T', 'Pickup', '162, 162, 163, 163kW electric independent electric motors; 360Ah battery', 'Part-Time 4WD', '74/70/66', '314'],
    ['BEV', 'Tesla', 'Model 3 (Long Range) AWD', 'Sedan/Wagon', '98 kW and 195 kW electric motors; 235 Ah battery', 'AWD', '134/131/126', '353'],
    ['BEV', 'Tesla', 'Model S', 'Sedan/Wagon', '247 kW dual electric motors; 256 Ah battery', 'AWD', '124/120/115', '405'],
    ['BEV', 'Volkswagen', 'ID.4 Pro', 'SUV', '150 kW electric motor; 234 Ah battery', 'RWD', '116/107/98', '275'],
    ['BEV', 'Volvo', 'C40 Recharge Twin', 'SUV', '150 kW electric motors (X2); 196 Ah battery', 'AWD', '94/87/80', '226']
]

print(f"\n1.0 elec_vehicles length = {len(elec_vehicles)}")


# 1.1 CHALLENGE 01

ev_types = []
for vehicle in elec_vehicles[1:]:
    if vehicle[3] not in ev_types:
        ev_types.append(vehicle[3])

print(f"\n1.1 EV types = {ev_types}")


# 1.2 CHALLENGE 02

for i in range(1, len(elec_vehicles)):
    if elec_vehicles[i][1] == 'Ford':
        elec_vehicles[i][1] = 'Ford Moter Company'

# Alternative
# for vehicle in elec_vehicles[1:]:
#     if vehicle[1] == 'Ford':
#         vehicle[1] = 'Ford Moter Company'

print('\n1.2 Rename Ford')
pprint(elec_vehicles[6:8])

# But Beware
us_automakers = [
    'Chevrolet',
    'Ford',
    'Lucid USA, Inc.',
    'Polestar Automotive USA',
    'Rivian'
    ]

for automaker in us_automakers:
    if automaker == 'Ford':
        automaker = 'Ford Moter Company'

print('\n1.2 Rename Ford (FAIL)')
pprint(us_automakers)


# 2.0 IF-ELSE

sedan_wagon = []
suv_pickup = []
for vehicle in elec_vehicles[1:]:
    string = f"{vehicle[1]} {vehicle[2]} {vehicle[3]}"
    if vehicle[3] == ev_types[0]:
        sedan_wagon.append(string)
    else:
        suv_pickup.append(string)

print(f"\n2.0.1 Sedan/Wagon (n={len(sedan_wagon)})")
pprint(sedan_wagon)

print(f"\n2.0.1 SUV/Pickup (n={len(suv_pickup)})")
pprint(suv_pickup)

standard_ranges = []
outlier_ranges = []
for vehicle in elec_vehicles[1:]:
    string = f"{vehicle[1]} {vehicle[2]} (range = {vehicle[-1]})"
    if 225 < int(vehicle[-1]) < 325:
        standard_ranges.append(string)
    else:
        outlier_ranges.append(string)

print(f"\n2.0.2 Standard ranges (n={len(standard_ranges)})")
pprint(standard_ranges)

print(f"\n2.0.2 Outlier ranges (n={len(outlier_ranges)})")
pprint(outlier_ranges)


# Challenge 03
us_automakers = [
    'Chevrolet',
    'Ford',
    'Lucid USA, Inc.',
    'Polestar Automotive USA',
    'Rivian'
    ]
domestic_count = 0
foreign_count = 0

for vehicle in elec_vehicles[1:]:
    if vehicle[1] in us_automakers:
        domestic_count += 1
    else:
        foreign_count += 1

print(f"\n2.0.2 Domestic-designed EV count = {domestic_count}")
print(f"\n2.0.2 Foreign-designed EV count = {foreign_count}")


# 3.1 CHALLENGE 04

awd_vehicles = []
for vehicle in elec_vehicles[1:]:
    if vehicle[5] == 'AWD':
        awd_vehicles.append(f"{vehicle[1]} {vehicle[2]}")

print(f"\n3.1 AWD EVs (n={len(awd_vehicles)})")
pprint(awd_vehicles)

# Alternative: lookup index with header value
headers = elec_vehicles[0] # Extract header row

print(f"\n3.1 Headers (n={len(headers)})")
pprint(headers)

awd_vehicles = []
for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('drivetrain')] == 'AWD':
        awd_vehicles.append(f"{vehicle[1]} {vehicle[2]}")

print(f"\n3.1 headers.index() lookup (n={len(awd_vehicles)})")
pprint(awd_vehicles)


# 3.2 CHALLENGE 05

ev_range = [None, 10000]
# ev_range = [None, float('inf')] # infinity
for vehicle in elec_vehicles[1:]:
    vehicle_range = int(vehicle[-1])
    if vehicle_range < ev_range[-1]:
        ev_range[0] = f"{vehicle[1]} {vehicle[2]}"
        ev_range[1] = vehicle_range

print(f"\n3.2.1 Shortest range mpge = {ev_range}")

# Example: longest range
ev_range = [None, 0]
for vehicle in elec_vehicles[1:]:
    vehicle_range = int(vehicle[-1])
    if vehicle_range > ev_range[-1]:
        ev_range[0] = f"{vehicle[1]} {vehicle[2]}"
        ev_range[1] = vehicle_range

print(f"\n3.2.2 Longest range mpge = {ev_range}")


# 3.3 CHALLENGE 06

# Accumulate combined mpge values
combined_mpge_vals = []
for vehicle in elec_vehicles[1:]:
    combined_mpge = int(vehicle[-2].split('/')[1]) # cast to int
    # combined_mpge = int(vehicle[headers.index('city/combined/highway_mpge')].split('/')[1])
    combined_mpge_vals.append(combined_mpge)

print(f"\n3.3 Combined mpge values = {combined_mpge_vals}")

# Compute mean (average) combined (city/highway) mpge to two decimal points
combined_mpge_mean = round(sum(combined_mpge_vals) / len(combined_mpge_vals), 2)

print(f"\n3.3 Combined mpge mean = {combined_mpge_mean}")
