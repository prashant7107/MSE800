import zoo_decorator
from zoo_decorator import login_required,log_activity 

username = "zoo"
password = "zoopass"

@log_activity
def login(user, pw):
    # Zoo keeper logs in and start working.
    if user == username and pw == password:
        zoo_decorator.zoo_keeper_logged_in = True
        print("Zoo keeper login successful.")
    else :
        print("Invalid credentials. Access denied!!")

@login_required
@log_activity
def feed_animal(name, food):
    # Log of feeding an animal their daily food.
    print(f"{name} was fed {food}") 

@login_required
@log_activity
def clean_cell(cell_name):
    # Log of cleaning animal shelter.
    print(f"{cell_name} has been cleaned")

@login_required
@log_activity
def logout(name):
    # Zoo keeper logs in and ends working.
    zoo_decorator.zoo_keeper_logged_in = False
    print(f" Zoo Keeper {name} has logged out.")