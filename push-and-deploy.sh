#!/bin/bash

if [ $# -eq 1 ]; then
    ENV=$1
else
    echo "Usage: sh push-and-deploy.sh [environment]"
    exit 1
fi

git push

REV=$(git rev-parse HEAD)

DATA='{"access_token":"aa62403d7a154b6e88d084617aa30d10","environment":"'$ENV'","revision":"'$REV'","rollbar_username":"ajtran","local_username":"ajtran"}'

curl \
    --request POST \
    --url https://api.rollbar.com/api/1/deploy/ \
    --header 'content-type: application/json' \
    --data $DATA

echo
echo
echo "."
echo "."
echo "Deployed to $ENV"
echo
echo "Latest Git SHA: $REV"
