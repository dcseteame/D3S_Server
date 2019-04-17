ID=ffff

curl -i \
--user admin:password -X POST \
--header "Content-Type:application/json" \
--data '{"time": 123456, "accelerationX": [], "accelerationY": [], "accelerationZ": []}' \
http://localhost:35673/addMeasurement?id=${ID}