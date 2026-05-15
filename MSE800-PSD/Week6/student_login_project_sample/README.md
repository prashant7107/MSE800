# Activity Logging System

## Findings & Observations
* decorator.py :
This handles formating and timestamps.
* user.py :
This contains tasks to be performed.
* main.py :
This is the entry point.

## FLow of the program
The programs starts in main.py , after reaching student_login("Mohammad") because the function has decorator @log_activity , the process continues to decorator. It continues to the wrapper. the result = func(*args, kwargs) send flow back to user, where it performs the action inside the function in this case "Mohammad logged into the system.", then the flow comes back to the program.  

The flow executes once for student_login, submit_assignment and view_grades.

## Key findings.
Decorators reduce duplicate logginig code. The code structure is cleaner, it is easier to debug and maintain.