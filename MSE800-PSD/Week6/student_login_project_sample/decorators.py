from datetime import datetime


# This function is the decorator
def log_activity(func):

    def wrapper(*args, **kwargs):
        print("===================================")
        # Identify the function that is running.
        print(f"Function: {func.__name__}")
        # Log the date time of the func executed
        print(f"Time: {datetime.now()}")
        print("Activity started...")
        
        # store the result from function performed.
        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        return result

    return wrapper
