#!/bin/bash

while true; do
    let "SECS = $RANDOM % 5"
    sleep $SECS
    curl http://127.0.0.1:8000/age_verification/\?birthdate\=$RANDOM-09-05
    echo
done
