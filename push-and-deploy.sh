#!/bin/bash

if [ $# -eq 2 ]; then
    ENV=$1
    MSG="fix rb#$2"
else
    echo "Usage: sh push-and-deploy.sh [environment] [rb# or url]"
    exit 1
fi

git add .
git commit -m "$MSG"
git push

REV=$(git rev-parse HEAD)

DATA='{"access_token":"e3211e5f9042453497de0f363739b770","environment":"'$ENV'","revision":"'$REV'","rollbar_username":"ajtran","local_username":"ajtran"}'

echo $DATA

curl \
    --request POST \
    --url https://api.rollbar.com/api/1/deploy/ \
    --header 'content-type: application/json' \
    --data $DATA
