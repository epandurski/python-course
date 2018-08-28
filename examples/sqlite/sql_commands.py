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
