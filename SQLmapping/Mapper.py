#!/usr/local/bin/python3
import mysql.connector as connection
    
class Base:
    def connect(self, sql_cmd):
        conn = connection.connect(user = "root", password = "", host = "127.0.0.1",
                            database = "MasterDB", auth_plugin='mysql_native_password')
        cur = conn.cursor()
        cur.execute(sql_cmd)
        conn.commit()
        cur.close()
        conn.close()

    def connect_fetch(self, sql_cmd):
        conn = connection.connect(user = "root", password = "", host = "127.0.0.1",
                            database = "MasterDB", auth_plugin='mysql_native_password')
        cur = conn.cursor()
        cur.execute(sql_cmd)
        return cur.fetchall()


class Insert(Base):
    def employee(self,emp_id,username,first_name,last_name,hire_date,salary,dept_id):
        sql_cmd = """
            INSERT INTO employees (
                emp_id,username,first_name,last_name,hire_date,salary,dept_id) 
            VALUES ({0},'{1}','{2}','{3}','{4}',{5},{6});""".format(emp_id,username,
                                            first_name,last_name,hire_date,salary,dept_id)
        self.connect(sql_cmd)

    def department(self,dept_id,dept_name,city,state):
        sql_cmd = """
            INSERT INTO departments (
                dept_id,dept_name,city,state) 
            VALUES ({0},'{1}','{2}','{3}');""".format(dept_id,dept_name,city,state)
        self.connect(sql_cmd)

    def emp_depts(self,emp_id,dept_id,start_date):
        sql_cmd = """
            INSERT INTO emp_depts (
                emp_id,dept_id,start_date) 
            VALUES ({0},{1},'{2}');""".format(emp_id,dept_id,start_date)
        self.connect(sql_cmd)


class Select(Base):
    def avg_city_salary(self):
        sql_cmd = """
            SELECT d.city, avg(e.salary) as AvgSalary
            FROM departments d
            INNER JOIN employees e ON d.dept_id = e.dept_id
            GROUP BY d.city
            ORDER BY AvgSalary desc
        """
        return self.connect_fetch(sql_cmd)

    def now(self):
        sql_cmd = """
            SELECT NOW();
        """
        return self.connect_fetch(sql_cmd)


# Insertion of Departments
Insert().department('10','Finance','New York','New York')
Insert().department('11','Software','San Francisco','California')
Insert().department('13','Aerospace','Boston','Massachussets')

# Insertion of Employees
Insert().employee('1001','user1','first1','last1','2019-04-01','200000','11')
Insert().employee('1002','user2','first2','last2','2019-04-01','300000','11')
Insert().employee('1003','user3','first3','last3','2019-04-01','150000','10')
Insert().employee('1004','user4','first4','last4','2019-04-01','250000','11')
Insert().employee('1005','user5','first5','last5','2019-04-01','350000','13')
Insert().employee('1006','user6','first6','last6','2019-04-01','180000','10')
Insert().employee('1007','user7','first7','last7','2019-04-01','900000','10')
Insert().employee('1008','user8','first8','last8','2019-04-01','100000','13')
Insert().employee('1009','user9','first9','last9','2019-04-01','450000','10')
Insert().employee('1010','user10','first10','last10','2019-04-01','700000','13')

# Printing of Average Salary By City
print(Select().avg_city_salary())

# Printing Current Date and Time
print(Select().now())