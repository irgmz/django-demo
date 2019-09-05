git add .
git commit -m "fix rb#13"
git push

REVISION=$(git rev-parse HEAD)

DATA='{ \
    "access_token":"e3211e5f9042453497de0f363739b770", \
    "environment":"development", \
    "revision":"REV", \
    "rollbar_username":"ajtran", \
    "local_username":"ajtran", \
}'

FINAL="${DATA/REV/$REVISION}"

curl \
    --request POST \
    --url https://api.rollbar.com/api/1/deploy/ \
    --header 'content-type: application/json' \
    --data $FINAL
