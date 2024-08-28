# MySQL Schema Maker

This project automates the creation of a MySQL schema and the execution of SQL commands from a specified file.

## Features

- Creates a new schema in MySQL.
- Executes SQL commands from a file.
- Securely manages MySQL credentials using a `.env` file.

## Packages
pip install mysql mysql-connector-python python-dotenv

## .env file layout

MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost

## Schema name and Filepath
Make sure to update schema name and filepath to where your files are located
