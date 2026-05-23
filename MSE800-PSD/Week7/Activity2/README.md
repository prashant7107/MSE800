# Aquarium Management System
Python console application developed to manage the inventory of an aquarium.  
This project includes object-oriented design patterns—the **Factory Pattern** and the **Singleton Pattern**—backed by a local **SQLite database**

## Architecture & Design Patterns  

### 1. Singleton Pattern
The system uses one single, centralized manager instance. The program forces the main `AquariumManager` to have only one active instance
 overriding __new__, prevent duplicate managers from being created.  
if its first time it builds an instance, else returns existing instance.  
flag check **if not hasattr(self, "initialized")** If yes, skips the setup and prevents reset.

### 2. Factory Pattern
Factory Pattern is used to create fish. It keeps the logic of creating a fish within itself keeping rest of the app clean from procedure.


### 3. SQL Storage
The system connects to a local database file named `aquarium.db`.  
In first run, it automatically creates an `inventory` table and seeds it with all 5 fish categories set to a quantity of `0`.


#### Simple Workflow of the Program
[User Input ] ──► [ 1. main.py ] ──► [ 2. manager.py ] ──► [ 3. factory.py ]
                                              │                      │
                                        (Runs SQL Update)    (Creates Fish Object)
                                              ▼                      ▼
                                        [ aquarium.db ] ◄──── [ 4. fish.py ]