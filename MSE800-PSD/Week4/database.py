import sqlite3

def create_connection():
    conn = sqlite3.connect("moneyexchange.db")
    return conn

def create_table_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customerId INTEGER PRIMARY KEY AUTOINCREMENT,
            documentType TEXT NOT NULL,
            documentNumber TEXT NOT NULL UNIQUE,
            fullName TEXT NOT NULL,
            nationality TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_table_branches():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS branches (
            branchId INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            agentName TEXT NOT NULL UNIQUE,
            valueLimit TEXT NOT NULL,
            status BOOLEAN NOT NULL CHECK (status IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()

def create_table_receipts():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
            receiptId INTEGER PRIMARY KEY AUTOINCREMENT,
            paidAmount REAL NOT NULL,
            receivedAmount REAL NOT NULL,
            timeStamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            branchId INTEGER,
            customerId INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def create_table_currencies():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS currencies (
            currencyId INTEGER PRIMARY KEY AUTOINCREMENT,
            currencyName TEXT NOT NULL,
            isExchangeOk INTEGER NOT NULL CHECK (isExchangeOk IN (0, 1)),
            unitName TEXT NOT NULL,
            minorUnitName TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_table_marketRates():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS market_rates (
            rateId INTEGER PRIMARY KEY AUTOINCREMENT,
            buyRate REAL NOT NULL,
            sellRate REAL NOT NULL,
            updateTimeStamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            baseCurrencyId INTEGER,
            targetCurrencyId INTEGER
        )
    ''')
    conn.commit()
    conn.close()