import sqlite3
conn = sqlite3.connect('sales.db')
c = conn.cursor()
# c.execute('''
# CREATE TABLE IF NOT EXISTS sales (
#     order_id INTEGER,
#     product TEXT,
#     price REAL,
#     quantity INTEGER,
#     salesperson TEXT
# )
# '''
# )
# data = [
#     (1001, '手机', 1999, 2, '张三'),
#     (1002, '电脑', 4999, 1, '李四'),
#     (1003, '耳机', 199, 5, '王五'),
#     (1004, '手机', 1899, 3, '张三'),
#     (1005, '电脑', 4999, 1, '李四'),
#     (1006, '耳机', 199, 5, '王五'),
#     (1007, '平板', 2999, 2, '赵六')
# ]
# c.executemany('INSERT INTO sales VALUES (?,?,?,?,?)', data)
# conn.commit()
c.execute('SELECT * FROM sales')
rows = c.fetchall()
for row in rows:
    print(row)
c.execute('SELECT *,price*quantity AS total_price FROM sales WHERE total_price > 2000')
print(c.fetchall())
c.execute('select *,price*quantity AS total_price FROM sales ORDER BY total_price DESC ')
print(c.fetchall())
c.execute('SELECT salesperson,SUM(price*quantity) AS total_price FROM sales GROUP BY salesperson')
print(c.fetchall())
conn.close()