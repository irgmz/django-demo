#!/bin/bash

if [ $# -eq 1 ]; then
    ENV=$1
else
    echo "Usage: sh push-and-deploy.sh [environment]"
    exit 1
fi

git push

REV=$(git rev-parse HEAD)

DATA='{"access_token":"e3211e5f9042453497de0f363739b770","environment":"'$ENV'","revision":"'$REV'","rollbar_username":"ajtran","local_username":"ajtran"}'

curl \
    --request POST \
    --url https://api.rollbar.com/api/1/deploy/ \
    --header 'content-type: application/json' \
    --data $DATA

echo $REV
