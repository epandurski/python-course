# import psycopg2
import sqlite3

# conn = psycopg2.connect("host=localhost dbname=test user=test password=test port=5435")
conn = sqlite3.connect('demo.db')
c = conn.cursor()
c.execute('create table if not exists demo (id int, name text)')
c.execute("insert into demo (id, name) values (1, 'Evgeni')")
c.execute("insert into demo (id, name) values (2, 'Ivan')")
c.execute("insert into demo (id, name) values (3, 'Georgi')")
conn.commit()
n = 1
c.execute('select * from demo where id=?', (n,))
print(c.fetchall())
