import sqlite3
conn = sqlite3.connect('rh.db')
c = conn.cursor()
c.execute('''
          INSERT INTO devices 
          VALUES (NULL,'Air Handler One','Controler01.ini','192.168.92.68','00-14-22-01-23-45')
          ''')
c.execute('''
          INSERT INTO devices 
          VALUES (NULL,'Air Handler Two','Controler02.ini','192.168.92.69','00-14-22-01-23-45')
          ''')
conn.commit()
conn.close()