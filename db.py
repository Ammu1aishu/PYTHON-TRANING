import MySQLdb
host = 'localhost'
username = 'root'
passwd = 'root123'
db = 'training'

db_con=MySQLdb.connect(host,username,passwd,db)
db_cur=db_con.cursor()
sql = "select * from datas" 
db_cur.execute(sql)
