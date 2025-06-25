import sqlite3

conn=sqlite3.connect("jarvis.db")
cursor=conn.cursor()


query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

# query="INSERT INTO sys_command VALUES (null,'notepad','C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2503.16.0_x64__8wekyb3d8bbwe\\Notepad')"
# cursor.execute(query)
# conn.commit()

query="CREATE TABLE IF NOT EXISTS wb_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query="INSERT INTO wb_command VALUES (null,'youtube','https://www.youtube.com/')"
cursor.execute(query)
conn.commit()