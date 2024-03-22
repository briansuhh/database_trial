## How to create a MySQL database using MySQL Workbench
1. Open Mysql Workbench
2. Create a new schema or database
3. Create a new table

## How to connect to MySQL database using Python
1. Create a MySql configuration file
    ```python
    dbConfig = {
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'database': 'my_books',
    }
    ```
2. Create a virtual environment
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
4. Install the mysql-connector-python package
    ```bash
    pip install mysql-connector-python
    ```
5. Create a connection to the database
    ```python
    import mysql.connector
    ```
