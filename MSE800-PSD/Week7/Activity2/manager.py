
import sqlite3
from singleton import Singleton
from factory import FishFactory
class AquariumManager(Singleton):
    def __init__(self):
        self.db_name="aquarium.db"

        # Python calls __init__ every time a class is called, 
        if not hasattr(self, "initialized"):
            self.initialize_database()
            self.initialized = True

    def _execute_query(self, query, params=()):
        #Helper method to handle SQL connections safely.
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()


    def initialize_database(self):
        #Creates the inventory table and seeds it with default fish categories.
        # Create table if it doesn't exist
        self._execute_query('''
            CREATE TABLE IF NOT EXISTS inventory (
                category TEXT PRIMARY KEY,
                quantity INTEGER DEFAULT 0
            )
        ''')
    # Seed default fish categories with 0 if the table is empty
        default_categories = ["Goldfish", "Shark", "Angelfish", "Tuna", "Salmon"]
        for category in default_categories:
            self._execute_query('''
                INSERT OR IGNORE INTO inventory (category, quantity) 
                VALUES (?, 0)
            ''', (category,))
            
       
    def add_fish(self, fish_type: str, count: int):
        
        if count <= 0:
            print("Quantity must be greater than 0.")
            return False
        # Uses FishFactory to validate, then updates the SQL database.
        fish_object = FishFactory.create_fish(fish_type)
        if fish_object:
            self._execute_query('''
                UPDATE inventory 
                SET quantity = quantity + ? 
                WHERE category = ?
            ''', (count, fish_object.category))
            return True
        else:
            print(f"Error: '{fish_type}' is not a valid fish category for the Auckland Aquarium.")
            return False

    def display_inventory(self):
       #Displays each fish category and its available quantity.
        rows = self._execute_query("SELECT category, quantity FROM inventory")
        print(f"{'Fish Category':<20} | {'Quantity Available':<18}")
        print("-" * 45)
        for category, quantity in rows:
            print(f"{category:<20} | {quantity:<18}")