import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

# load env vars from .env file
load_dotenv()

# define schema name & path
schema_name = "Fact".lower() # mysql wants lowercase
file_path = r"Windows Path"  # r"" is required for windows path, if not using that you can remove the r

# mysql connection config
config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
}

try:
    # connect to mysql
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # create schema
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {schema_name};")
    cursor.execute(f"USE {schema_name};")

    # read & execute sql commands from file
    with open(file_path, 'r') as file:
        sql_commands = file.read().split(';')
        for command in sql_commands:
            command = command.strip()
            if command:  # skip empty commands
                cursor.execute(command)

    # commit
    cnx.commit()
    print("Schema created and SQL commands executed successfully.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'cnx' in locals():
        cnx.close()
