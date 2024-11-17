
#Create new User
curl -v -X POST "http://127.0.0.1:8000/api/v1/user" \
-H "Content-Type: application/json" \
-d '{
        "name": "name1",
        "last_name": "last_nm1",
        "email": "test22@test.com",
        "password": "123",
        "bday": "1999-11-11",
        "sex": "male",
        "interests": ["i1", "i2"],
        "city": "dc"
}'

#Get user by Id
curl http://127.0.0.1:8000/api/v1/user/2

#Get auth token
curl -v -F username=user1@test.com -F password=123 http://127.0.0.1:8000/token