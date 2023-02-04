#!/bin/bash
ip=localhost
declare -a RESPONSES
API=( "post add" "get id" "get person" "put update" "delete" )

RESPONSES[${#RESPONSES[@]}]=$(curl -X POST -s -o /dev/null -w '%{http_code}' -d 'firstName=asdf&lastName=asdfg' --connect-timeout 2 $ip:80/person/1234)
RESPONSES[${#RESPONSES[@]}]=$(curl -s -o /dev/null -w '%{http_code}' --connect-timeout 2 $ip:80/person)
RESPONSES[${#RESPONSES[@]}]=$(curl -s -o /dev/null -w '%{http_code}' --connect-timeout 2 $ip:80/person/1234)
RESPONSES[${#RESPONSES[@]}]=$(curl -X PUT -s -o /dev/null -w '%{http_code}' -d 'age=25' --connect-timeout 2 $ip:80/person/1234)
RESPONSES[${#RESPONSES[@]}]=$(curl -X DELETE -s -o /dev/null -w '%{http_code}' --connect-timeout 2 $ip:80/person/1234)

declare -a failures
api_num=5
for (( i=0;i<$api_num;i++ ))
do
    echo ${RESPONSES[$i]}
    if [[ ${RESPONSES[$i]} != "200" ]]; then
        failures[${#failures[@]}]=${API[$i]}
        bol=true
    fi
done

if [ $bol ]
then
    for api in "${failures[@]}"; do
        echo "the $api faild"    
     done
     exit 1
fi


echo "succese"
exit 0