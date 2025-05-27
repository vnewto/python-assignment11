import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##Task 2

#connect to database
with sqlite3.connect("../python_homework/python_homework/db/lesson.db") as conn:
    print("Database connected successfully.")

    #join tables, sum up order prices, and group by order
    sql_statement = """SELECT order_id, SUM(line_items.quantity * products.price) as order_total FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    GROUP BY order_id
    """

    #execute statement
    prices_by_order = pd.read_sql_query(sql_statement, conn)
    print(prices_by_order)

#write function to return cumulative sum
def cumulative(row):
   current_total = prices_by_order['order_total'][0:row.name+1]
   return current_total.sum()

#apply function to every row in the dataframe and add it as a new column
prices_by_order['cumulative'] = prices_by_order.apply(cumulative, axis=1)
print(prices_by_order)

#plot on line plot
plt.plot(prices_by_order['order_id'], prices_by_order['cumulative'], color='green')
plt.title('Cumulative Revenue by Order')
plt.xlabel('Order ID')
plt.ylabel('Revenue ($)')
plt.show()