# START PROBLEM SET 5
club_events = [
    'Host Organization; Event Name; Date; Start Time; Duration; Location; Theme',
    'Zouk Dance Club; Zouk Dance Club Lesson; 2022/9/29; 6 PM; 3 hours; Mason Hall; Arts & Music',
    'Student Astronomical Society; SAS Open House; 2022/9/30; 9 PM; 2 hours; Angell Hall; Learning',
    "Lebanese Student Association; Apple Orchard Trip 2022; 2022/10/1; 3 PM; 2 hours; Wiard's Apple Orchard; Social",
    'Zouk dance club; September Zouk Social; 2022/10/1; 7 PM; 5 hours; North Quad; Social',
    'A2 Movimiento Latino; Bachata Class; 2022/10/4; 6:30 PM; 3 hours; Phoenix Center; Art & Music',
    'A2 Movimiento Latino; A2ML Weekly Social; 2022/10/5; 6 PM; 1.5 hours; Hoover Street Studio; Social',
    'STEM Society; STEM Saturday; 2022/11/5; 9 AM; 5 hours; University of Michigan; Community Service',
    'Bujinkan Budo Club; Bujinkan Budo Training Session; 2022/10/3; 7 PM; 1.5 hours; CCRB; Exercise/Fitness',
    'A2 Movimiento Latino; Technique Class; 2022/10/25; 6:30 PM; 3 hours; Phoenix Center; Exercise/Fitness',
    'Ballroom Dance Team; Free Newcomer Lessons; 2022/9/29; 9 pm; 2 hours; CCRB; Exercise/Fitness',
    'MRun; Spartan Grand Classic; 2022/10/1; 7 AM; 8 hours; Lansing MI; Exercise/Fitness',
    'Michigan Sailing Team; Cary Price 2022; 2022/10/1; 8 AM; 30 hours; University of Michigan; Sport',
    'Michigan Weightlifting; Boo Bash 2022; 2022/10/8; 9 AM; 7 hours; Livonia MI; Weightlifting Competition',
    "Chapter of the Scientista Foundation; Homework Help at The Children's Center; 2022/3/24; 1 PM; 24 hours; Detroit MI; Community Service",
    'UNICEF at the University of Michigan; General Meeting; 2022/10/20; 6 PM; 1 hour; Rackham Graduate School; Meeting',
    'MRun; NIRCA Cross Country Great Lakes Regional; 2022/10/21; 12 pm; 31 hours; Shelbyville IN; Race',
    'In the Round Productions at UM; Spring Awakening Performances; 2022/12/2; 8 AM; 56.5 hours; Arthur Miller Theater; Performance',
]

# PROBLEM 01 

# element is a string
def convert_str_to_list(element, separator):
    # print(element)
    reversedList = element.split(separator)
    return reversedList


for i in range(len(club_events)):
    club_events[i] = convert_str_to_list(separator='; ', element=club_events[i])
print(f"\nclub_events = {club_events}")


# PROBLEM 02
# info is a list
def get_duration(event_info):
    time_split = []
    time_split = event_info[4].split(' ')
    return float(time_split[0])

def get_event_month(event_info):
    time_split = []
    time_split = event_info[2].split('/')
    return int(time_split[1])

# time = get_duration(club_events[1])
# print(f"\ntime = {time}")


# PROBLEM 03
def event_with_longest_duration(club_events):
    longest_duration = 0
    # event is a list
    for event in club_events[1:]:
        if(get_duration(event) > longest_duration):
            longest_duration = get_duration(event)
            longest_event = event[1]
    return (longest_event, longest_duration)


# event_name, event_duration = event_with_longest_duration(club_events)
# print(f"\nevent_name = {event_name}")
# print(f"\nevent_duration = {event_duration}")

# PROBLEM 04
def categorize_events_by_month(club_events, month):
    events_by_month = []
    for event in club_events[1:]:
        if(get_event_month(event) == month):
            events_by_month.append(event[1])
    return events_by_month

# oct_events = categorize_events_by_month(club_events, 10)
# print(f"\noct_events = {oct_events}")

# PROBLEM 05
# return type is a list[] input is (list[], String)
def categorize_events_by_theme(club_events, theme):
    events_by_theme = []
    for event in club_events[1:]:
        if(theme.lower() in event[6].lower()):
            events_by_theme.append(event[1])
    return events_by_theme


themes = ['art', 'Social', 'learning']
specified_theme_events = []
for theme in themes:
    specified_theme_events.append(categorize_events_by_theme(club_events, theme))

# print(f"\nspecified_theme_events = {specified_theme_events}")

# PROBLEM 06
# return type is a list[] --> for + function return some events
# time is a string type

def categorize_events_by_time(club_events, time='7 pm', duration=1):
    events_by_time = []
    for event in club_events:
        if(event[3].lower() == time.lower()):
            if(get_duration(event) >= duration):
                events_by_time.append(event[1])
    return events_by_time



# evening_events = categorize_events_by_time(club_events)
# print(f"\nevening_events = {evening_events}")

# PROBLEM 07
def calculate_num_events(club_events, host_org):
    num_events = 0
    for event in club_events:
        if(host_org.lower() == event[0].lower()):
            num_events = num_events + 1
    return num_events

num_events_for_zouk = calculate_num_events(club_events, 'Zouk Dance Club')

# print(f"\nnum_events_for_zouk = {num_events_for_zouk}")

# END PROBLEM SET
