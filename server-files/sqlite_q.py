import sqlite3


def fetchall(str_databaseName,str_tableName):
	conn = sqlite3.connect(str_databaseName)
	c = conn.cursor()
	c.execute('SELECT * FROM str_tableName')
	print c.fetchall()
	conn.close()

def insert(str_databaseName,str_values):
	conn = sqlite3.connect(str_databaseName)
	c = conn.cursor()
	c.execute('''
          INSERT INTO devices
          VALUES values(?)
          ''',(str_values))
	conn.commit()
	conn.close()

#Function to log messages to database     
def log(message):
    db = sqlite3.connect('log.db')
    c = db.cursor()
    c.execute('Insert into logs(time,message) values(?,?)',(time.time(),message))
    db.commit()
    db.close()

#Convert SQLite query results to dictionary
def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect('rh.db')
c = conn.cursor()
c.execute('SELECT * FROM devices')
x = c.fetchall()
conn.close()

# con = sqlite3.connect("rh.db")
# con.row_factory = dict_factory
# cur = con.cursor()
# cur.execute("select 1 as a")
# print cur.fetchone()["a"]

# database = 'rh.db'
# table = 'devices'
# value = "1,'Air Handler One','Controler01.ini','192.168.92.68','00-14-22-01-23-45'"
# insert(database,value)
# fetchall(database,table)

# db = sqlite3.connect('rh.db')
# with db:
#     db.row_factory=dict_factory
#     cur = db.cursor()
#     cur.execute("select * from objects")
#     objects = cur.fetchall()
