# SI 506 Lecture 04

# 1.0 STATEMENTS AND EXPRESSIONS

ala = "American Library Association" # statement

challenges_2019_to_2021 = 377 + 156 + 729 # arithmetical expression

print(challenges_2019_to_2021) # expression


# 1.1 CHALLENGE 01

banned_title = 'Gender Queer: A Memoir'
banned_author = 'Maia Kobabe'
banned_publisher = '(Lion Forge Comics, 2019)'


# 1.2 CHALLENGE 02

print(banned_author, banned_title, banned_publisher)


# 1.3 CHALLENGE 03

banned_book = banned_author + ', ' + banned_title + ' ' + banned_publisher

# Alternative (str.join( < iterable >))
# banned_book = ' '.join([banned_author, banned_title, banned_publisher])

print(banned_book)


# 2.0 FORMATTED STRING LITERALS

author = 'George M. Johnson'

print(f"Author = {author}\n")


# 2.1 CHALLENGE 04

print(f"{banned_book}\n")


# 2.2 CHALLENGE 05

bluest_eye = "Toni Morrison, The Bluest Eye (Holt, Rinehart and Winston, 1970)"
bluest_eye_len = len(bluest_eye)

print(f"bluest_eye char count = {bluest_eye_len}\n")


# 3.0 OBJECT METHODS

event = 'banned books week (18-24 September 2022)'
event_upper = event.upper()

print(f"{event_upper}\n")


# 3.1 CHALLENGE 06

hate_u_give = "Angie Thomas, The Hate You Give (Balzer + Bray, 2017)" # typo

print(f"hate_u_give (id={id(hate_u_give)} = {hate_u_give}\n")

hate_u_give = hate_u_give.replace('You', 'U')

print(f"hate_u_give (id={id(hate_u_give)} = {hate_u_give}\n")


# 3.2 CHALLENGE 07

stamped = "Ibram X. Kendi with Jason Reynolds, Stamped: Racism, Antiracism, and You (Little, Brown Books for Young Readers, 2020)"
stamped_i_count = stamped.count('i')

print(f"stamped 'i' count = {stamped_i_count}\n")


# 4.0 ARITHMETIC OPERATIONS

# 4.1 CHALLENGE 08

votes_cast = 3045
votes_yes = 1141
votes_no = 1904

votes_yes_pct = votes_yes / votes_cast * 100
votes_no_pct = votes_no / votes_cast * 100

print(f"Percentage yes vote = {votes_yes_pct:.2f}\n")
print(f"Percentage no vote = {votes_no_pct:.2f}\n")


# 4.2 CHALLENGE 09

pop_est_2021 = 9923
pop_under_18 = .316

eligible_voters = pop_est_2021 * (1 - pop_under_18)
eligible_voters = int(eligible_voters) # convert float to int

print(f"Eligible voters = {eligible_voters}\n")

# Alternative
# eligible_voters = int(pop_est_2021 - (pop_est_2021 * pop_under_18))

# print(f"Eligible voters = {eligible_voters}\n")

turnout_est_pct = votes_cast / eligible_voters * 100

# Alternative
# turnout_est_pct = (votes_cast / eligible_voters) * 100

print(f"Percentage estimated turnout = {turnout_est_pct:.2f}\n")
