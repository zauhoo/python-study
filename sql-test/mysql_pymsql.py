#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/10 23:21
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : mysql_pymsql.py

import pymysql

mydb = pymysql.connect(
    host="192.168.32.128",
    user="root",
    password="mariadb",
)

mariadb_sql = {
    "create_db": "CREATE DATABASE IF NOT mydatabase",
    "show_db": "SHOW DATABASES",
    "create_table": """
create table if not exists person(
    id      int primary key auto_increment,
    name    varchar(100) not null unique,
    age     int
)
""",
    "show_table": "SHOW TABLES",
    "alter_table": "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY",
    "insert_table": "INSERT INTO customers (name, address) VALUES (%s, %s)",
    "select_value": "SELECT name, address FROM customers",
    "order_value": "SELECT * FROM customers ORDER BY name DESC",
    "delete_value": "DELETE FROM customers WHERE address = %s",
    "update_value": "UPDATE customers SET address = %s WHERE address = %s",
    "delete_table": "DROP TABLE IF EXISTS mydatabase"
}

cursor = mydb.cursor()
mydb.begin()
cursor.execute()
cursor.execute()
cursor.execute()
cursor.execute()
