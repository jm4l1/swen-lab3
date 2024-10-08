#! /bin/bash

clear_arp() {
    echo "Clearing Arp Entries"
    (for e in $(arp -a | sed -n 's/.*(\([^()]*\)).*/\1/p'); do arp -d $e; done)
}

send_request() {
    curl \
    -s \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"user_name" : "'${USER_NAME}'" , "password" : "'$1'"}' \
    http://${SERVER_NAME}:${SERVER_PORT} > /dev/null

    return $?
}

generate_password() {
  password=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
  echo $password
}

password="$(generate_password)"
sleep_time=5
while true
do
    send_request "${password}"
    if [ ! $? -eq 0 ]; then
        echo "No response from server, updating password"
        password="$(generate_password)"
    else
         echo "Request completed to server"
    fi
   
    sleep $sleep_time
done

