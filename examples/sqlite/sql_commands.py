import sqlite3
conn = sqlite3.connect('chinook.db')

c = conn.cursor()
c.execute("SELECT artistid FROM artists WHERE name = 'Accept'")
accept_id = c.fetchone()[0]
print("Accept's ID is {}.".format(accept_id))
print("Accept's albums:")
albums = c.execute("SELECT albumid, title FROM albums WHERE artistid = ?", (2,))
for row in albums:
    print(row)
conn.close()


##c = conn.cursor()
##c.execute("""
##CREATE TABLE IF NOT EXISTS expenses
##(
##    egn text PRIMARY KEY NOT NULL,
##    first_name TEXT NOT NULL,
##    last_name TEXT NOT NULL
##)
##""")
##egn = input('EGN: ')
##fn = input('FN: ')
##ln = input('LN: ')
##c.execute('insert into expenses (egn, first_name, last_name) values (?, ?, ?)',
##          (egn, fn, ln))
##conn.commit()
##conn.close()

