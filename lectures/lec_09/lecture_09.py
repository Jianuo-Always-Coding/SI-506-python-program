# SI 506 Lecture 09

from email import header
from formatter import NullFormatter
from pprint import pprint

# 1.0 DATA

station_data = [
    ['id', 'station_name', 'facility_type', 'access_code', 'access_days_time', 'restricted_access', 'city', 'zip', 'street_address', 'intersection_directions', 'ev_network', 'ev_connector_types', 'ev_dc_fast_num', 'ev_level1_evse_num', 'ev_level2_evse_num', 'ev_other_evse', 'ev_pricing', 'date_last_confirmed'],
    ['41828', 'DTE Energy - Ann Arbor Ashley Mews Building', 'UTILITY', 'private', 'Employee and official visitor use only, 24 hours daily with employee security badge', None, 'Ann Arbor', '48104', '414 S Main St', 'Southeast corner of W Williams Street and S Ashley Street; in underground parking garage, entrance off of S Ashley Street; visitor parking spaces #1 and #2.', 'Non-Networked', 'J1772', None, None, '1', None, None, '2020-10-09'],
    ['42726', 'Ann Arbor Downtown Development Authority - Library Parking Structure', 'LIBRARY', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '319 S Fifth Ave', 'Sift between Liberty and William', 'Non-Networked', 'J1772', None, None, '9', None, 'Variable parking fee', '2021-07-14'],
    ['44282', 'Ann Arbor Downtown Development Authority - Ann Ashley Parking Structure', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '120 W Ann St', 'Ann and Ashley', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44283', 'Ann Arbor Downtown Development Authority - Catherine and Fourth Surface Lot', 'PARKING_LOT', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '121 Catherine St', 'Catherine and Fourth', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44284', 'Ann Arbor Downtown Development Authority - Forrest Parking Structure', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '650 Forrest St', 'Forrest and S University', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44285', 'Ann Arbor Downtown Development Authority - Maynard Parking Structure', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '316 Maynard St', 'Maynard between Liberty and William', 'Non-Networked', 'J1772', None, None, '4', None, 'Variable parking fee', '2021-07-14'],
    ['44286', 'Ann Arbor Downtown Development Authority - William Street Parking Structure', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '115 William St', 'William and Main', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44287', 'Ann Arbor Nissan', 'CAR_DEALER', 'public', 'Dealership business hours', 'False', 'Ann Arbor', '48103', '3975 Jackson Rd', None, 'Non-Networked', 'CHADEMO, J1772, J1772COMBO', '2', None, '1', None, 'Free', '2022-03-07'],
    ['44288', 'Ann Arbor Nissan', 'CAR_DEALER', 'private', None, None, 'Ann Arbor', '48103', '3975 Jackson Rd', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-03-07'],
    ['44773', 'IMRA America', 'OFFICE_BLDG', 'private', 'Employee and fleet use only', None, 'Ann Arbor', '48105', '1044 Woodridge Ave', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-06-14'],
    ['62417', 'U-M ANN ARBOR WALL STREET #2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '1041 Wall St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['63647', 'Varsity Ford', 'CAR_DEALER', 'private', None, None, 'Ann Arbor', '48103', '3480 Jackson Rd', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-06-14'],
    ['74325', 'Ann Arbor Downtown Development Authority - Ashley and Washington Parking Structure', 'PAY_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '215 W Washington', 'Washington and Ashley', 'Non-Networked', 'J1772', None, None, '3', None, 'Variable parking fee', '2022-05-05'],
    ['79282', 'First Martin', 'OFFICE_BLDG', 'private', 'Employee use only', None, 'Ann Arbor', '48104', '115 Depot St', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-09-14'],
    ['80037', 'MEADOWLARK BLDG STATION 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48103', '3250 W Liberty Rd', None, 'ChargePoint Network', 'J1772', None, None, '1', None, None, '2022-09-26'],
    ['99362', 'A & D Technology', 'OFFICE_BLDG', 'public', 'Open to public after company business hours', 'True', 'Ann Arbor', '48108', '4622 Runway Blvd', None, 'Non-Networked', 'J1772', None, None, '4', None, 'Free', '2020-12-03'],
    ['102221', 'Meijer - Tesla Supercharger', None, 'public', '24 hours daily; for Tesla use only', None, 'Ann Arbor', '48103', '3145 Ann Arbor-Saline Road', None, 'Tesla', 'TESLA', '8', None, None, None, '$0.28 per kWh; $0.26 per minute above 60 kW and $0.13 per minute at or below 60 kW', '2021-10-11'],
    ['114460', 'Sheraton Ann Arbor Hotel - Tesla Destination', 'HOTEL', 'public', '24 hours daily; for customer use only; see front desk for access', None, 'Ann Arbor', '48108', '3200 Boardwalk Dr', None, 'Tesla Destination', 'J1772, TESLA', None, None, '4', None, 'Free', '2020-11-03'],
    ['145371', 'Roundtree Place', None, 'public', '24 hours daily', None, 'Ypsilanti', '48197', '2539 Ellsworth Rd', None, 'Electrify America', 'CHADEMO, J1772COMBO', '6', None, None, None, None, '2022-09-07'],
    ['147501', 'MEIJER STORES 064 SALINE RD 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48108', '3145 Ann Arbor-Saline Rd', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['147555', 'U-M ANN ARBOR NCRC STATION 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '2800 Plymouth Rd', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['164341', '173 - Ann Arbor', None, 'public', '24 hours daily', None, 'Ann Arbor', '48103', '5645 Jackson Road', None, 'Greenlots', 'CHADEMO, J1772, J1772COMBO', '2', None, '4', None, None, '2022-09-26'],
    ['168052', 'The Ypsilanti Performance Space', 'OTHER_ENTERTAINMENT', 'public', '24 hours daily', 'False', 'Ypsilanti', '48197', '218 N Adams St', None, 'Non-Networked', 'J1772', None, None, '1', None, '$1 per hour; $5 per day', '2022-08-10'],
    ['168663', 'Car & Driver - Tesla Destination', None, 'public', '24 hours daily; for customer use only; see front desk for access', None, 'Ann Arbor', '48108', '1585 Eisenhower Place', None, 'Tesla Destination', 'TESLA', None, None, '2', None, 'Free', '2020-11-03'],
    ['171786', 'U-M ANN ARBOR WALL STREET #1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '1041 Wall St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['172462', 'MEADOWLARK BLDG STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48103', '3250 W Liberty Rd', None, 'ChargePoint Network', 'J1772', None, None, '1', None, None, '2022-09-26'],
    ['174646', 'MEIJER STORES 064 SALINE RD 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48108', '3145 Ann Arbor-Saline Rd', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['174657', 'U-M ANN ARBOR NCRC STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '2800 Plymouth Rd', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['184715', 'NOAA', 'FED_GOV', 'private', 'Drivers must bring their own J1772 cordset for Level 1 charging', None, 'ANN ARBOR', '48108', '4840 S State Rd', None, 'Non-Networked', 'NEMA515', None, '2', None, None, None, '2021-02-22'],
    ['184845', 'EPA Ann Arbor - Station 1', 'FED_GOV', 'private', None, None, 'Ann Arbor', '48105', '2565 Plymouth Rd', None, 'Non-Networked', 'J1772', None, None, '6', None, None, '2021-02-22'],
    ['184846', 'EPA Ann Arbor - Station 2', 'FED_GOV', 'private', 'Drivers must bring their own J1772 cordset for Level 1 charging', None, 'Ann Arbor', '48105', '2565 Plymouth Rd', None, 'Non-Networked', 'NEMA515', None, '1', None, None, 'Free', '2021-02-22'],
    ['187890', 'HAMPTON -YPSI DTWYP #1', None, 'public', '24 hours daily', None, 'Ypsilanti', '48197', '515 James L Hart Pkwy', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['187922', 'BMW ANN ARBOR STATION 01', None, 'public', '24 hours daily', None, 'Ann Arbor', '48103', '501 Auto Mall Dr', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['188119', 'Prentice Partners', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '830 Henry Street', None, 'Greenlots', 'J1772', None, None, '10', None, None, '2022-09-26'],
    ['198009', 'Hover + Greene', 'MULTI_UNIT_DWELLING', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '950 Greene St', None, 'EV Connect', 'J1772', None, None, '4', None, None, '2021-11-04'],
    ['198073', 'BEEKMAN STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '1200 Broadway St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['199100', 'FLEET SERVICES DCFC-STATION 4', None, 'public', '24 hours daily', None, 'Ann Arbor, MI', '48104', '301 E. Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['199101', 'FLEET SERVICES DCFC-STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '301 E. Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['199102', 'FLEET SERVICES DCFC-STATION 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '301 E Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['200995', 'FLEET SERVICES DCFC-STATION 3', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '301 E Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['201411', 'U-M ANN ARBOR ANN 1 & 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '1115 E Ann St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['201412', 'U-M ANN ARBOR ANN 3', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '1101-1189 E Ann St', None, 'ChargePoint Network', 'J1772', None, None, '1', None, None, '2022-09-26'],
    ['201416', 'U-M ANN ARBOR SC32', None, 'public', '24 hours daily', None, 'Ann Arbor', '48109', '1024 Greene St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['201417', 'U-M ANN ARBOR NC27 1 & 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48109', '1300 Murfin Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['202411', 'WASHTENAW BP 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48108', '4975 Washtenaw Ave', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['202417', 'WASHTENAW BP 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48108', '4975 Washtenaw Ave', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['216275', 'Suburban Chevrolet', 'CAR_DEALER', 'public', '24 hours daily', 'False', 'Ann Arbor', '48103', '3515 Jackson Rd', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['216276', 'Fourth & Washington Parking Garage', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '123 E Washington St', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['216277', 'Audi Ann Arbor', 'CAR_DEALER', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '2575 S State St', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['216278', 'ProQuest Employee Parking Garage', 'PARKING_GARAGE', 'private', '24 hours daily', None, 'Ann Arbor', '48108', '789 E Eisenhower Pkwy', None, 'Non-Networked', 'J1772', None, None, '4', None, None, '2022-05-05'],
    ['216279', 'Staybridge Suites', 'HOTEL', 'public', '24 hours daily', 'False', 'Ann Arbor', '48108', '3850 Research Park Dr', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-05-05'],
    ['216280', 'Mitsubishi Motor - Ann Arbor Lab', 'PARKING_LOT', 'public', '24 hours daily', 'False', 'Ann Arbor', '48108', '3735 Varsity Dr', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['223001', 'A2DDA STATION 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223002', 'A2DDA STATION 3', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223003', 'A2DDA STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223004', 'A2DDA STATION 4', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223005', 'A2DDA ST 4123', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '320 Thompson St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223006', 'A2DDA STATION 4121', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '320 Thompson St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223007', 'A2DDA 500 E WASH 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '500 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223008', 'A2DDA 500 E WASH 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '500 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223009', 'A2DDA STATION 27', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '123E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223010', 'A2DDA STATION 28', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '115E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223011', 'A2DDA STATION 33', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '123E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223012', 'A2DDA STATION 22', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '115E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223013', 'A2DDA STATION 24', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '115E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223014', 'A2DDA STATION 18', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223015', 'A2DDA STATION 19', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223016', 'A2DDA STATION 20', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223017', 'A2DDA STATION 13', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '120 W Ann St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223018', 'A2DDA STATION 17', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223019', 'A2DDA STATION 15', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223020', 'A2DDA STATION 12', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '120 W Ann St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223021', 'A2DDA STATION 26', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223022', 'A2DDA STATION 8', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223023', 'A2DDA STATION 21', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223024', 'A2DDA STATION 16', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223025', 'A2DDA STATION 25', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223026', 'A2DDA STATION 23', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223027', 'A2DDA STATION 6', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223028', 'A2DDA STATION 31', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223029', 'A2DDA STATION 11', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223030', 'A2DDA STATION 9', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223031', 'A2DDA STATION 29', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223032', 'A2DDA STATION 32', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223033', 'A2DDA STATION 30', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223034', 'A2DDA STATION 7', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223035', 'A2DDA STATION 5', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223036', 'A2DDA STATION 10', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223038', 'A2DDA E WASH CT4K', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '123 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223039', 'A2DDA E WASH CT4K 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '123 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['228549', 'Shell', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '2991 S State St', None, 'eVgo Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26']
    ]

# 1.0 WARMUP
ev_station_count = None # TODO Return length



# print(f"\n1.0 EV station count = {ev_station_count}")

# 1.1 CHALLENGE 01

headers = station_data[10] # TODO access headers


chargepoint_count = 0

for i in range(1,len(station_data)):
    if station_data[i][10] != None:
        chargepoint_count = chargepoint_count + int(station_data[i][10]);

# TODO Implement loop

print(f"\n1.0 ChargePoint network count = {chargepoint_count}")


# 1.2 CHALLENGE 02

# print('\n1.2 Ann Arbor Development Authority charging stations')

# TODO Implement loop

# TODO Uncomment
# Confirm string replacement
# for station in station_data[1:]:
#     if 'Ann Arbor Downtown' in station[1]:
#         print(f"{station[0]} {station[1]}")


# 2.0 BREAK AND CONTINUE


# 2.1 BREAK STATEMENT EXAMPLE

has_ypsi = False
for station in station_data[1:]:
    if station[6].lower() == 'ypsilanti':
        has_ypsi = True
        break # exit loop

# print(f"\n2.1.1 Has Ypsilanti data = {has_ypsi}")

# Alternative (headers lookup)

headers = station_data[0] # column headers
has_ypsi = False
for station in station_data[1:]:
    if station[headers.index('city')].lower() == 'ypsilanti':
        has_ypsi = True
        break # exit loop

# print(f"\n2.1.2 Has Ypsilanti data = {has_ypsi}")


# 2.2 CONTINUE STATEMENT EXAMPLE

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

# TODO Uncomment

# outliers = []
# for vehicle in elec_vehicles[1:]:
#     vehicle_range = int(vehicle[-1]) # Do not name the var range (shadows the range() type)
#     if 225 < vehicle_range < 325:
#         continue # proceed to next iteration (skip)
#     outliers.append(f"{vehicle[1]} {vehicle[2]} (range = {vehicle_range} mpge")

# print(f"\n2.2 City range outliers (n={len(outliers)})")
# pprint(outliers)


# 3.0 WHILE LOOP

# print(f"\n2.0 while loop")

# TODO Implement loop

# Example
# chargepoint_count = 0
# i = 1 # skip the header list
# while i < len(station_data):
#     if station_data[i][headers.index('ev_network')].lower() == 'chargepoint network':
#         chargepoint_count += 1
#     i += 1 # increment

# print(f"\n3.0 ChargePoint network count = {chargepoint_count}")


# 3.1 INFINITE LOOPS

# TODO Uncomment

# print(f"\n2.1 while True")
# i = 0
# while True:
#     print(i, 'infinite loop triggered')
#     if i == 5:
#         print(i, 'infinite loop terminated\n')
#         break # exit the loop
#     i += 1 # increment (note indention)


# 3.2 WHILE LOOP ELSE CONDITION

# TODO Uncomment

# print(f"\n2.2 while loop with else")
# i = 0
# while i < 5:
#     print('I want an EV.')
#     i += 1 # increment
# else:
#     print('Enough said. We believe you.')


# 3.3 WHILE LOOP AND CONDITIONAL STATEMENTS

# TODO Uncomment

# print(f"\n2.3.1 while loop if-else (increment)")
# i = 0
# while i < 10:
#     if i % 2 == 0:
#         print(f"{i} is an even number.")
#     else:
#         print(f"{i} is an odd number.")
#     i += 1 # increment


# TODO Uncomment

# print(f"\n2.3.2 while loop if-else (decrement)")
# i = 10
# while i >= 0:
#     if i % 2 == 0:
#         print(f"{i} is an even number.")
#     else:
#         print(f"{i} is an odd number.")
#     i -= 1 # decrement


# 3.4 WHILE LOOP AND RANGE

# print(f"\n2.4. while loop and range()")
i = 0
while i in range(0, 10, 2):
    # print(f"{i} is an even number.") # TODO UNCOMMENT
    i += 2 # increment by 2


# 3.5 CHALLENGE 03

idx = None # TODO return headers ev_connector_types index to use in loop below
i = 1

# TODO Implement loop

# print(f"\n3.5.1 while loop: convert str to list (slice) = {station_data[8][idx]}")


# 3.6 CHALLENGE 04

first_ypsi_station_idx = None # Don't default to zero
i = 1

# TODO Implement list

# print(f"3.5.1 First Ypsi EV station index val = {first_ypsi_station_idx}")


# 4.0 BUILT-IN INPUT() FUNCTION

streets = (
    'Ann Arbor-Saline Rd',
    'Auto Mall Dr',
    'Boardwalk Dr',
    'Broadway St',
    'Catherine St',
    'Depot St',
    'Eisenhower Place',
    'Ellsworth Rd',
    'Greene St',
    'Henry Street',
    'Jackson Rd',
    'James L Hart Pkwy',
    'Forrest St',
    'Maynard St',
    'Murfin Ave',
    'Plymouth Rd',
    'Research Park Dr',
    'Runway Blvd',
    'Thompson St',
    'Varsity Dr',
    'Wall St',
    'Washtenaw Ave',
    'William St',
    'Woodridge Ave',
    'E Ann St',
    'E Eisenhower Pkwy',
    'E Huron St',
    'E Washington St',
    'N Adams St',
    'N Ashley St',
    'S Main St',
    'S Fifth Ave',
    'S 5th Ave'
    'S Forest Ave',
    'S State Rd',
    'S State St',
    'W Ann St',
    'W Liberty Rd',
    'W Washington',
    'W William St'
    )

# TODO Uncomment
# while True:
#     is_found = False
#     entry = input('\nProvide street name: ')

#     # Attempt to obtain an exact match; otherwise attempt to obtain a case insensitive partial match
#     if entry in streets:
#         is_found = True # exact match obtained
#     else:
#         for street in streets:
#             if entry.lower() in street.lower():
#                 is_found = True
#                 break # partial match obtained, exit loop

#     if is_found:
#         print(f"\nSUCCESS: One or more EV charging stations found on the provided street.")
#         break # exit while loop

#     print(f"\nFAIL: No EV charging stations found on provided street. Provide a different street name.")
