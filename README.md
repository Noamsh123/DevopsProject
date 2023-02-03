Portfolio
===

The Portfolio project is a three tier web application that maintaining a database of football players it can query, insert, update, and delete from the db and it have a ci/cd with multibranch pipeline that build, test, publish and deploy.

#### Application Architecture
The application is comprised of two services:
(1) A mySQL Server which hosts the data and allows to query, insert and modify.

(2) A Python Server that work with flask and serve the data to the nginx

(3) An nginx Server that is used as reverse proxy

All servers run in a docker containers

#### Configuration

The Python Server have 6 APIs that can contact by curl you can see an examples in the e2e.sh or you can contact them through the url

The Python Server connect to the mySQL db with the dbconnect.py

The nginx listen on port 80 and redirect all the request to the Python app that run on port 5000 in the local network

#### APIs
Get-id allowing to query all the ids in the db.

Get-person allowing to query all data about one person using his id.

Add allowing to add a player to the table.

Update allowing to update some data about a player.

Delete allowing to delete player from the db.


#### Building & Running the app
In order to build the app you will need:

(1) Docker

(2) Docker compose

### Steps:

(1) docker compose up -d


#### ci/cd with Jenkins multibranch pipeline
The ci/cd process including three branches

(1) Feature branch build the application and test it end to end.

(2) Release branch build the application test it end to end and calculate a new version and release to ECR(Elastic Container Registry).

(3) Main branch build the application test it end to end publish to ECR and deploy to the prodection server.