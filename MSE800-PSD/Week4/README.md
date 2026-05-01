# File Structure
database.py: Contains the logic for creating connections and executing SQL DDL commands.  

main.py: Entry point that orchestrates the table creation sequence.  

Provides a detailed breakdown of all five tables (`customers`, `branches`, `receipts`, `currencies`, and `market_rates`) including their specific fields and constraints.

### 1. Customers Table
Description: Stores essential personal data including full names, nationalities, and unique document identification.  

This table is critical for regulatory compliance and KYC (Know Your Customer) protocols. It allows the system to link every financial transaction to a verified individual.

### 2. Branches Table
Description: Manages physical exchange locations, agent names, and operational statuses (Active/Inactive).  

Necessary for operational oversight. It enables the tracking of which physical site processed a transaction and allows administrators to enforce "value limits" to manage risk per location.  

### 3. Currencies Table
Description: A master list of supported currencies, including their major/minor unit names and a flag indicating if exchange is currently permitted.  

Provides a centralized reference for all currency types. By separating this from the rates, we can toggle the availability of a specific currency.

### 4. Market Rates Table
Description: Records the buy and sell rates between currency pairs, timestamped for historical tracking.  

Essential for dynamic pricing. 

### 5. Receipts Table
Description: Recording the amounts paid and received, timestamps for branches and customers.  

Who exchanged money, where they did it, and exactly how much was moved.