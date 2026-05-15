from decorators import log_activity

# when this is called, it works like log_activity(student_login())
@log_activity
def student_login(username):
    print(f"{username} logged into the system.")


@log_activity
def submit_assignment(username, assignment):
    # decorator gets username and assignment from *args  
    print(f"{username} submitted {assignment}.")


@log_activity
def view_grades(username):
    print(f"{username} is viewing grades.")
