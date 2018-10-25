import psycopg2


class DatabaseActions:
    connect = psycopg2.connect(
        database="store-manager",
        host="localhost",
        port=5432,
        user="postgres",
        password="KelynPNjeri@1998",
    )
    cur = connect.cursor()
    connect.autocommit = True
    cur.execute("DROP TABLE IF EXISTS users, products, sales;")
    users = """CREATE TABLE IF NOT EXISTS users(User_id serial PRIMARY KEY,
        Name varchar(100) NOT NULL,
        Username varchar(50) NOT NULL UNIQUE,
        Email varchar(100) NOT NULL UNIQUE,
        Role varchar(25) NOT NULL,
        Password varchar(50) NOT NULL,
        Confirm_password varchar(50) NOT NULL
    );"""
    products = """CREATE TABLE IF NOT EXISTS products(
        Product_id serial PRIMARY KEY,
        Product_name varchar(100) NOT NULL,
        Product_category varchar(100) NOT NULL,
        Product_description varchar(250) NOT NULL,
        Quantity INTEGER NOT NULL,
        Date_created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );"""
    sales = """CREATE TABLE IF NOT EXISTS sales(
        Sales_id serial PRIMARY KEY,
        Sold_by varchar(100) NOT NULL,
        Product_name varchar(50) NOT NULL,
        Product_category varchar(100) NOT NULL,
        Quantity INTEGER NOT NULL,
        Date_created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );"""
    cur.execute(users)
    cur.execute(products)
    cur.execute(sales)
