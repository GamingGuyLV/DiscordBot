import sqlite3


con = sqlite3.connect("Main.db")
cur = con.cursor()

cur.execute('''
  CREATE TABLE IF NOT EXISTS balances (
    servermemberid TEXT NOT NULL,
    balance REAL NOT NULL,
    membername TEXT NOT NULL,
    servername TEXT NOT NULL,
    PRIMARY KEY (servermemberid)
    )
''')