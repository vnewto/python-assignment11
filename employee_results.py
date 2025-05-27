import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Task 1
#connect to sql database
with sqlite3.connect("../python_homework/python_homework/db/lesson.db") as conn:
    print("Database created and connected successfully")
    
    sql_statement = """ SELECT last_name, sum(price * quantity) AS revenue FROM employees 
    JOIN orders ON employees.employee_id = orders.order_id
    JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON products.product_id = line_items.product_id
    GROUP BY employees.employee_id;
    """

    employees_revenue = pd.read_sql_query(sql_statement, conn)
    print(employees_revenue)

#make a bar plot
plt.bar(employees_revenue['last_name'], employees_revenue['revenue'], width=0.8, color='pink')
plt.title('Total Revenue by Employee')
plt.xlabel('Employee')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45, ha='right')
plt.show()


##Task 2