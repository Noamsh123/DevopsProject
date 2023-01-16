from flask import Flask, request, abort, jsonify
from db import dbconnect
# import mysql.connector

print("hello")

app = Flask(__name__)
# print(app)

@app.route("/person", methods=["GET"])
def get_id():
    query = dbconnect.run_select(fr"select player_id from active_players;")
    result = {"id": []}
    for item in query:
        result["id"].append(item[0])
    return result



@app.route("/person/<id>", methods=["POST"])
def add(id):
    # id_input = id
    # id = request.form.get("id")
    age = request.form.get("age")
    # print(age)
    # age = str(age)
    # age = float(age)
    age = int(age)
    country = request.form.get("country")
    # dbconnect.run_insert_query(fr"DELETE FROM active_players;")
    dbconnect.run_insert_query(fr"INSERT INTO active_players (player_id, age, country) VALUES ('{id}', {age}, '{country}');")
    return "damm"


@app.route("/person/<id>", methods=["PUT"])
def update(id):
    age = request.form.get("age")
    age = int(age)
    country = request.form.get("country")
    # dbconnect.run_insert_query(fr"DELETE FROM active_players;")
    dbconnect.update(fr"UPDATE active_players SET country = '{country}', age = {age} WHERE player_id = '{id}'")

    return "ok"
    


@app.route("/health")
def health():
    print("=================1================")
    res = dbconnect.health()
    print("==================2===============")
    print(res)
    if res == '1':
        return "OK\n"
    else:
        return '2'

if __name__ == "__main__":
    app.run(host='0.0.0.0')




#db connection

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


# def DB_INITIALIZATION():
#     db_connect()
#     print(" If this is the only message you see while running this file: Data Base is connected and runing")
#     # cnx.commit()
#     mydb.close()


# def health():
#     mycursor = mydb.cursor()
#     mycursor.execute("select 1;")
#     # run_sql_command("select 1;")
#     try:
#         mycursor.execute("select 1;")
#         print("DB Works and connected")
#         return '1'
#     except:
#         return '0'

# if __name__ == "__main__":
#     DB_INITIALIZATION()
#     health()

# @app.route("/health")
# def health():
#     res = dbconnection.health()
#     if res == '1':
#         return "OK\n"
#     else:
#         return '0'


# docker exec -it mydb bash -c 'mysql -u root -ppassword'
# curl -X POST -F "age=23&country=israel" localhost:5000/person/129
# DELETE FROM active_players;