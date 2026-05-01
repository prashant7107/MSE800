import database as db

def main():
    db.create_table_branches()
    db.create_table_currencies()
    db.create_table_customers()
    db.create_table_marketRates()
    db.create_table_receipts()

if __name__ == "__main__":
    main()
