import sqlite3

#連接到SQLite資料庫(若資料庫不存在，將創建一個新的資料庫文件)
conn=sqlite3.connect('1.db')

#創建一個游標對象，用於執行SQL查詢
cursor=conn.cursor()

#創建名為meat的表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meat (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
        )''')

#插入資料
cursor.execute("INSERT INTO meat(name,price,quantity)VALUES('chicken',30,5)")
cursor.execute("INSERT INTO meat(name,price,quantity)VALUES('beaf',55,10)")
cursor.execute("INSERT INTO meat(name,price,quantity)VALUES('pork',40,15)")

#提交事務
conn.commit()

#查詢資料
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
print("列表:")
for Meat in meat:
    print(Meat)

#第一次更動
cursor.execute("UPDATE meat SET price=35 WHERE name='pork'")
conn.commit()
print("第一次更動後(將pork的價格改為35):")
#查詢資料
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
for Meat in meat:
    print(Meat)

#第二次更動
cursor.execute("UPDATE meat SET quantity=30 WHERE name='chicken'")
conn.commit()
print("第二次更動後(將chicken的數量改為30):")
#查詢資料
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
for Meat in meat:
    print(Meat)

#第三次更動
cursor.execute("DELETE FROM meat WHERE price=40")
conn.commit()
print("第三次更動後(刪除價格為40的資料):")
#查詢資料
cursor.execute("SELECT*FROM meat")
meat=cursor.fetchall()
for Meat in meat:
    print(Meat)
    
cursor.execute('''
        DROP TABLE meat''')

#關閉游標和連接
cursor.close()
conn.close()