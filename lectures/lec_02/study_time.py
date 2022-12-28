
def check_input(hours):
    """Checks input and returns an appraisal of the estimated number of hours per week for study
    and assignment work.

    Parameters:
        hours (float): Hours estimate

    Returns:
        str: Terse appraisal of hours estimate.
    """

    msgs = [
        (
            f"\n{hours} hours/week: A heroic hours estimation for anyone other than a (very)\n"
            f"experienced programmer.\n "
            f"\nStudents are advised to budget additional time for the weekly readings,\n"
            f"assignments, Slack conversations, and office hour visits.\n"
            ),
        (
            f"\n{hours} hours/week: Even for students with a solid programming background we\n"
            f"believe this number underestimates the hours required.\n"
            f"\nStudents are advised to budget additional time for the weekly readings,\n"
            f"assignments, Slack conversations, and office hour visits.\n"
            ),
        (
            f"\n{hours} hours/week: A reasonable hours estimation for students with a solid\n"
            f"programming background.\n"
            f"\nStudents with little or no programming experience are advised to budget\n"
            f"additional time for the weekly readings, assignments, Slack conversations,\n"
            f"and office hour visits.\n"
            ),
        (
            f"\n{hours} hours/week: For students with little or no programming experience we\n"
            f"believe this number underestimates the hours required.\n"
            f"\nStudents are advised to budget additional time for the weekly readings,\n"
            f"assignments, Slack conversations, and office hour visits.\n"
            ),
        (
            f"\n{hours} hours/week: For students with little or no programming experience we\n"
            f"believe this number may still fall below the hours required.\n"
            f"\nStudents are advised to budget additional time for the weekly readings,\n"
            f"assignments, Slack conversations, and office hour visits.\n"
            ),
        (
            f"\n{hours} hours/week: A reasonable hours estimation for students with little or no\n"
            f"programming experience.\n"
            ),
        (
            f"\n{hours} hours/week: Contact the teaching team if your weekly time committment\n"
            f"outside of lectures/labs exceeds ten (10) hours on a regular basis.\n"
            )
        ]

    if hours < 4.0:
        return msgs[0]
    elif 4.0 <= hours < 5.0:
        return msgs[1]
    elif 5.0 <= hours < 6.0:
        return msgs[2]
    elif 6.0 <= hours < 7.0:
        return msgs[3]
    elif 7.0 <= hours < 8.0:
        return msgs[4]
    elif 8.0 <= hours < 10.0:
        return msgs[5]
    else:
        return msgs[6]


def main():
    """Entry point for program."""

    msg = '\nEnter number of hours outside of lectures/lab that you plan to spend on this course: '

    while True:
        try:
            print(check_input(float(input(msg))))
            break
        except ValueError:
            print('Input error. Please enter a numeric value.')
            continue


if __name__ == '__main__':
    main()
