from users import (
    student_login,
    submit_assignment,
    view_grades
)


def main():

    # log_activity.wrapper starts
    # student_login prints msg
    # log_activity.wrapper complets

    student_login("Mohammad")

    # log_activity.wrapper starts
    # submit_assignment prints msg
    # log_activity.wrapper complets

    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    # log_activity.wrapper starts
    # view_grades prints msg
    # log_activity.wrapper complets
    view_grades("Alex")


if __name__ == "__main__":
    main()
