ID=00000000-5c81-8a90-ffff-ffffb02b9897
curl -i --user admin:password -X POST --header "Content-Type:application/json" --data `cat data1.json` http:\/\/localhost:35673\/addMeasurement?id=${ID}