#!/bin/bash
curl 3.8.158.98:80/person
curl 3.8.158.98:80/person/1
curl -X POST -d 'firstName=asdf&lastName=asdfg' 3.8.158.98:80/person/1234
curl -X PUT -d 'age=25' 3.8.158.98:80/person/1234
curl -X DELETE 3.8.158.98:80/person/1234