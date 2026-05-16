from zoo_keeper import login,feed_animal,clean_cell,logout

def main():
    # Get credentials to log in and start working
    username = input("Enter username")
    password = input("Enter password")
    login(username,password)

    # Perform activities (if login is successful)

    feed_animal("Lion", "meat")
    clean_cell("Leopard cell")
    logout("Maya")

if __name__ == "__main__":
    main()