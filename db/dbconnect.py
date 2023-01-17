import mysql.connector



# def db_connect():
#     # global cnx
#     # global cursor
#     global mydb
#     global cursor

#     mydb = mysql.connector.connect(
#     user="root",
#     host="localhost",
#     port = 8082,
#     password="password"
#     )   
#     cursor = mydb.cursor()


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



def DB_INITIALIZATION():
    db_connect()
    print(" If this is the only message you see while running this file: Data Base is connected and runing")
    # cnx.commit()
    mydb.close()

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

def update(command):
    db_connect()
    cursor.execute("USE players;")
    cursor.execute(command)
    mydb.commit()
    mydb.close()




def health():
    db_connect()
    mycursor = mydb.cursor()
    # check = mycursor.execute("select 1;")
    # print(check)
    # run_sql_command("select 1;")
    try:
        print("check1")
        mycursor.execute("select 1;")
        print("check2")
        print("DB Works and connected")
        return '1'
    except:
        return '0'

if __name__ == "__main__":
    DB_INITIALIZATION()
    health()