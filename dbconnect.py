import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                            user = "root",
                            passwd = "mayukh@741201",
                            db = "pythonprogramming")
    c = conn.cursor()

    return c, conn
