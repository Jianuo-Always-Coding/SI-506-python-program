# START PROBLEM SET 03

tv_shows = [
    "Only Murders in the Building | Comedy | 2021 | 8.1 | 99 | Hulu",
    "Reservation Dogs | Crime | 2021 | 8.1 | 99 | Hulu",
    "Justified | crime | 2010 | 8.6 | 97 | Hulu",
    "Better Things | Comedy | 2016 | 7.8 | 98 | Hulu",
    "Grey's Anatomy | Drama | 2005 | 7.6 | 84 | hulu",
    'Atlanta | comedy | 2016 | 8.6 | 99 | Hulu',
    'Fargo | Drama | 2014 | 8.9 | 97 | Hulu',
    'Lost | Scifi | 2004 | 8.3 | 85 | Hulu',
    "What We Do in the Shadows | Horror | 2019 | 8.9 | 92 | Hulu",
    'American Horror Story | Horror | 2011 | 8.0 | 77 | Hulu',
    'Yellowjackets | Horror | 2021 | 7.9 | 100 | Hulu',
    "Bridgerton | Drama | 2020 | 7.3 | 82 | Netflix",
    'Stranger Things | Scifi | 2016 | 8.7 | 96 | Netflix',
    'Dark | Thriller | 2017 | 8.8 | 93 | Netflix',
    "The Queen's Gambit | Drama | 2020 | 8.6 | 92 | Netflix",
    'Mindhunter | Thriller | 2017 | 8.6 | 90 | Netflix',
    'Money Heist | Crime | 2017 | 8.5 | 90 | Netflix',
    'Lucifer | Fantasy | 2016 | 8.1 | 90 | netflix',
    'The Witcher | fantasy | 2019 | 8.2 | 89 | Netflix',
    'Ozark | Crime | 2017 | 8.4 | 89 | Netflix',
    'The Crown | Drama | 2016 | 8.6 | 89 | Netflix',
    'Cobra Kai | Comedy | 2018 | 8.6 | 89 | Netflix',
    'The Good Place | Comedy | 2016 | 8.2 | 97 | Netflix',
    'Better Call Saul | Crime | 2015 | 8.9 | 98 | Netflix',
    'On My Block | drama | 2018 | 7.9 | 93 | netflix',
    'New Girl | comedy | 2011 | 7.7 | 95 | Netflix',
    'The 100 | Scifi | 2014 | 7.6 | 93 | Netflix',
    'Lost in Space | Scifi | 2018 | 7.3 | 84 | Netflix',
    'The Marvelous Mrs. Maisel | Comedy | 2017 | 8.7 | 89 | Prime',
    'As We See It | Comedy | 2022 | 9.1 | 90 | Prime',
    'The Cleaning Lady | crime | 2022 | 7.0 | 60 | Prime',
    'The Lord of the Rings: The Rings of Power | fantasy | 2022 | 6.9 | 84 | Prime',
    'The Wheel of Time | Fantasy | 2021 | 7.1 | 82 | Prime',
    'Fleabag | drama | 2016 | 8.7 | 100 | Prime',
    'Star Trek: The Next Generation | Scifi | 1987 | 8.7 | 92 | Prime',
    'The Expanse | Scifi | 2015 | 8.5 | 94 | Prime',
    'Severence | Thriller | 2022 | 8.7 | 97 | AppleTV',
    'Trying | Comedy | 2021 | 7.9 | 93 | AppleTV',
    'For All Mankind | Scifi | 2019 | 8.0 | 90 | AppleTV',
    'Dickinson | Comedy | 2019 | 7.6 | 92 | AppleTV',
    'See | Scifi | 2019 | 7.6 | 63 | appleTV'
    ]

tv_shows_to_update = [
    ['The Bold Type', 'Drama', '2017', '7.8', '89', 'Hulu'],
    ['Suits', 'Drama', '2011', '8.5', '90', 'Netflix'],
    ['Virgin River', 'Drama', '2019', '7.4', '84', 'Netflix']
]

# PROBLEM 1
print("Problem 1\n")
# 1.1
format_tv_shows = []
# 1.2
for show in tv_shows_to_update:
    for item in show:
        newItem = show[0] + ' | ' + show[1] + ' | ' + show[2] + ' | ' + show[3] + ' | ' + show[4] + ' | ' + show[5]
    format_tv_shows.append(newItem)
