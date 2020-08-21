# CS204-Database

# Requirements
- PostgreSQL (I'm using version 12, but any version should work fine)
- Python 3.17 or newer

# Setup
1. To install the python packages required, Open a command prompt and cd to this directory and enter the following command:
    ```
    pip install -r requirements.txt
    ```

2. Create a database in PostgreSQL with the following command:
    ```
    CREATE DATABASE database_name;
    ```
3. Connect to the new database and execute the following command to create the tables:
    ```
    \i create_tables.sql
    ```
    
4. Execute the following python command to populate the tables:
    ```
    python populate_tables.py
    ```
    
5. Thats it! Start making those queries.
