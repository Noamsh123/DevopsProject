#!/bin/bash
declare -a RESPONSES
# API=( "/person/1234" "/person/1" "" )
RESPONSES+=$(curl -s -o /dev/null -w '%{http_code}' --connect-timeout 2 18.130.32.203:80/person)
RESPONSES+=$(curl -s -o /dev/null -w '%{http_code}' --connect-timeout 2 18.130.32.203:80/person/1)
RESPONSES+=$(curl -X POST -s -o /dev/null -w '%{http_code}' -d 'firstName=asdf&lastName=asdfg' --connect-timeout 2 18.130.32.203:80/person/1234)
RESPONSES+=$(curl -X PUT -s -o /dev/null -w '%{http_code}' -d 'age=25' --connect-timeout 2 18.130.32.203:80/person/1234)
RESPONSES+=$(curl -X DELETE -s -o /dev/null -w '%{http_code}' --connect-timeout 2 18.131.32.203:80/person/1234)


# curl -s -o /dev/null -w '%{http_code}' --connect-timeout 3 18.130.32.203:80/person
# curl -s -o /dev/null -w '%{http_code}' --connect-timeout 3 18.130.32.203:80/person/1
# curl -X POST -s -o /dev/null -w '%{http_code}' -d 'firstName=asdf&lastName=asdfg' --connect-timeout 3 18.130.32.203:80/person/1234
# curl -X PUT -s -o /dev/null -w '%{http_code}' -d 'age=25' --connect-timeout 3 18.130.32.203:80/person/1234
# curl -X DELETE -s -o /dev/null -w '%{http_code}' --connect-timeout 3 18.130.32.203:80/person/1234



for item in "${RESPONSES[@]}"; do
    echo $item
    if [[ $item != "200" ]]; then
        echo "tests faild"
        exit 1
    fi
done
echo "succese"
exit 0