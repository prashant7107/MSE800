# Zoo Keeper Management System

## Project Structure
- main.py : entry point, runs the system.
- zoo_keeper.py : contains functions to be perforemd.
- zoo_decorator.py : contains logic of login_required and log_activity.

## Functions of a zoo keeper
A zoo keeper can login to mark entry to the system and start work shift. Only once logged in the keeper can feed the animal, clean animal cells. Once the shift is over the keeper can log out to mark end shift.

## Flow of the program
- The keeper enters credentials for log in.
- The system checks if it is correct.
- If successful, keeper has access to other activities.
- At the end of the shift the keeper can log off.

## Credentials for log in
- username : "zoo"
- password : "zoopass"