# print(format_tv_shows)
# 1.3
newShow = []
index = 0
for i in range(0,len(tv_shows)):
    newShow.append(tv_shows[i].split(' | '))
    # print(newShow[i][1])
    if newShow[i][1] == 'Horror':
        tv_shows[i] = format_tv_shows[index]
        index = index + 1    
# print(tv_shows)

# print(format_tv_shows)

# TODO Implement loop

# TODO Perform slice assignment

# print(f"Problem 1 - Shows Updated: \n{tv_shows[8:11]}")


# PROBLEM 2
print("Problem 2\n")

drama = []
newShow = []
for i in range(0,len(tv_shows)):
    newShow.append(tv_shows[i].split(' | '))
    # print(newShow[i][0])
    if newShow[i][1].lower() == 'drama':
        drama.append(newShow[i][0])

# TODO Implement loop

# print(f"\Problem 2 - drama list: \n{drama}")


# PROBLEM 3
print("Problem 3\n")

total_ratings = 0
newShow = []

for i in range(0,len(tv_shows)):
    newShow.append(tv_shows[i].split(' | '))
    total_ratings = total_ratings + int(newShow[i][4])

# TODO Implement loop

# print(f"total_ratings: {total_ratings}")

avg_rating_all_shows = round(total_ratings / len(tv_shows), 2)

# print(f"\Problem 3 - average rating: {avg_rating_all_shows}")


# PROBLEM 4
print("Problem 4\n")

above_avg = []
below_avg = []

# TODO Implement loop

newShow = []

for i in range(0,len(tv_shows)):
    newShow.append(tv_shows[i].split(' | '))
    if int(newShow[i][4]) > avg_rating_all_shows:
        above_avg.append(newShow[i][0])
    else:
        below_avg.append(newShow[i][0])



# print(f"\nPROBLEM 4 above average shows: {above_avg}")
# print(f"\nPROBLEM 4 below average shows: {below_avg}")


# PROBLEM 5
print("Problem 5\n")

tv_shows_new = []
newShow = []

for i in range(0,len(tv_shows)):
    newShow.append(tv_shows[i].split(' | '))
    averange_score = int((float(newShow[i][3]) * 10 + int(newShow[i][4])) / 2)
    tv_shows_new.append(newShow[i][0] + ' - ' + str(averange_score))



# TODO Implement loop

# print(f"\nPROBLEM 5 tv_shows_new = {tv_shows_new}")


# PROBLEM 6
print("Problem 6\n")

min_year = 2022
oldest_show = None

newShow = []
index = 0

for i in range(0,len(tv_shows)):
    newShow.append(tv_shows[i].split(' | '))
    if int(newShow[i][2]) < min_year:
        min_year = int(newShow[i][2])
        index = i
oldest_show = newShow[index][0]

# TODO Implement loop

# print(f"\nPROBLEM 6 - oldest_shows: {oldest_show}")


# Problem 7
print("Problem 7\n")

select_content = []
newShow = []

for i in range(0,9,2):
    if tv_shows[i].split(' | ')[5].lower() == 'hulu':
        select_content.append(tv_shows[i])

    
# TODO Implement loop

# print(f"\nPROBLEM 7 - select_content: \n{select_content}")


# PROBLEM 8
print("Problem 8\n")

unique_genre = []
unique_streaming_service = []

newShow = []
add_genre = True
add_service = True

for item in tv_shows:
    newShow = item.split(' | ')
    for genre in unique_genre:
        if genre == newShow[1].lower():
            add_genre = False
            break;
    if add_genre:
        unique_genre.append(newShow[1].lower())
    add_genre = True

    for service in unique_streaming_service:
        if service == newShow[5].lower():
            add_service = False
            break;
    if add_service:
        unique_streaming_service.append(newShow[5].lower())
    add_service = True


    


# TODO Implement loop

# print(f"\nPROBLEM 8 unique genre list: \n {unique_genre}")
# print(f"\nPROBLEM 8 unique streaming service list: \n{unique_streaming_service}")

# END PROBLEM SET 03
