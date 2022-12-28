# START LAB EXERCISE 02

wellbeing_resources_data = """Counseling and Psychological Services (CAPS):734-764-8312
Dean of Students Office:734-764-7420
Ginsberg Center for Community Service Learning:734-763-3548
Maize and Blue Cupboard (MBC):734-936-2794
Multi-ethnic Student Affairs (MESA):734-763-9044
Office of Student Conflict Resolution:734-936-6308
Services for Students with Disabilities (SSD):734-763-3000
SilverCloud:
Sexual Assault Prevention and Awareness Center (SAPAC):734-764-7771
Spectrum Center:734-763-4186"""

# Problem 1
wellbeing_resources = wellbeing_resources_data.splitlines()

# Problem 2
wellbeing_resource_with_no_phone = wellbeing_resources[7]

# Problem 3
wellbeing_resources_temp = wellbeing_resources_data.splitlines()

# Problem 4
# wellbeing_resources_temp.<METHOD CALL>
wellbeing_resources_temp.remove(wellbeing_resources_temp[7])

# Problem 5
# wellbeing_resources_temp.<METHOD CALL>
wellbeing_resources_temp.reverse()
# print(wellbeing_resources_temp)
# Problem 6
additional_data = 'Office of the Ombuds:734-763-3545'
wellbeing_resources.append(additional_data)
# Problem 7
new_data_index = wellbeing_resources.index(additional_data)

# Problem 8
elements_sliced = wellbeing_resources[4:9]
# print(elements_sliced)
