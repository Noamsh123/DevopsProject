from flask import Flask, request, abort, jsonify, render_template
from db import dbconnect
import json


app = Flask(__name__)

def is_id_exist(id):
    query = dbconnect.run_select(fr"select player_id from active_players where player_id = '{id}';")    
    return len(query) != 0


# @app.route("/")
# def index():
#     return render_template("home.html")


@app.route("/person", methods=["GET"])
def get_id():
    query = dbconnect.run_select(fr"select player_id from active_players;")
    if len(query) == 0:
        return abort(404)
    result = {"id": []}
    for item in query:
        result["id"].append(item[0])
    return jsonify(result)

@app.route("/person/<id>", methods=["GET"])
def get_person(id):
    if not(is_id_exist(id)):
        return abort(404)
    query = dbconnect.run_select(fr"select * from active_players where player_id = '{id}';")
    print(query)
    result = {"id": query[0][0],
    "firstName": query[0][1],
    "lastName": query[0][2],
    "team": query[0][3],
    "age": query[0][4],
    "country": query[0][5]}
    return jsonify(result)



@app.route("/person/<id>", methods=["POST"])
def add(id):
    if is_id_exist(id):
        return "<h3>id is already exist</h3>"

    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    if first_name is None or last_name is None:
        return "<h3>you must enter last name and first name</h3>"
    age = request.form.get("age")
    if age is not None:
        if not(age.isnumeric()):
            return "<h3>age must be a number</h3>"
        age = int(age)

    team = request.form.get("team")
    country = request.form.get("country")
    dbconnect.run_insert_query(fr"INSERT INTO active_players (player_id, first_name, last_name) VALUES ('{id}', '{first_name}', '{last_name}');")
    if age is not None:
        dbconnect.run_insert_query(fr"UPDATE active_players SET age = {age} WHERE player_id = '{id}'")
    if team is not None:
        dbconnect.run_insert_query(fr"UPDATE active_players SET current_team = '{team}' WHERE player_id = '{id}'")
    if country is not None:
        dbconnect.run_insert_query(fr"UPDATE active_players SET country = '{country}' WHERE player_id = '{id}'")
    return "damm"


@app.route("/person/<id>", methods=["PUT"])
def update(id):
    # checking if id exist
    if not(is_id_exist(id)):
        return abort(404)
    age = request.form.get("age")
    team = request.form.get("team")
    country = request.form.get("country")
    
    if age is None and team is None and country is None:
        return "<h3>must be at least one argument</h3>"

    if age is not None:
        if not(age.isnumeric()):
            return "<h3>age must be a number</h3>"
            
        dbconnect.run_insert_query(fr"UPDATE active_players SET age = {age} WHERE player_id = '{id}'")

    if team is not None:
        dbconnect.run_insert_query(fr"UPDATE active_players SET current_team = '{team}' WHERE player_id = '{id}'")

    if country is not None:
        dbconnect.run_insert_query(fr"UPDATE active_players SET country = '{country}' WHERE player_id = '{id}'")
    
    return "ok"
    
@app.route("/person/<id>", methods=["DELETE"])
def delete(id):
    if not(is_id_exist(id)):
        return abort(404)
    dbconnect.run_insert_query(fr"DELETE FROM active_players where player_id = '{id}';")
    return "for now"



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


# docker exec -it mydb bash -c 'mysql -u root -ppassword'