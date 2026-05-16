from datetime import datetime

# Check if a zoo keeper is authenticated
zoo_keeper_logged_in = False


def login_required(func):
    # Make sure user is logged in before performing an action.
    def wrapper(*args, **kwargs):
        if not zoo_keeper_logged_in:
            print("Access denied. Zoo keeper must login.")
            return
        return func(*args, **kwargs)
    return wrapper


def log_activity(func):
    # Log zoo keeper activities with a timestamp
    def wrapper(*args, **kwargs):
        print("====================================")
        # Show which task is being performed
        print(f"Keeper Action: {func.__name__}")   
        # Record datetime when the task happens
        print(f"Timestamp: {datetime.now()}")      
        print("Status: In progress...")

        result = func(*args, **kwargs)         
        # Call back to the original
        #  function
        print("Status: Completed successfully.")
        print("====================================\n")

        return result                          

    return wrapper