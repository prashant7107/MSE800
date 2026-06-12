from database import DatabaseManager
from user_manager import UserManager


def main():
    # Initialize database file
    db = DatabaseManager("system.db")
    user_sys = UserManager(db)

    while True:
        print("\n=== SYSTEM MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\n--- Registration ---")
            username = input("Username: ")
            password = input("Password: ")
            full_name = input("Full Name: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            sq = input("Security Question: ")
            sa = input("Security Answer: ")

            success, msg = user_sys.register_user(
                username, password, full_name, dob, sq, sa
            )
            print(f"[{'SUCCESS' if success else 'ERROR'}] {msg}")

        elif choice == "2":
            print("\n--- Login ---")
            username = input("Username: ")
            password = input("Password: ")

            success, result = user_sys.authenticate_user(username, password)
            if success:
                print(f"\n[SUCCESS] Welcome back, {result}!")
            else:
                print(f"[ERROR] {result}")

        elif choice == "3":
            print("\n--- Forgot Password Recovery ---")
            username = input("Enter your username: ")
            question = user_sys.initiate_password_reset(username)

            if question:
                print(f"Security Question: {question}")
                answer = input("Your Answer: ")
                new_pw = input("Enter New Password: ")
                success, msg = user_sys.reset_password(
                    username, answer, new_pw
                )
                print(f"[{'SUCCESS' if success else 'ERROR'}] {msg}")
            else:
                print("[ERROR] Username not found.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()