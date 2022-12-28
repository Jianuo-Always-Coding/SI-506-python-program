# START PROBLEM SET 2
print('Problem Set 2 \n')

wellbeing_resources = 'Counseling and Psychological Services (CAPS)|734-764-8312, '\
'SilverCloud|, '\
'Dean of Students Office|734-764-7420, '\
'Office of Student Conflict Resolution|734-936-6308, '\
'Services for Students with Disabilities (SSD)|734-763-3000, '\
'Maize and Blue Cupboard (MBC)|734-936-2794, '\
'Ginsberg Center for Community Service Learning|734-763-3548, '\
'Sexual Assault Prevention and Awareness Center (SAPAC)|734-764-7771, '\
'Multi-ethnic Student Affairs (MESA)|734-763-9044, '\
'Spectrum Center|734-763-4186'
# PROBLEM 01 (30 points)
print('\nPROBLEM 01')
wellbeing = wellbeing_resources.split(', ')

health = wellbeing[:2]
academic = wellbeing[2:5]
community = wellbeing[-5:-3]
marginalized_comm = wellbeing[-3:]
# print(marginalized_comm)

# PROBLEM 02 (40 points)
print('\nPROBLEM 02')
addl_health_resources = ['UMSI Embedded CAPS Psychologist|Ashley Evearitt',
'Wolverine Wellness|734-763-1320']
health.extend(addl_health_resources)
# print(health)

uhs = 'University Health Service (UHS)|734-764-8320'
health.append(uhs)
# print(health)

trotter = 'Trotter Multicultural Center|734-763-3670'
marginalized_comm.insert(1, trotter)
# print(marginalized_comm)


addl_academic_resources = ['Sweetland Center for Writing', 'Office of the Ombuds']
addl_academic_resource_numbers = ['|734-764-0429', '|734-763-3545']

addl_academic_resources[0] = addl_academic_resources[0] + addl_academic_resource_numbers[0]
addl_academic_resources[1] = addl_academic_resources[1] + addl_academic_resource_numbers[1]
# print(addl_academic_resources)

academic.extend(addl_academic_resources)
# print(academic)
# PROBLEM 03 (20 points)
print('\nPROBLEM 03')
health.reverse()
academic.sort()
# print(academic)
marginalized_comm.sort(reverse=True)
# print(marginalized_comm)
umsi_caps = health.index('UMSI Embedded CAPS Psychologist|Ashley Evearitt')
# print(health)
student_focused_health_resources = health[1:umsi_caps+1]
# print(student_focused_health_resources)

# PROBLEM 04 (10 points)
print('\nPROBLEM 04')
# print(health[0])
uhs = tuple(health[0].split("|"))
# print(uhs)
caps = tuple(health[-1].split("|"))
# print(caps)
marginalized_comm_str = ",".join(marginalized_comm)
# print(marginalized_comm_str)
# END PROBLEM SET