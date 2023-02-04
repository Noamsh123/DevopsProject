import mysql.connector

def db_connect():
    # global cnx
    # global cursor
    global mydb
    global cursor

    mydb = mysql.connector.connect(
    user="root",
    host="mysql",
    port = 3306,
    password="password"
    )   
    cursor = mydb.cursor()



def run_select(command):
  db_connect()
  cursor.execute("USE players;")
  cursor.execute(command)

  results = cursor.fetchall()
  mydb.close()
  return results

def run_insert_query(command):
    db_connect()
    cursor.execute("USE players;")
    cursor.execute(command)
    mydb.commit()
    mydb.close()

def health():
    db_connect()
    mycursor = mydb.cursor()
    try:
        mycursor.execute("select 1;")
        return '1'
    except:
        return '0'

if __name__ == "__main__":
    health()