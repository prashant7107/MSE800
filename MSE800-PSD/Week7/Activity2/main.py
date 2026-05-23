from manager import AquariumManager
# USER INTERFACE
def main():
    # Instantiate the Singleton manager
    aquarium = AquariumManager()
    
    # Set up SQL tables and seed initial fish rows
    aquarium.initialize_database()
    
    print("Manage categories: Goldfish, Shark, Angelfish, Tuna, Salmon")

    while True:
        print("\nOptions:")
        print("1. Add Fish to Inventory")
        print("2. Display Current Inventory")
        print("3. Exit System")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            fish_type = input("Enter fish type (e.g., Goldfish): ").strip()
            qty_input = input("Enter quantity to add: ").strip()
            
            try:
                quantity = int(qty_input)
                # Call the singleton instance to add fish using factory validation
                aquarium.add_fish(fish_type, quantity)
            except ValueError:
                print("Invalid input! Quantity must be an integer.")
                
        elif choice == "2":
            # Display inventory using the singleton instance
            aquarium.display_inventory()
            
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()