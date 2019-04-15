#!/usr/local/bin/python3
import mysql.connector

conn= mysql.connector.connect(
                            user = "root",         
                            password = "",
                            host = "127.0.0.1",
                            database = "MasterDB",
                            auth_plugin='mysql_native_password')      

cur = conn.cursor()

cur.execute(
    """ CREATE TABLE IF NOT EXISTS departments(
            dept_id             INT(2)              NOT NULL,
            dept_name           VARCHAR(16)         NOT NULL,
            city                VARCHAR(32)         NOT NULL,
            state               VARCHAR(32)         NOT NULL,
        PRIMARY KEY (dept_id),
        UNIQUE  KEY (dept_name)
    );""" 
)

cur.execute(
    """ CREATE TABLE IF NOT EXISTS employees(
            emp_id              INT(4)              NOT NULL,
            username            VARCHAR(32)         NOT NULL,
            first_name          VARCHAR(16)         NOT NULL,
            last_name           VARCHAR(32)         NOT NULL,
            hire_date           DATE                NOT NULL,
            salary              INT                 NOT NULL,
            dept_id             INT(2)              NOT NULL,     
        PRIMARY KEY (emp_id),
        UNIQUE  KEY (username),
        FOREIGN KEY (dept_id) REFERENCES departments (dept_id) ON DELETE CASCADE
    );"""
)

# cur.execute(
#     """ CREATE TABLE IF NOT EXISTS emp_depts(
#             emp_id              INT                 NOT NULL,
#             dept_id             INT                 NOT NULL,
#             start_date          DATE                NOT NULL,
#             end_date            DATE                DEFAULT NULL, 
#         PRIMARY KEY (emp_id, dept_id),
#         FOREIGN KEY (emp_id) REFERENCES employees (emp_id) ON DELETE CASCADE,
#         FOREIGN KEY (dept_id) REFERENCES departments (dept_id) ON DELETE CASCADE
#     );"""
# )

cur.close()
conn.close()