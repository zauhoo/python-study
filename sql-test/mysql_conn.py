#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 13:42
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : mysql_conn.py

import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.32.128",
    user="root",
    passwd="mariadb"
)

mycursor = mydb.cursor()
mariadb_sql = {
    "create_db": "CREATE DATABASE IF NOT mydatabase",
    "show_db": "SHOW DATABASES",
    "create_table": "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))",
    "show_table": "SHOW TABLES",
    "alter_table": "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY",
    "insert_table": "INSERT INTO customers (name, address) VALUES (%s, %s)",
    "select_value": "SELECT name, address FROM customers",
    "order_value": "SELECT * FROM customers ORDER BY name DESC",
    "delete_value": "DELETE FROM customers WHERE address = %s",
    "update_value": "UPDATE customers SET address = %s WHERE address = %s",
    "delete_table": "DROP TABLE IF EXISTS customers"
}
value = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]
adr = ('Yellow Garden 2', )
val = ("Canyon 123", "Valley 345")

mycursor.execute(mariadb_sql["create_db"])

mydb.commit()
